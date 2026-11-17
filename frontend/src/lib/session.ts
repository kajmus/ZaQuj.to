
const SESSION_KEY = 'app_session'

/**
 * Sprawdza, czy użytkownik posiada aktywną sesję.
 */
export function isSessionActive(): boolean {
  return getSessionId() !== null
}

export function getSessionId(): number | null {
  const value = localStorage.getItem(SESSION_KEY)
  if (value === null) return null
  const sessionId = Number(value)
  return Number.isInteger(sessionId) && sessionId > 0 ? sessionId : null
}

export function startSession(sessionId: number): void {
  localStorage.setItem(SESSION_KEY, String(sessionId))
}

/**
 * Kończy bieżącą sesję użytkownika.
 */
export function endSession(): void {
  localStorage.removeItem(SESSION_KEY)
}
