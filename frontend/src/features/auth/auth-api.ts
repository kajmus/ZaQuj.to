const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api'

export interface AuthUser {
  id_user: number
  login: string
}

type RequestOptions =
  | { method: 'GET'; headers?: Record<string, string> }
  | { method: 'POST'; body: unknown; headers?: Record<string, string> }

async function request<T>(
  path: string,
  options: RequestOptions,
): Promise<T> {
  const { method, headers = {} } = options
  const requestOptions: RequestInit = {
    method,
    headers: { ...headers },
  }
  if (method === 'POST') {
    requestOptions.headers = {
      'Content-Type': 'application/json',
      ...headers,
    }
    requestOptions.body = JSON.stringify(options.body)
  }

  let response: Response
  try {
    response = await fetch(`${API_BASE_URL}${path}`, requestOptions)
  } catch {
    throw new Error('Nie udało się połączyć z serwerem. Spróbuj ponownie.')
  }

  if (!response.ok) {
    let message = 'Wystąpił błąd. Spróbuj ponownie.'
    try {
      const data = await response.json() as { detail?: string }
      if (data.detail) message = data.detail
    } catch {
      // Use the generic message when the server does not return JSON.
    }
    throw new Error(message)
  }

  return response.json() as Promise<T>
}

export function registerUser(name: string, password: string): Promise<unknown> {
  return request('/users/register', { method: 'POST', body: { name, password } })
}

export function loginUser(name: string, password: string): Promise<number> {
  return request('/auth/login', { method: 'POST', body: { name, password } })
}

export function verifySession(sessionId: number): Promise<AuthUser> {
  return request('/auth/me', {
    method: 'GET',
    headers: { 'Session-Id': String(sessionId) },
  })
}

export function logoutUser(sessionId: number): Promise<{ message: string }> {
  return request('/auth/logout', { 
    method: 'POST', body: { session_id: sessionId } })
}
