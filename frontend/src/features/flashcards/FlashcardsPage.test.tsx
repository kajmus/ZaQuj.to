import { afterEach, describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'
import FlashcardsPage from './FlashcardsPage'
import { fetchFlashcards } from './flashcards-api'

const cards = [
  { id: 'one', frontText: 'Pierwsze pytanie', backText: 'Pierwsza odpowiedź' },
  { id: 'two', frontText: 'Drugie pytanie', backText: 'Druga odpowiedź' },
]

afterEach(() => {
  vi.unstubAllGlobals()
})

describe('FlashcardsPage', () => {
  it('przechodzi między kartami i pokazuje nową kartę od strony pytania', async () => {
    const user = userEvent.setup()

    render(
      <MemoryRouter>
        <FlashcardsPage cards={cards} />
      </MemoryRouter>,
    )

    expect(screen.getByRole('link', { name: 'Strona główna' })).toBeInTheDocument()
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

  it('zlicza i zastępuje ocenę karty, a po ostatniej pokazuje podsumowanie', async () => {
    const user = userEvent.setup()

    render(
      <MemoryRouter>
        <FlashcardsPage cards={cards} />
      </MemoryRouter>,
    )

    expect(screen.getByText('Poprawne: 0')).toBeInTheDocument()
    expect(screen.getByText('Niepoprawne: 0')).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Sprawdź' }))
    await user.click(screen.getByRole('button', { name: 'Źle' }))

    expect(screen.getByText('Drugie pytanie')).toBeInTheDocument()
    expect(screen.getByText('Niepoprawne: 1')).toBeInTheDocument()
    expect(screen.getByText('Poprawne: 0')).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Poprzednia' }))
    await user.click(screen.getByRole('button', { name: 'Sprawdź' }))
    await user.click(screen.getByRole('button', { name: 'Dobrze' }))

    expect(screen.getByText('Drugie pytanie')).toBeInTheDocument()
    expect(screen.getByText('Poprawne: 1')).toBeInTheDocument()
    expect(screen.getByText('Niepoprawne: 0')).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: 'Sprawdź' }))
    await user.click(screen.getByRole('button', { name: 'Źle' }))

    expect(screen.queryByRole('heading', { name: 'Koniec fiszek' })).not.toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Powrót do strony głównej' })).toHaveAttribute('href', '/')
    expect(screen.getByText('Poprawne: 1')).toBeInTheDocument()
    expect(screen.getByText('Niepoprawne: 1')).toBeInTheDocument()
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

  it('pobiera wszystkie fiszki z API i mapuje odpowiedź na karty', async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        items: [{ id: 42, front_text: 'Pytanie z API', back_text: 'Odpowiedź z API' }],
        total: 1,
      }),
    })
    vi.stubGlobal('fetch', fetchMock)

    render(
      <MemoryRouter>
        <FlashcardsPage />
      </MemoryRouter>,
    )

    expect(screen.getByRole('status')).toHaveTextContent('Ładowanie fiszek...')
    expect(await screen.findByText('Pytanie z API')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenCalledWith(
      'http://127.0.0.1:8000/api/flashcards/',
      expect.objectContaining({ signal: expect.any(AbortSignal) }),
    )
  })

  it('pokazuje pusty stan dla pustej odpowiedzi z API', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ items: [], total: 0 }),
    }))

    render(
      <MemoryRouter>
        <FlashcardsPage />
      </MemoryRouter>,
    )

    expect(await screen.findByText('Ten zestaw nie zawiera jeszcze żadnych fiszek.')).toBeInTheDocument()
  })

  it('po błędzie pobierania pozwala ponowić próbę', async () => {
    const user = userEvent.setup()
    const fetchMock = vi.fn()
      .mockRejectedValueOnce(new Error('Network error'))
      .mockResolvedValueOnce({
        ok: true,
        json: async () => ({
          items: [{ id: 7, front_text: 'Pytanie po ponowieniu', back_text: 'Odpowiedź' }],
          total: 1,
        }),
      })
    vi.stubGlobal('fetch', fetchMock)

    render(
      <MemoryRouter>
        <FlashcardsPage />
      </MemoryRouter>,
    )

    expect(await screen.findByRole('alert')).toHaveTextContent('Nie udało się pobrać fiszek.')
    await user.click(screen.getByRole('button', { name: 'Spróbuj ponownie' }))

    expect(await screen.findByText('Pytanie po ponowieniu')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenCalledTimes(2)
  })

  it('wybiera trasę tematu dla przyszłego filtrowania', async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ items: [], total: 0 }),
    })
    vi.stubGlobal('fetch', fetchMock)

    await fetchFlashcards('topic 12')

    expect(fetchMock).toHaveBeenCalledWith(
      'http://127.0.0.1:8000/api/flashcards/topic/topic%2012',
      expect.objectContaining({ signal: undefined }),
    )
  })
})