
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
          path="/flashcards"
          element={<h1>Strona fiszek</h1>}
        />
      </Routes>
    </MemoryRouter>
  )
}

describe('HomePage', () => {
  beforeEach(() => {
    endSession()
  })

  it('wyświetla przycisk logowania, gdy użytkownik nie jest zalogowany', () => {
    renderHomePage()

    expect(
      screen.getByRole('button', { name: /zaloguj się/i })
    ).toBeInTheDocument()

    expect(
      screen.queryByRole('link', { name: /fiszki/i })
    ).not.toBeInTheDocument()

    expect(
      screen.queryByRole('button', { name: /quizy/i })
    ).not.toBeInTheDocument()
  })

  it('loguje użytkownika po kliknięciu przycisku logowania', async () => {
    const user = userEvent.setup()

    renderHomePage()

    await user.click(
      screen.getByRole('button', { name: /zaloguj się/i })
    )

    expect(isSessionActive()).toBe(true)

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

  it('wyświetla funkcje nauki, gdy użytkownik ma aktywną sesję', () => {
    startSession()

    renderHomePage()

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

    startSession()
    renderHomePage()

    await user.click(
      screen.getByRole('link', { name: /fiszki/i })
    )

    expect(
      screen.getByRole('heading', { name: 'Strona fiszek' })
    ).toBeInTheDocument()
  })

  it('nie pozwala przejść do quizów, ponieważ kafelek jest wyłączony', async () => {
    const user = userEvent.setup()

    startSession()
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
