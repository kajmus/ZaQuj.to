// PRZYKŁADOWY TEST
// Zmień mnie, gdy przestanę być przydatny jako demo!

import { beforeEach, describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from './App'

describe('Aplikacja i współdzielony stan', () => {
  beforeEach(() => {
    window.history.pushState({}, '', '/')
  })

  it('zachowuje licznik podczas nawigacji między stronami', async () => {
    const user = userEvent.setup()

    render(<App />)

    // Zwiększamy licznik na stronie głównej.
    await user.click(
      screen.getByRole('button', { name: 'Zwiększ' }),
    )

    expect(
      screen.getByText(/Licznik współdzielony: 1/),
    ).toBeInTheDocument()

    // Przechodzimy na drugą stronę bez przeładowania aplikacji.
    await user.click(
      screen.getByRole('link', { name: 'Do dummy' }),
    )

    expect(
      screen.getByRole('heading', { name: 'Strona dodatkowa' }),
    ).toBeInTheDocument()

    // Licznik powinien nadal mieć wartość 1.
    expect(
      screen.getByText(/Licznik współdzielony: 1/),
    ).toBeInTheDocument()
  })
})
