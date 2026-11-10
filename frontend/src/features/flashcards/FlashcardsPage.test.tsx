import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import FlashcardsPage from './FlashcardsPage'

const cards = [
  { id: 'one', frontText: 'Pierwsze pytanie', backText: 'Pierwsza odpowiedź' },
  { id: 'two', frontText: 'Drugie pytanie', backText: 'Druga odpowiedź' },
]

describe('FlashcardsPage', () => {
  it('przechodzi między kartami i pokazuje nową kartę od strony pytania', async () => {
    const user = userEvent.setup()

    render(
      <MemoryRouter>
        <FlashcardsPage cards={cards} />
      </MemoryRouter>,
    )

    expect(screen.getByText('Pierwsze pytanie')).toBeInTheDocument()
    expect(screen.getByText('Karta 1 z 2')).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Sprawdź' }))
    expect(screen.getByText('Pierwsza odpowiedź')).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Następna' }))
    expect(screen.getByText('Drugie pytanie')).toBeInTheDocument()
    expect(screen.getByText('Karta 2 z 2')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Sprawdź' })).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Poprzednia' }))
    expect(screen.getByText('Pierwsze pytanie')).toBeInTheDocument()
  })

  it('pokazuje komunikat, gdy zestaw jest pusty', () => {
    render(
      <MemoryRouter>
        <FlashcardsPage cards={[]} />
      </MemoryRouter>,
    )

    expect(screen.getByText('Ten zestaw nie zawiera jeszcze żadnych fiszek.')).toBeInTheDocument()
    expect(screen.queryByRole('button', { name: 'Następna' })).not.toBeInTheDocument()
  })
})