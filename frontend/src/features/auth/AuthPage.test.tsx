import { beforeEach, describe, expect, it, vi } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import AuthPage from './AuthPage'

function renderAuthPage() {
  return render(
    <MemoryRouter initialEntries={['/login']}>
      <Routes>
        <Route path="/login" element={<AuthPage />} />
        <Route path="/" element={<h1>Strona główna</h1>} />
      </Routes>
    </MemoryRouter>,
  )
}

function jsonResponse(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

describe('AuthPage', () => {
  beforeEach(() => {
    localStorage.clear()
    vi.stubGlobal('fetch', vi.fn())
  })

  it('rejestruje konto, następnie loguje i zapisuje zwróconą sesję', async () => {
    const user = userEvent.setup()
    const fetchMock = vi.mocked(fetch)
    fetchMock
      .mockResolvedValueOnce(jsonResponse({ id_user: 4, login: 'ola' }, 201))
      .mockResolvedValueOnce(jsonResponse(37))
    renderAuthPage()

    await user.click(screen.getByRole('button', { name: 'Załóż konto' }))
    await user.type(screen.getByLabelText('Nazwa użytkownika'), 'ola')
    await user.type(screen.getByLabelText('Hasło'), 'tajne')
    await user.click(screen.getByRole('button', { name: 'Załóż konto' }))

    expect(await screen.findByRole('heading', { name: 'Strona główna' })).toBeInTheDocument()
    expect(fetchMock).toHaveBeenNthCalledWith(1, 'http://localhost:8000/api/users/register', expect.objectContaining({
      method: 'POST', body: JSON.stringify({ name: 'ola', password: 'tajne' }),
    }))
    expect(fetchMock).toHaveBeenNthCalledWith(2, 'http://localhost:8000/api/auth/login', expect.objectContaining({
      method: 'POST', body: JSON.stringify({ name: 'ola', password: 'tajne' }),
    }))
    expect(localStorage.getItem('app_session')).toBe('37')
  })

  it('pokazuje błąd serwera i pozwala poprawić formularz', async () => {
    const user = userEvent.setup()
    vi.mocked(fetch).mockResolvedValueOnce(jsonResponse({ detail: 'Password does not match' }, 401))
    renderAuthPage()

    await user.type(screen.getByLabelText('Nazwa użytkownika'), 'ola')
    await user.type(screen.getByLabelText('Hasło'), 'wrong')
    await user.click(screen.getByRole('button', { name: 'Zaloguj się' }))

    expect(await screen.findByRole('alert')).toHaveTextContent('Password does not match')
    expect(localStorage.getItem('app_session')).toBeNull()
  })

  it('nie próbuje logować, jeśli rejestracja się nie powiedzie', async () => {
    const user = userEvent.setup()
    const fetchMock = vi.mocked(fetch)
    fetchMock.mockResolvedValueOnce(jsonResponse({ detail: 'Conflict: User.name already in the data base' }, 409))
    renderAuthPage()

    await user.click(screen.getByRole('button', { name: 'Załóż konto' }))
    await user.type(screen.getByLabelText('Nazwa użytkownika'), 'ola')
    await user.type(screen.getByLabelText('Hasło'), 'tajne')
    await user.click(screen.getByRole('button', { name: 'Załóż konto' }))

    expect(await screen.findByRole('alert')).toHaveTextContent('Conflict: User.name already in the data base')
    expect(fetchMock).toHaveBeenCalledTimes(1)
    expect(localStorage.getItem('app_session')).toBeNull()
  })

  it('blokuje wielokrotne wysłanie formularza podczas żądania', async () => {
    const user = userEvent.setup()
    let resolveLogin!: (response: Response) => void
    vi.mocked(fetch).mockImplementation(() => new Promise((resolve) => { resolveLogin = resolve }))
    renderAuthPage()
    await user.type(screen.getByLabelText('Nazwa użytkownika'), 'ola')
    await user.type(screen.getByLabelText('Hasło'), 'tajne')
    await user.click(screen.getByRole('button', { name: 'Zaloguj się' }))
    expect(screen.getByRole('button', { name: 'Proszę czekać…' })).toBeDisabled()
    resolveLogin(jsonResponse(12))
    await waitFor(() => expect(localStorage.getItem('app_session')).toBe('12'))
  })
})
