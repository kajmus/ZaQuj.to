
import { useState } from 'react'
import { useCounter } from './CounterContext'
import { getCookie, setCookie } from '../../lib/cookies'

const COOKIE_NAME = 'state_demo_note'

export default function StateDemo() {
  const { count, increment, reset } = useCounter()
  const [cookieValue, setCookieValue] = useState(
    () => getCookie(COOKIE_NAME) ?? '',
  )
  const [cookieInput, setCookieInput] = useState('')

  function saveCookie() {
    setCookie(COOKIE_NAME, cookieInput)
    setCookieValue(cookieInput)
    setCookieInput('')
  }

  function deleteCookie() {
    setCookie(COOKIE_NAME, '')
    setCookieValue('')
  }

  return (
    <section className="mt-8 space-y-6 rounded-xl border p-6">
      <h2 className="text-xl font-bold">Test zarządzania stanem</h2>

      <div className="space-y-2">
        <h3 className="font-semibold">React Context</h3>
        <p>Licznik współdzielony: {count}</p>

        <div className="flex flex-wrap gap-2">
          <button
            type="button"
            onClick={increment}
            className="rounded bg-blue-600 px-3 py-2 text-white"
          >
            Zwiększ
          </button>

          <button
            type="button"
            onClick={reset}
            className="rounded border px-3 py-2"
          >
            Wyzeruj
          </button>
        </div>
      </div>

      <div className="space-y-2">
        <h3 className="font-semibold">Cookie</h3>
        <p>
          Wartość zapisana w cookie:{' '}
          <strong>{cookieValue || '(brak wartości)'}</strong>
        </p>

        <form
          onSubmit={(event) => {
            event.preventDefault()
            saveCookie()
          }}
          className="flex flex-wrap gap-2"
        >
          <input
            type="text"
            value={cookieInput}
            onChange={(event) => setCookieInput(event.target.value)}
            placeholder="Wpisz testową wartość"
            aria-label="Wartość cookie"
            className="min-w-0 rounded border px-3 py-2"
          />

          <button
            type="submit"
            className="rounded bg-blue-600 px-3 py-2 text-white"
          >
            Zapisz cookie
          </button>
        </form>

        <button
          type="button"
          onClick={deleteCookie}
          className="rounded border px-3 py-2"
        >
          Usuń cookie
        </button>
      </div>
    </section>
  )
}
