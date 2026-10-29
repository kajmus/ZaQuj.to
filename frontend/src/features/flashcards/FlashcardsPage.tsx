import { useState } from 'react'
import { Link } from 'react-router-dom'
import Flashcard, { type FlashcardData } from './Flashcard'

const sampleCards: FlashcardData[] = [
  {
    id: '1',
    frontText: 'Pytanie numer jeden',
    backText: 'Odpowiedź numer jeden',
  },
  {
    id: '2',
    frontText: 'Pytanie numer dwa',
    backText: 'Odpowiedź numer dwa',
  },
  {
    id: '3',
    frontText: 'Bardzo długie pytanie numer trzy, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.',
    backText: 'Bardzo długa odpowiedź numer trzy, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.',
    // Najwięcej na standardowym ekranie mieści się około 300 znaków, na telefonie około 100. 
    // TODO: Dorobić skalowanie tekstu lub wielkości fiszki
},
]

interface FlashcardsPageProps {
  cards?: FlashcardData[]
}

export default function FlashcardsPage({
  cards = sampleCards,
}: FlashcardsPageProps) {
  const [currentIndex, setCurrentIndex] = useState(0)
  const selectedIndex = Math.min(currentIndex, Math.max(cards.length - 1, 0))
  const currentCard = cards[selectedIndex]

  function showPreviousCard() {
    setCurrentIndex((index) => Math.max(index - 1, 0))
  }

  function showNextCard() {
    setCurrentIndex((index) => Math.min(index + 1, cards.length - 1))
  }

  return (
    <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-900 sm:px-8">
      <div className="mx-auto max-w-2xl">
        <Link
          to="/"
          className="text-sm font-medium text-indigo-700 underline-offset-4 hover:underline"
        >
          Strona główna
        </Link>

        <header className="mb-8 mt-10">
          <p className="text-sm font-semibold uppercase tracking-wide text-indigo-700">
            Nauka
          </p>
          <h1 className="mt-2 text-3xl font-bold">Fiszki</h1>
        </header>

        {currentCard ? (
          <>
            <p className="mb-3 text-right text-sm font-medium text-slate-600" aria-live="polite">
              Karta {selectedIndex + 1} z {cards.length}
            </p>

            <Flashcard
              key={currentCard.id}
              frontText={currentCard.frontText}
              backText={currentCard.backText}
            />

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
                disabled={selectedIndex === cards.length - 1}
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