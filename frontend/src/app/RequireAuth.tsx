import { Navigate, Outlet, useLocation } from 'react-router-dom'
import { isSessionActive } from '../lib/session'
import LogoutButton from '../features/auth/LogoutButton'

export default function RequireAuth() {
  const location = useLocation()

  if (!isSessionActive()) {
    return <Navigate to="/login" replace state={{ from: location }} />
  }

  return (
    <>
      <LogoutButton />
      <Outlet />
    </>
  )
}
