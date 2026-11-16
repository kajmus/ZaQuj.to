
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from '../features/home/HomePage'
import DummyPage from '../features/dummy/DummyPage'
import FlashcardsPage from '../features/flashcards/FlashcardsPage'
import CategoriesPage from '../features/categories/CategoriesPage'
import TopicsPage from '../features/categories/TopicsPage'
import { CounterProvider } from '../features/state-demo/CounterContext'

export default function App() {
  return (
    <CounterProvider>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dummy" element={<DummyPage />} />
        <Route path="/categories" element={<CategoriesPage />} />
        <Route path="/categories/:categoryId/topics" element={<TopicsPage />} />
        <Route path="/flashcards" element={<FlashcardsPage />} />
      </Routes>
    </BrowserRouter>
    </CounterProvider>
  )
}
