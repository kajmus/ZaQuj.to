import { Link } from 'react-router-dom'

export default function AllQuestionsPage() {
  return (
    <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-900 sm:px-8">
      <div className="mx-auto max-w-3xl">
        <Link
          to="/"
          className="text-sm font-medium text-indigo-700 underline-offset-4 hover:underline"
        >
          Strona główna
        </Link>

        <header className="mb-10 mt-10">
          <p className="text-sm font-semibold uppercase tracking-wide text-indigo-700">
            Cała baza
          </p>
          <h1 className="mt-2 text-3xl font-bold">Wszystkie pytania</h1>
          <p className="mt-3 text-slate-600">Wybierz tryb nauki.</p>
        </header>

        <section aria-label="Tryb nauki" className="grid grid-cols-1 gap-4 sm:grid-cols-2">
          <Link
            to="/flashcards"
            className="flex min-h-40 flex-col items-start justify-between gap-5 rounded-xl border-2 border-teal-700 bg-white p-6 text-left text-teal-700 transition-colors hover:bg-slate-50"
          >
            <span className="flex items-center gap-3">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
                strokeLinejoin="round"
                aria-hidden="true"
                className="h-8 w-8"
              >
                <rect x="3" y="4" width="15" height="16" rx="2" />
                <path d="M7 8h7M7 12h7M7 16h4" />
                <path d="M18 7h3v13a1 1 0 0 1-1 1" />
              </svg>
              <span className="text-xl font-bold">Fiszki</span>
            </span>
            <span className="text-sm text-slate-600">
              Utrwalaj wiedzę z pytań z całej bazy.
            </span>
          </Link>

          <button
            type="button"
            disabled
            aria-disabled="true"
            className="flex min-h-40 cursor-not-allowed flex-col items-start justify-between gap-5 rounded-xl border-2 border-slate-400 bg-white p-6 text-left text-slate-500 opacity-60"
          >
            <span className="flex items-center gap-3">
              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="1.8"
                strokeLinecap="round"
                strokeLinejoin="round"
                aria-hidden="true"
                className="h-8 w-8"
              >
                <circle cx="12" cy="12" r="9" />
                <path d="M9.5 9a2.5 2.5 0 1 1 4.2 1.8c-1.1 1-1.7 1.2-1.7 2.7" />
                <path d="M12 17h.01" />
              </svg>
              <span className="text-xl font-bold">Quizy</span>
            </span>
            <span className="text-sm text-slate-600">
              Sprawdź swoją wiedzę z pytań z całej bazy.
            </span>
          </button>
        </section>
      </div>
    </main>
  )
}