import { useLayoutEffect, useRef, useState } from 'react'
import { fitTextToContainer } from './fit-text'

const MAX_FONT_SIZE = 24

function FittedText({ text }: { text: string }) {
  const containerRef = useRef<HTMLDivElement>(null)
  const textRef = useRef<HTMLSpanElement>(null)

  useLayoutEffect(() => {
    const container = containerRef.current
    const content = textRef.current
    if (!container || !content) return

    const fit = () => fitTextToContainer(content, container)
    fit()

    if (typeof ResizeObserver === 'undefined') return

    const observer = new ResizeObserver(fit)
    observer.observe(container)
    return () => observer.disconnect()
  }, [text])

  return (
    <div
      ref={containerRef}
      className="flex min-h-0 flex-1 items-center justify-center overflow-hidden"
    >
      <span
        ref={textRef}
        className="block max-h-full w-full overflow-hidden text-center font-semibold leading-tight text-slate-900"
        style={{ fontSize: `${MAX_FONT_SIZE}px` }}
      >
        {text}
      </span>
    </div>
  )
}

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
          className="group relative block h-[min(60vh,28rem)] min-h-72 w-full rounded-xl text-left focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-indigo-600"
        >
          <span
            className={`absolute inset-0 block transition-transform duration-500 [transform-style:preserve-3d] ${isFlipped ? '[transform:rotateY(180deg)]' : ''}`}
          >
            <span
              aria-hidden={isFlipped}
              className="absolute inset-0 flex flex-col rounded-xl border border-slate-200 bg-white p-6 shadow-sm [backface-visibility:hidden] sm:p-8"
            >
              <span className="text-sm font-semibold uppercase tracking-wide text-indigo-700">
                Pytanie
              </span>
              <FittedText text={frontText} />
              <span className="text-center text-sm text-slate-500">
                Kliknij, aby zobaczyć odpowiedź
              </span>
            </span>
            <span
              aria-hidden={!isFlipped}
              className="absolute inset-0 flex flex-col rounded-xl border border-teal-200 bg-teal-50 p-6 shadow-sm [backface-visibility:hidden] [transform:rotateY(180deg)] sm:p-8"
            >
              <span className="text-sm font-semibold uppercase tracking-wide text-teal-800">
                Odpowiedź
              </span>
              <FittedText text={backText} />
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