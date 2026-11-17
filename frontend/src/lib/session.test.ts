
import { describe, it, expect, beforeEach } from 'vitest'

import {
  isSessionActive,
  getSessionId,
  startSession,
  endSession,
} from './session'

describe('session', () => {
  beforeEach(() => {
    localStorage.clear()
  })

  it('zwraca false, gdy sesja nie jest aktywna', () => {
    expect(isSessionActive()).toBe(false)
  })

  it('rozpoczyna sesję użytkownika', () => {
    startSession(42)

    expect(isSessionActive()).toBe(true)
    expect(localStorage.getItem('app_session')).toBe('42')
    expect(getSessionId()).toBe(42)
  })

  it('kończy aktywną sesję użytkownika', () => {
    startSession(42)

    endSession()

    expect(isSessionActive()).toBe(false)
    expect(localStorage.getItem('app_session')).toBeNull()
  })

  it('nie zgłasza błędu przy kończeniu nieaktywnej sesji', () => {
    expect(() => endSession()).not.toThrow()
    expect(isSessionActive()).toBe(false)
  })
})
