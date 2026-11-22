import { afterEach, describe, it, expect, beforeEach, vi } from 'vitest'
import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter, Routes, Route } from 'react-router-dom'

import HomePage from './HomePage'
import AllQuestionsPage from './AllQuestionsPage'
import { isSessionActive, startSession, endSession } from '../../lib/session'

function jsonResponse(data: unknown) {
  return new Response(JSON.stringify(data), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  })
}

function renderHomePage() {
  return render(
    <MemoryRouter initialEntries={['/']}>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/all" element={<AllQuestionsPage />} />
        <Route
          path="/categories/:categoryId/topics"
          element={<h1>Tematy kategorii</h1>}
        />
        <Route
          path="/flashcards"
          element={<h1>Strona fiszek</h1>}
        />
        <Route path="/login" element={<h1>Strona logowania</h1>} />
      </Routes>
    </MemoryRouter>
  )
}

describe('HomePage', () => {
  beforeEach(() => {
    endSession()
    sessionStorage.clear()
  })

  afterEach(() => {
    vi.unstubAllGlobals()
  })

  it('wyświetla przycisk logowania, gdy użytkownik nie jest zalogowany', () => {
    renderHomePage()

    expect(
      screen.getByRole('link', { name: /zaloguj się/i })
    ).toBeInTheDocument()
    
    expect(
      screen.queryByRole('link', { name: /wszystkie/i })
    ).not.toBeInTheDocument()

    expect(
      screen.queryByRole('button', { name: /quizy/i })
    ).not.toBeInTheDocument()
  })

  it('przenosi niezalogowanego użytkownika do logowania', async () => {
    const user = userEvent.setup()

    renderHomePage()

    await user.click(screen.getByRole('link', { name: /zaloguj się/i }))
    expect(screen.getByRole('heading', { name: 'Strona logowania' })).toBeInTheDocument()
    expect(isSessionActive()).toBe(false)

  })

  it('wyświetla nowe akcje i listę kategorii dla aktywnej sesji', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(jsonResponse({
      items: [{ id: 3, name: 'Biologia' }],
      total: 1,
    })))
    startSession(1)

    renderHomePage()

    expect(
      screen.getByRole('link', { name: /^Wszystkie/ })
    ).toHaveAttribute('href', '/all')

    expect(
      screen.getByRole('button', { name: /powtórka/i })
    ).toBeDisabled()

    expect(
      screen.getByRole('button', { name: /mój profil/i })
    ).toBeDisabled()

    expect(await screen.findByRole('link', { name: 'Biologia' })).toHaveAttribute(
      'href',
      '/categories/3/topics',
    )
    expect(
      within(screen.getByRole('navigation', { name: 'Kategorie' })).getByRole('link', {
        name: 'Wszystkie',
      }),
    ).toHaveAttribute('href', '/all')

    expect(
      screen.queryByRole('button', { name: /zaloguj się/i })
    ).not.toBeInTheDocument()
  })

  it('przenosi użytkownika do wyboru trybu dla wszystkich pytań', async () => {
    const user = userEvent.setup()
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(jsonResponse({ items: [], total: 0 })))

    startSession(1)
    renderHomePage()

    await user.click(
      screen.getByRole('link', { name: /^Wszystkie/ })
    )

    expect(
      screen.getByRole('heading', { name: 'Wszystkie pytania' })
    ).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /fiszki/i })).toHaveAttribute(
      'href',
      '/flashcards',
    )
    expect(screen.getByRole('button', { name: /quizy/i })).toBeDisabled()
  })

  it('otwiera tematy po wybraniu kategorii z homepage', async () => {
    const user = userEvent.setup()
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(jsonResponse({
      items: [{ id: 3, name: 'Biologia' }],
      total: 1,
    })))

    startSession(1)
    renderHomePage()

    await user.click(await screen.findByRole('link', { name: 'Biologia' }))

    expect(
      screen.getByRole('heading', { name: 'Tematy kategorii' }),
    ).toBeInTheDocument()
  })

  it('nie pozwala rozpocząć powtórki, ponieważ akcja jest wyłączona', async () => {
    const user = userEvent.setup()
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(jsonResponse({ items: [], total: 0 })))

    startSession(1)
    renderHomePage()

    const reviewButton = screen.getByRole('button', {
      name: /powtórka/i,
    })

    expect(reviewButton).toBeDisabled()

    await user.click(reviewButton)

    expect(
      screen.queryByRole('heading', { name: 'Wszystkie pytania' })
    ).not.toBeInTheDocument()
  })
})
