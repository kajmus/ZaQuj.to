import { useState } from 'react'

export interface FlashcardData {
  id: string
  frontText: string
  backText: string
}

interface FlashcardProps {
  frontText: string
  backText: string
}

export default function Flashcard({ frontText, backText }: FlashcardProps) {
  const [isFlipped, setIsFlipped] = useState(false)

  function flipCard() {
    setIsFlipped((flipped) => !flipped)
  }

  return (
    <div className="space-y-4">
      <div className="[perspective:1000px]">
        <button
          type="button"
          aria-label={isFlipped ? 'Pokaż pytanie' : 'Pokaż odpowiedź'}
          onClick={flipCard}
          className="group relative block min-h-72 w-full rounded-xl text-left focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-indigo-600"
        >
          <span
            className={`absolute inset-0 block transition-transform duration-500 [transform-style:preserve-3d] ${isFlipped ? '[transform:rotateY(180deg)]' : ''}`}
          >
            <span
              aria-hidden={isFlipped}
              className="absolute inset-0 flex flex-col justify-between rounded-xl border border-slate-200 bg-white p-8 shadow-sm [backface-visibility:hidden]"
            >
              <span className="text-sm font-semibold uppercase tracking-wide text-indigo-700">
                Pytanie
              </span>
              <span className="text-center text-2xl font-semibold text-slate-900">
                {frontText}
              </span>
              <span className="text-center text-sm text-slate-500">
                Kliknij, aby zobaczyć odpowiedź
              </span>
            </span>
            <span
              aria-hidden={!isFlipped}
              className="absolute inset-0 flex flex-col justify-between rounded-xl border border-teal-200 bg-teal-50 p-8 shadow-sm [backface-visibility:hidden] [transform:rotateY(180deg)]"
            >
              <span className="text-sm font-semibold uppercase tracking-wide text-teal-800">
                Odpowiedź
              </span>
              <span className="text-center text-2xl font-semibold text-slate-900">
                {backText}
              </span>
              <span className="text-center text-sm text-slate-500">
                Kliknij, aby wrócić do pytania
              </span>
            </span>
          </span>
        </button>
      </div>

      <button
        type="button"
        onClick={flipCard}
        className="w-full rounded-lg bg-indigo-700 px-5 py-3 font-semibold text-white transition-colors hover:bg-indigo-800 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-700"
      >
        {isFlipped ? 'Wróć do pytania' : 'Sprawdź'}
      </button>
    </div>
  )
}