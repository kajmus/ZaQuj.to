
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
  })

  it('wyświetla stronę główną niezalogowanemu użytkownikowi', () => {
    render(<App />)

    expect(
      screen.getByRole('heading', { name: 'Co dziś powtarzamy?' }),
    ).toBeInTheDocument()

    expect(
      screen.getByRole('button', { name: /zaloguj się/i }),
    ).toBeInTheDocument()
  })

  it('umożliwia zalogowanie i przejście do fiszek', async () => {
    const user = userEvent.setup()

    render(<App />)

    // Logujemy użytkownika.
    await user.click(
      screen.getByRole('button', { name: /zaloguj się/i }),
    )

    expect(sessionStorage.getItem('app_session')).toBe('active')

    // Sprawdzamy dostępność funkcji nauki.
    const flashcardsLink = screen.getByRole('link', {
      name: /fiszki/i,
    })

    expect(flashcardsLink).toBeInTheDocument()

    // Przechodzimy do fiszek.
    await user.click(flashcardsLink)

    // Sprawdzamy, czy wyświetliła się strona fiszek.
    expect(
      screen.getByRole('heading', { name: /fiszki/i }),
    ).toBeInTheDocument()
  })

  it('otwiera menu kategorii z kafelka na stronie głównej', async () => {
    const user = userEvent.setup()
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response(JSON.stringify({
      items: [{ id: 1, name: 'Matematyka' }],
      total: 1,
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    })))
    sessionStorage.setItem('app_session', 'active')

    render(<App />)

    await user.click(screen.getByRole('link', { name: /kategorie/i }))

    expect(await screen.findByRole('heading', { name: 'Kategorie' })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Matematyka' })).toHaveAttribute(
      'href',
      '/categories/1/topics',
    )
  })

  it('wyświetla funkcje nauki po odświeżeniu aplikacji z aktywną sesją', () => {
    sessionStorage.setItem('app_session', 'active')

    render(<App />)

    expect(
      screen.getByRole('link', { name: /fiszki/i }),
    ).toBeInTheDocument()

    expect(
      screen.getByRole('button', { name: /quizy/i }),
    ).toBeDisabled()
  })
})
