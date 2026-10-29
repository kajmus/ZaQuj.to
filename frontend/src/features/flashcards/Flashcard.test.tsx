import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import Flashcard from './Flashcard'
import { fitTextToContainer } from './fit-text'

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

  it('zmniejsza tekst, gdy przekracza dostępny obszar', () => {
    const text = document.createElement('span')
    const container = document.createElement('div')

    Object.defineProperties(container, {
      clientWidth: { value: 200 },
      clientHeight: { value: 200 },
    })
    Object.defineProperties(text, {
      scrollWidth: {
        get: () => Number.parseFloat(text.style.fontSize) * 10,
      },
      scrollHeight: {
        get: () => Number.parseFloat(text.style.fontSize) * 10,
      },
    })

    fitTextToContainer(text, container)

    expect(Number.parseFloat(text.style.fontSize)).toBeLessThan(24)
    expect(Number.parseFloat(text.style.fontSize)).toBeGreaterThanOrEqual(12)
  })
})