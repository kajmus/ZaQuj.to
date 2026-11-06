
import { describe, it, expect, beforeEach } from 'vitest'

import {
  isSessionActive,
  startSession,
  endSession,
} from './session'

describe('session', () => {
  beforeEach(() => {
    sessionStorage.clear()
  })

  it('zwraca false, gdy sesja nie jest aktywna', () => {
    expect(isSessionActive()).toBe(false)
  })

  it('rozpoczyna sesję użytkownika', () => {
    startSession()

    expect(isSessionActive()).toBe(true)
    expect(sessionStorage.getItem('app_session')).toBe('active')
  })

  it('kończy aktywną sesję użytkownika', () => {
    startSession()

    endSession()

    expect(isSessionActive()).toBe(false)
    expect(sessionStorage.getItem('app_session')).toBeNull()
  })

  it('nie zgłasza błędu przy kończeniu nieaktywnej sesji', () => {
    expect(() => endSession()).not.toThrow()
    expect(isSessionActive()).toBe(false)
  })
})
