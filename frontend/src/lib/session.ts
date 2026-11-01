
// Na tę chwilę, podstawowy handler sesji, do rozszerzenia o inne elementy później.
const SESSION_KEY = 'app_session'

/**
 * Sprawdza, czy użytkownik posiada aktywną sesję.
 */
export function isSessionActive(): boolean {
  return sessionStorage.getItem(SESSION_KEY) === 'active'
}

/**
 * Rozpoczyna sesję użytkownika.
 */
export function startSession(): void {
  sessionStorage.setItem(SESSION_KEY, 'active')
}

/**
 * Kończy bieżącą sesję użytkownika.
 */
export function endSession(): void {
  sessionStorage.removeItem(SESSION_KEY)
}
