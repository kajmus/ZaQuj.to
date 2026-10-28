
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from '../features/home/HomePage'
import DummyPage from '../features/dummy/DummyPage'
import { CounterProvider } from '../features/state-demo/CounterContext'

export default function App() {
  return (
    <CounterProvider>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dummy" element={<DummyPage />} />
      </Routes>
    </BrowserRouter>
    </CounterProvider>
  )
}
