// PRZYKŁADOWY TEST
// Usuń mnie, gdy przestanę być przydatny jako demo!

import { beforeEach, describe, expect, it } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { CounterProvider } from './CounterContext'
import StateDemo from './StateDemo'

describe('StateDemo — cookies', () => {
  beforeEach(() => {
    document.cookie = 'state_demo_note=; Max-Age=0; Path=/'
  })

  it('zapisuje wpisaną wartość w cookie i pokazuje ją na stronie', async () => {
    const user = userEvent.setup()

    render(
      <CounterProvider>
        <StateDemo />
      </CounterProvider>,
    )

    const input = screen.getByRole('textbox', {
      name: 'Wartość cookie',
    })

    await user.type(input, 'Moja notatka')

    await user.click(
      screen.getByRole('button', { name: 'Zapisz cookie' }),
    )

    expect(
      screen.getByText('Moja notatka'),
    ).toBeInTheDocument()

    expect(document.cookie).toContain(
      'state_demo_note=Moja%20notatka',
    )
  })

  it('usuwa zapisaną wartość cookie', async () => {
    const user = userEvent.setup()

    document.cookie = 'state_demo_note=test; Path=/'

    render(
      <CounterProvider>
        <StateDemo />
      </CounterProvider>,
    )

    await user.click(
      screen.getByRole('button', { name: 'Usuń cookie' }),
    )

    expect(document.cookie).not.toContain('state_demo_note=')

    expect(
      screen.getByText('(brak wartości)'),
    ).toBeInTheDocument()
  })
})
