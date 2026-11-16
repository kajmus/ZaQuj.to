import { afterEach, describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import CategoriesPage from './CategoriesPage'
import TopicsPage from './TopicsPage'

function jsonResponse(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

function renderAt(path: string) {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <Routes>
        <Route path="/categories" element={<CategoriesPage />} />
        <Route path="/categories/:categoryId/topics" element={<TopicsPage />} />
      </Routes>
    </MemoryRouter>,
  )
}

afterEach(() => {
  vi.unstubAllGlobals()
})

describe('menu kategorii i tematów', () => {
  it('pobiera kategorie i umieszcza „Wszystkie” na końcu menu', async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse({
      items: [{ id: 3, name: 'Biologia' }, { id: 8, name: 'Historia' }],
      total: 2,
    }))
    vi.stubGlobal('fetch', fetchMock)

    renderAt('/categories')

    const allCategoriesLink = await screen.findByRole('link', { name: 'Wszystkie' })
    expect(screen.getByRole('link', { name: 'Biologia' })).toHaveAttribute(
      'href',
      '/categories/3/topics',
    )
    expect(screen.getByRole('link', { name: 'Historia' })).toHaveAttribute(
      'href',
      '/categories/8/topics',
    )
    expect(allCategoriesLink).toHaveAttribute('href', '/categories/all/topics')
    expect(fetchMock).toHaveBeenCalledWith('/api/categories/')
  })

  it('pobiera tematy, linkuje wybrane tematy i pozostawia „Wszystkie” nieaktywne', async () => {
    const fetchMock = vi.fn((input: RequestInfo | URL) => {
      const url = String(input)
      if (url.endsWith('/topics/category/3')) {
        return Promise.resolve(jsonResponse({
          items: [{ id: 12, name: 'Komórka' }],
          total: 1,
        }))
      }
      return Promise.resolve(jsonResponse({ id: 3, name: 'Biologia' }))
    })
    vi.stubGlobal('fetch', fetchMock)

    renderAt('/categories/3/topics')

    expect(await screen.findByRole('heading', { name: 'Biologia' })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Komórka' })).toHaveAttribute(
      'href',
      '/topics/12',
    )
    expect(screen.getByRole('button', { name: 'Wszystkie' })).toBeDisabled()
    expect(fetchMock).toHaveBeenCalledWith('/api/topics/category/3')
    expect(fetchMock).toHaveBeenCalledWith('/api/categories/3')
  })

  it('pobiera wszystkie tematy dla kategorii „Wszystkie”', async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse({
      items: [{ id: 21, name: 'Algebra' }],
      total: 1,
    }))
    vi.stubGlobal('fetch', fetchMock)

    renderAt('/categories/all/topics')

    expect(await screen.findByRole('heading', { name: 'Wszystkie' })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: 'Algebra' })).toHaveAttribute(
      'href',
      '/topics/21',
    )
    expect(screen.getByRole('button', { name: 'Wszystkie' })).toBeDisabled()
    expect(fetchMock).toHaveBeenCalledOnce()
    expect(fetchMock).toHaveBeenCalledWith('/api/topics/')
  })

  it('pokazuje błąd pobierania kategorii', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(jsonResponse({}, 500)))

    renderAt('/categories')

    expect(await screen.findByRole('alert')).toHaveTextContent(
      'Nie udało się pobrać kategorii.',
    )
  })
})