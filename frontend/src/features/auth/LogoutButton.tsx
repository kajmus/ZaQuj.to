import { useNavigate } from 'react-router-dom'
import { endSession } from '../../lib/session'

export default function LogoutButton() {
  const navigate = useNavigate()

  function handleLogout() {
    endSession()
    window.dispatchEvent(new Event('app-session-change'))
    navigate('/', { replace: true })
  }

  return (
    <button
      type="button"
      onClick={handleLogout}
      className="fixed right-5 top-4 z-10 rounded px-2 py-1 text-xs text-slate-500 hover:text-slate-800 hover:underline focus-visible:outline-2 focus-visible:outline-indigo-600 sm:right-8"
    >
      Wyloguj się
    </button>
  )
}
