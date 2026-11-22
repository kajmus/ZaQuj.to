import { afterEach, describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import CategoryAllPage from './CategoryAllPage'

afterEach(() => vi.unstubAllGlobals())

describe('CategoryAllPage', () => {
  it('pokazuje nazwę kategorii i prowadzi do jej wszystkich fiszek', async () => {
    const user = userEvent.setup()
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response(JSON.stringify({
      id: 3,
      name: 'Biologia',
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    })))

    render(
      <MemoryRouter initialEntries={['/categories/3/all']}>
        <Routes>
          <Route path="/categories/:categoryId/all" element={<CategoryAllPage />} />
          <Route path="/flashcards/category/:categoryId" element={<h1>Fiszki kategorii</h1>} />
        </Routes>
      </MemoryRouter>,
    )

    expect(await screen.findByRole('heading', { name: 'Biologia' })).toBeInTheDocument()
    expect(screen.getByRole('button', { name: /quizy/i })).toBeDisabled()
    expect(screen.getByRole('link', { name: /fiszki/i })).toHaveAttribute(
      'href',
      '/flashcards/category/3',
    )

    await user.click(screen.getByRole('link', { name: /fiszki/i }))
    expect(screen.getByRole('heading', { name: 'Fiszki kategorii' })).toBeInTheDocument()
  })
})
