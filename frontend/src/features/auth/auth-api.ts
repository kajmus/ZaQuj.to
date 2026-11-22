const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api'

export interface AuthUser {
  id_user: number
  login: string
}

async function request<T>(
  path: string,
  options: {
    method?: 'GET' | 'POST'
    body?: unknown
    headers?: Record<string, string>
  } = {},
): Promise<T> {
  const { method = 'POST', body, headers = {} } = options
  let response: Response
  try {
    response = await fetch(`${API_BASE_URL}${path}`, {
      method,
      headers: {
        ...(body === undefined ? {} : { 'Content-Type': 'application/json' }),
        ...headers,
      },
      ...(body === undefined ? {} : { body: JSON.stringify(body) }),
    })
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
  return request('/users/register', { body: { name, password } })
}

export function loginUser(name: string, password: string): Promise<number> {
  return request('/auth/login', { body: { name, password } })
}

export function verifySession(sessionId: number): Promise<AuthUser> {
  return request('/auth/me', {
    method: 'GET',
    headers: { 'Session-Id': String(sessionId) },
  })
}

export function logoutUser(sessionId: number): Promise<{ message: string }> {
  return request('/auth/logout', { body: { session_id: sessionId } })
}
