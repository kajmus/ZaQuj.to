
import { createContext } from 'react'

export type CounterContextValue = {
  count: number
  increment: () => void
  reset: () => void
}

export const CounterContext = createContext<
  CounterContextValue | undefined
>(undefined)
