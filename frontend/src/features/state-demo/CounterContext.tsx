
import {
  createContext,
  useContext,
  useState,
  type ReactNode,
} from 'react'

type CounterContextValue = {
  count: number
  increment: () => void
  reset: () => void
}

const CounterContext = createContext<CounterContextValue | undefined>(
  undefined,
)

export function CounterProvider({ children }: { children: ReactNode }) {
  const [count, setCount] = useState(0)

  function increment() {
    setCount((current) => current + 1)
  }

  function reset() {
    setCount(0)
  }

  return (
    <CounterContext.Provider value={{ count, increment, reset }}>
      {children}
    </CounterContext.Provider>
  )
}

export function useCounter() {
  const context = useContext(CounterContext)

  if (context === undefined) {
    throw new Error('useCounter must be used within CounterProvider')
  }

  return context
}
