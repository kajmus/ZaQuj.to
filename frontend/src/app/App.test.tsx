
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
