
import { describe, it, expect, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter, Routes, Route } from 'react-router-dom'

import HomePage from './HomePage'
import { isSessionActive, startSession, endSession } from '../../lib/session'

function renderHomePage() {
  return render(
    <MemoryRouter initialEntries={['/']}>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route
          path="/categories"
          element={<h1>Menu kategorii</h1>}
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

  it('wyświetla przycisk logowania, gdy użytkownik nie jest zalogowany', () => {
    renderHomePage()

    expect(
      screen.getByRole('link', { name: /zaloguj się/i })
    ).toBeInTheDocument()
    
    expect(
      screen.getByRole('link', { name: /kategorie/i })
    ).not.toBeInTheDocument()
    
    expect(
      screen.queryByRole('link', { name: /fiszki/i })
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

  it('wyświetla funkcje nauki, gdy użytkownik ma aktywną sesję', () => {
    startSession(1)

    renderHomePage()
          
    expect(
      screen.getByRole('link', { name: /kategorie/i })
    ).toBeInTheDocument()

    expect(
      screen.getByRole('link', { name: /fiszki/i })
    ).toBeInTheDocument()

    expect(
      screen.getByRole('button', { name: /quizy/i })
    ).toBeInTheDocument()

    expect(
      screen.queryByRole('button', { name: /zaloguj się/i })
    ).not.toBeInTheDocument()
  })

  it('przenosi użytkownika na stronę fiszek po kliknięciu kafelka', async () => {
    const user = userEvent.setup()

    startSession(1)
    renderHomePage()

    await user.click(
      screen.getByRole('link', { name: /fiszki/i })
    )

    expect(
      screen.getByRole('heading', { name: 'Strona fiszek' })
    ).toBeInTheDocument()
  })

  it('pokazuje Kategorie przed Fiszkami i otwiera menu kategorii', async () => {
    const user = userEvent.setup()

    startSession(1)
    renderHomePage()

    const learningLinks = screen.getAllByRole('link')
    const categoriesLink = screen.getByRole('link', { name: /kategorie/i })
    const flashcardsLink = screen.getByRole('link', { name: /fiszki/i })
    expect(learningLinks.indexOf(categoriesLink)).toBeLessThan(
      learningLinks.indexOf(flashcardsLink),
    )

    await user.click(categoriesLink)

    expect(
      screen.getByRole('heading', { name: 'Menu kategorii' }),
    ).toBeInTheDocument()
  })

  it('nie pozwala przejść do quizów, ponieważ kafelek jest wyłączony', async () => {
    const user = userEvent.setup()

    startSession(1)
    renderHomePage()

    const quizButton = screen.getByRole('button', {
      name: /quizy/i,
    })

    expect(quizButton).toBeDisabled()

    await user.click(quizButton)

    expect(
      screen.queryByRole('heading', { name: 'Strona fiszek' })
    ).not.toBeInTheDocument()
  })
})
