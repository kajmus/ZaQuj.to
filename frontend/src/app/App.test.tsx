
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

  it('przechodzi z ekranu tematu do jego fiszek', async () => {
    const user = userEvent.setup()
    window.history.pushState({}, '', '/topics/12')
    const fetchMock = vi.fn((input: RequestInfo | URL) => {
      const url = String(input)
      if (url === '/api/topics/12') {
        return Promise.resolve(new Response(JSON.stringify({ id: 12, name: 'Układ krążenia' }), {
          status: 200,
          headers: { 'Content-Type': 'application/json' },
        }))
      }
      return Promise.resolve(new Response(JSON.stringify({
        items: [{ id: 44, front_text: 'Pytanie z układu', back_text: 'Odpowiedź' }],
        total: 1,
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      }))
    })
    vi.stubGlobal('fetch', fetchMock)

    render(<App />)

    expect(await screen.findByRole('heading', { name: 'Układ krążenia' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /quizy/i })).toBeDisabled()
    await user.click(screen.getByRole('link', { name: /fiszki/i }))

    expect(await screen.findByText('Pytanie z układu')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenCalledWith('/api/flashcards/topic/12', expect.anything())
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
