import { afterEach, describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
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
      '/api/flashcards/',
      expect.objectContaining({ signal: expect.any(AbortSignal) }),
    )
  })

  it('pobiera i wyświetla fiszki tylko dla tematu z trasy', async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        items: [{ id: 12, front_text: 'Pytanie z tematu', back_text: 'Odpowiedź z tematu' }],
        total: 1,
      }),
    })
    vi.stubGlobal('fetch', fetchMock)

    render(
      <MemoryRouter initialEntries={['/flashcards/topic/12']}>
        <Routes>
          <Route path="/flashcards/topic/:topicId" element={<FlashcardsPage />} />
        </Routes>
      </MemoryRouter>,
    )

    expect(await screen.findByText('Pytanie z tematu')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/flashcards/topic/12',
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

  it('buduje endpoint dla numerycznego ID tematu', async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ items: [], total: 0 }),
    })
    vi.stubGlobal('fetch', fetchMock)

    await fetchFlashcards(12)

    expect(fetchMock).toHaveBeenCalledWith(
      '/api/flashcards/topic/12',
      expect.objectContaining({ signal: undefined }),
    )
  })

  it('łączy fiszki ze wszystkich tematów wybranej kategorii', async () => {
    const fetchMock = vi.fn((input: RequestInfo | URL) => {
      const url = String(input)
      if (url === '/api/topics/category/3') {
        return Promise.resolve({
          ok: true,
          json: async () => ({
            items: [{ id: 12, name: 'Komórka' }, { id: 13, name: 'Tkanki' }],
            total: 2,
          }),
        })
      }
      if (url === '/api/flashcards/topic/12') {
        return Promise.resolve({
          ok: true,
          json: async () => ({
            items: [{ id: 101, front_text: 'Pytanie komórkowe', back_text: 'Odpowiedź komórkowa' }],
            total: 1,
          }),
        })
      }
      if (url === '/api/flashcards/topic/13') {
        return Promise.resolve({
          ok: true,
          json: async () => ({
            items: [{ id: 102, front_text: 'Pytanie tkankowe', back_text: 'Odpowiedź tkankowa' }],
            total: 1,
          }),
        })
      }
      return Promise.reject(new Error(`Nieoczekiwany URL: ${url}`))
    })
    vi.stubGlobal('fetch', fetchMock)

    render(
      <MemoryRouter initialEntries={['/flashcards/category/3']}>
        <Routes>
          <Route path="/flashcards/category/:categoryId" element={<FlashcardsPage />} />
        </Routes>
      </MemoryRouter>,
    )

    expect(await screen.findByText('Pytanie komórkowe')).toBeInTheDocument()
    expect(fetchMock).toHaveBeenCalledWith('/api/topics/category/3')
    expect(fetchMock).toHaveBeenCalledWith('/api/flashcards/topic/12', expect.anything())
    expect(fetchMock).toHaveBeenCalledWith('/api/flashcards/topic/13', expect.anything())
  })
})