import { useState } from 'react'
import type { FormEvent } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { startSession } from '../../lib/session'
import { loginUser, registerUser } from './auth-api'

export default function AuthPage() {
  const [isRegistering, setIsRegistering] = useState(false)
  const [name, setName] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const navigate = useNavigate()

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setError('')
    setIsSubmitting(true)
    try {
      if (isRegistering) await registerUser(name, password)
      const sessionId = await loginUser(name, password)
      if (!Number.isInteger(sessionId) || sessionId <= 0) {
        throw new Error('Serwer zwrócił nieprawidłową sesję.')
      }
      startSession(sessionId)
      navigate('/')
    } catch (submitError) {
      setError(submitError instanceof Error ? submitError.message : 'Wystąpił błąd. Spróbuj ponownie.')
    } finally {
      setIsSubmitting(false)
    }
  }

  function switchMode() {
    setIsRegistering((current) => !current)
    setError('')
  }

  return (
    <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-900 sm:px-8">
      <div className="mx-auto max-w-3xl">
        <header className="mb-10">
          <p className="text-sm font-semibold uppercase tracking-widest text-indigo-700">
            <Link to="/">ZaQuj.to</Link>
          </p>
          <h1 className="mt-2 text-3xl font-bold">Zaloguj się/Załóż konto</h1>
          <p className="mt-3 text-slate-600">Zaloguj się lub załóż konto, aby uzyskać dostęp do narzędzi nauki.</p>
        </header>

        <section className="w-full rounded-2xl border-2 border-indigo-600 bg-white p-6">
          <div className="mb-6 flex items-center gap-3 text-indigo-700">
            <span className="[&_svg]:h-8 [&_svg]:w-8">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4" />
                <path d="M10 17l5-5-5-5" />
                <path d="M15 12H3" />
              </svg>
            </span>
            <h2 className="text-xl font-bold">{isRegistering ? 'Załóż konto' : 'Zaloguj się'}</h2>
          </div>

        <form className="space-y-5" onSubmit={handleSubmit}>
          <div>
            <label htmlFor="auth-name" className="mb-1.5 block text-sm font-medium">Nazwa użytkownika</label>
            <input id="auth-name" name="name" autoComplete="username" required value={name} onChange={(event) => setName(event.target.value)} className="w-full rounded-lg border border-slate-300 px-3 py-2.5 outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100" />
          </div>
          <div>
            <label htmlFor="auth-password" className="mb-1.5 block text-sm font-medium">Hasło</label>
            <input id="auth-password" name="password" type="password" autoComplete={isRegistering ? 'new-password' : 'current-password'} required value={password} onChange={(event) => setPassword(event.target.value)} className="w-full rounded-lg border border-slate-300 px-3 py-2.5 outline-none focus:border-indigo-600 focus:ring-2 focus:ring-indigo-100" />
          </div>
          {error && <p role="alert" className="text-sm text-red-700">{error}</p>}
          <button type="submit" disabled={isSubmitting} className="w-full rounded-lg bg-indigo-700 px-4 py-3 font-semibold text-white hover:bg-indigo-800 disabled:cursor-wait disabled:opacity-60">
            {isSubmitting ? 'Proszę czekać…' : isRegistering ? 'Załóż konto' : 'Zaloguj się'}
          </button>
        </form>

        <p className="mt-6 text-sm text-slate-600">
          {isRegistering ? 'Masz już konto?' : 'Nie masz jeszcze konta?'}{' '}
          <button type="button" onClick={switchMode} className="font-semibold text-indigo-700 underline underline-offset-2">
            {isRegistering ? 'Zaloguj się' : 'Załóż konto'}
          </button>
        </p>
        </section>
      </div>
    </main>
  )
}
