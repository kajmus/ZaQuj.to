const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api'

export interface AuthUser {
  id_user: number
  login: string
}

async function request<T>(path: string, body: unknown): Promise<T> {
  let response: Response
  try {
    response = await fetch(`${API_BASE_URL}${path}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
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
  return request('/users/register', { name, password })
}

export function loginUser(name: string, password: string): Promise<number> {
  return request('/auth/login', { name, password })
}

export function verifySession(sessionId: number): Promise<AuthUser> {
  return request('/auth/me', { session_id: sessionId })
}

export function logoutUser(sessionId: number): Promise<{ message: string }> {
  return request('/auth/logout', { session_id: sessionId })
}
