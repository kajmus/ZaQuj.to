import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import Flashcard from './Flashcard'

describe('Flashcard', () => {
  it('pokazuje odpowiedź po kliknięciu karty i wraca do pytania', async () => {
    const user = userEvent.setup()

    render(<Flashcard frontText="Pytanie testowe" backText="Odpowiedź testowa" />)

    expect(screen.getByText('Pytanie testowe')).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Pokaż odpowiedź' }))

    expect(screen.getByText('Odpowiedź testowa')).toBeInTheDocument()
    expect(screen.getByRole('button', { name: 'Pokaż pytanie' })).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Wróć do pytania' }))

    expect(screen.getByText('Pytanie testowe')).toBeInTheDocument()
  })

  it('obraca kartę przyciskiem Sprawdź', async () => {
    const user = userEvent.setup()

    render(<Flashcard frontText="Pytanie testowe" backText="Odpowiedź testowa" />)

    await user.click(screen.getByRole('button', { name: 'Sprawdź' }))

    expect(screen.getByText('Odpowiedź testowa')).toBeInTheDocument()
  })
})