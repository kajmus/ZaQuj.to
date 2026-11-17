
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from './App'

describe('Aplikacja i nawigacja', () => {
  afterEach(() => {
    vi.unstubAllGlobals()
  })

  beforeEach(() => {
    window.history.pushState({}, '', '/')
    sessionStorage.clear()
    localStorage.clear()
  })

  it('wyświetla stronę główną niezalogowanemu użytkownikowi', () => {
    render(<App />)

    expect(
      screen.getByRole('heading', { name: 'Co dziś powtarzamy?' }),
    ).toBeInTheDocument()

    expect(screen.getByRole('link', { name: /zaloguj się/i })).toHaveAttribute('href', '/login')
  })

  it('przenosi do ekranu logowania', async () => {
    const user = userEvent.setup()

    render(<App />)

    await user.click(screen.getByRole('link', { name: /zaloguj się/i }))
    expect(screen.getByRole('heading', { name: 'Zaloguj się' })).toBeInTheDocument()
    expect(localStorage.getItem('app_session')).toBeNull()
  })

  it('wyświetla funkcje nauki po odświeżeniu aplikacji z aktywną sesją', () => {
    localStorage.setItem('app_session', '23')

    render(<App />)

    expect(
      screen.getByRole('link', { name: /fiszki/i }),
    ).toBeInTheDocument()

    expect(
      screen.getByRole('button', { name: /quizy/i }),
    ).toBeDisabled()
  })
})
