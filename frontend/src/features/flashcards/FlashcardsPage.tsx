import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import Flashcard, { type FlashcardData } from './Flashcard'
import { fetchFlashcards } from './flashcards-api'

interface FlashcardsPageProps {
  cards?: FlashcardData[]
}

type FlashcardRating = 'incorrect' | 'correct'

export default function FlashcardsPage({ cards }: FlashcardsPageProps) {
  const [loadedCards, setLoadedCards] = useState<FlashcardData[]>([])
  const [loadState, setLoadState] = useState<'loading' | 'error' | 'success'>(
    cards === undefined ? 'loading' : 'success',
  )
  const [retryCount, setRetryCount] = useState(0)
  const [currentIndex, setCurrentIndex] = useState(0)
  const [ratings, setRatings] = useState<Record<string, FlashcardRating>>({})
  const [isComplete, setIsComplete] = useState(false)
  const activeCards = cards ?? loadedCards
  const isLoading = cards === undefined && loadState === 'loading'
  const loadError = cards === undefined && loadState === 'error'
  const selectedIndex = Math.min(currentIndex, Math.max(activeCards.length - 1, 0))
  const currentCard = activeCards[selectedIndex]
  const correctCount = Object.values(ratings).filter((rating) => rating === 'correct').length
  const incorrectCount = Object.values(ratings).filter((rating) => rating === 'incorrect').length

  useEffect(() => {
    if (cards !== undefined) return

    const controller = new AbortController()

    fetchFlashcards(undefined, controller.signal)
      .then((result) => {
        setLoadedCards(result)
        setLoadState('success')
      })
      .catch(() => {
        if (!controller.signal.aborted) setLoadState('error')
      })

    return () => controller.abort()
  }, [cards, retryCount])

  function showPreviousCard() {
    setCurrentIndex((index) => Math.max(index - 1, 0))
  }

  function showNextCard() {
    setCurrentIndex((index) => Math.min(index + 1, activeCards.length - 1))
  }

  function rateCurrentCard(rating: FlashcardRating) {
    if (!currentCard) return

    setRatings((currentRatings) => ({
      ...currentRatings,
      [currentCard.id]: rating,
    }))

    if (selectedIndex === activeCards.length - 1) {
      setIsComplete(true)
    } else {
      showNextCard()
    }
  }

  return (
    <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-900 sm:px-8">
      <div className="mx-auto max-w-2xl">
        {!isComplete && (
          <Link
            to="/"
            className="text-sm font-medium text-indigo-700 underline-offset-4 hover:underline"
          >
            Strona główna
          </Link>
        )}

        <header className="mb-8 mt-10">
          <p className="text-sm font-semibold uppercase tracking-wide text-indigo-700">
            Nauka
          </p>
          <h1 className="mt-2 text-3xl font-bold">Fiszki</h1>
        </header>

        {isLoading ? (
          <p role="status" className="rounded-xl border border-slate-200 bg-white p-8 text-slate-600">
            Ładowanie fiszek...
          </p>
        ) : loadError ? (
          <section role="alert" className="rounded-xl border border-rose-200 bg-rose-50 p-8 text-rose-800">
            <p>Nie udało się pobrać fiszek.</p>
            <button
              type="button"
              onClick={() => {
                setLoadState('loading')
                setRetryCount((count) => count + 1)
              }}
              className="mt-4 rounded-lg border border-rose-300 px-4 py-2 font-medium hover:bg-rose-100"
            >
              Spróbuj ponownie
            </button>
          </section>
        ) : isComplete ? (
          <section className="flex flex-col items-center">
            <Link
              to="/"
              className="inline-flex min-h-20 w-full max-w-md items-center justify-center rounded-lg bg-indigo-700 px-6 py-4 text-center text-lg font-semibold text-white transition-colors hover:bg-indigo-800 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-700"
            >
              Powrót do strony głównej
            </Link>
            <div className="mt-6 grid w-full grid-cols-2 gap-3 text-center" aria-live="polite">
              <p className="rounded-lg border border-rose-200 bg-rose-50 px-3 py-2 text-sm font-medium text-rose-800">
                Niepoprawne: {incorrectCount}
              </p>
              <p className="rounded-lg border border-emerald-200 bg-emerald-50 px-3 py-2 text-sm font-medium text-emerald-800">
                Poprawne: {correctCount}
              </p>
            </div>
          </section>
        ) : currentCard ? (
          <>
            <p className="mb-3 text-right text-sm font-medium text-slate-600" aria-live="polite">
              Karta {selectedIndex + 1} z {activeCards.length}
            </p>

            <Flashcard
              key={currentCard.id}
              frontText={currentCard.frontText}
              backText={currentCard.backText}
              onRate={rateCurrentCard}
            />

            <div className="mt-4 grid grid-cols-2 gap-3 text-center" aria-live="polite">
              <p className="rounded-lg border border-rose-200 bg-rose-50 px-3 py-2 text-sm font-medium text-rose-800">
                Niepoprawne: {incorrectCount}
              </p>
              <p className="rounded-lg border border-emerald-200 bg-emerald-50 px-3 py-2 text-sm font-medium text-emerald-800">
                Poprawne: {correctCount}
              </p>
            </div>

            <nav aria-label="Nawigacja fiszek" className="mt-6 flex justify-between">
              <button
                type="button"
                onClick={showPreviousCard}
                disabled={selectedIndex === 0}
                className="rounded-lg border border-slate-300 px-4 py-2 font-medium text-slate-700 hover:bg-white disabled:cursor-not-allowed disabled:opacity-40"
              >
                Poprzednia
              </button>
              <button
                type="button"
                onClick={showNextCard}
                disabled={selectedIndex === activeCards.length - 1}
                className="rounded-lg border border-slate-300 px-4 py-2 font-medium text-slate-700 hover:bg-white disabled:cursor-not-allowed disabled:opacity-40"
              >
                Następna
              </button>
            </nav>
          </>
        ) : (
          <p className="rounded-xl border border-slate-200 bg-white p-8 text-slate-600">
            Ten zestaw nie zawiera jeszcze żadnych fiszek.
          </p>
        )}
      </div>
    </main>
  )
}