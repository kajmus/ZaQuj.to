
import { useState, type ReactNode } from 'react'
import { CounterContext } from './counter-context'

// USUŃ MNIE, GDY PRZESTANĘ BYĆ PRZYDATNY JAKO DEMO

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
