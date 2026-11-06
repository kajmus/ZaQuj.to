
import { describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { CounterProvider } from './CounterContext'
import StateDemo from './StateDemo'

describe('React Context — licznik', () => {
  it('zwiększa licznik po kliknięciu przycisku', async () => {
    const user = userEvent.setup()

    render(
      <CounterProvider>
        <StateDemo />
      </CounterProvider>,
    )

    await user.click(
      screen.getByRole('button', { name: 'Zwiększ' }),
    )

    expect(
      screen.getByText('Licznik współdzielony: 1'),
    ).toBeInTheDocument()
  })

  it('zeruje licznik po kliknięciu przycisku resetowania', async () => {
    const user = userEvent.setup()

    render(
      <CounterProvider>
        <StateDemo />
      </CounterProvider>,
    )

    await user.click(
      screen.getByRole('button', { name: 'Zwiększ' }),
    )
    await user.click(
      screen.getByRole('button', { name: 'Zwiększ' }),
    )
    await user.click(
      screen.getByRole('button', { name: 'Wyzeruj' }),
    )

    expect(
      screen.getByText('Licznik współdzielony: 0'),
    ).toBeInTheDocument()
  })
})
