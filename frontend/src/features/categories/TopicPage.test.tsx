import { afterEach, describe, expect, it, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import TopicPage from './TopicPage'

afterEach(() => {
  vi.unstubAllGlobals()
})

describe('TopicPage', () => {
  it('pokazuje nazwę tematu, blokuje quizy i otwiera fiszki tego tematu', async () => {
    const user = userEvent.setup()
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({
      id: 12,
      name: 'Układ krążenia',
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    }))
    vi.stubGlobal('fetch', fetchMock)

    render(
      <MemoryRouter initialEntries={['/topics/12']}>
        <Routes>
          <Route path="/topics/:topicId" element={<TopicPage />} />
          <Route path="/flashcards/topic/:topicId" element={<h1>Fiszki tematu</h1>} />
        </Routes>
      </MemoryRouter>,
    )

    expect(await screen.findByRole('heading', { name: 'Układ krążenia' })).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /fiszki/i })).toHaveAttribute(
      'href',
      '/flashcards/topic/12',
    )
    expect(screen.getByRole('button', { name: /quizy/i })).toBeDisabled()
    expect(fetchMock).toHaveBeenCalledWith('/api/topics/12')

    await user.click(screen.getByRole('link', { name: /fiszki/i }))
    expect(screen.getByRole('heading', { name: 'Fiszki tematu' })).toBeInTheDocument()
  })
})