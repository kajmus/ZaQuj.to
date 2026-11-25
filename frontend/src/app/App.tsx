import { BrowserRouter, Routes, Route } from 'react-router-dom'
import HomePage from '../features/home/HomePage'
import DummyPage from '../features/dummy/DummyPage'
import FlashcardsPage from '../features/flashcards/FlashcardsPage'
import CategoriesPage from '../features/categories/CategoriesPage'
import TopicsPage from '../features/categories/TopicsPage'
import TopicPage from '../features/categories/TopicPage'
import CategoryAllPage from '../features/categories/CategoryAllPage'
import { CounterProvider } from '../features/state-demo/CounterContext'
import AuthPage from '../features/auth/AuthPage'
import AllQuestionsPage from '../features/home/AllQuestionsPage'

export default function App() {
  return (
    <CounterProvider>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/all" element={<AllQuestionsPage />} />
        <Route path="/login" element={<AuthPage />} />
        <Route path="/dummy" element={<DummyPage />} />
        <Route path="/categories" element={<CategoriesPage />} />
        <Route path="/categories/:categoryId/topics" element={<TopicsPage />} />
        <Route path="/categories/:categoryId/all" element={<CategoryAllPage />} />
        <Route path="/topics/:topicId" element={<TopicPage />} />
        <Route path="/flashcards" element={<FlashcardsPage />} />
        <Route path="/flashcards/topic/:topicId" element={<FlashcardsPage />} />
        <Route path="/flashcards/category/:categoryId" element={<FlashcardsPage />} />
      </Routes>
    </BrowserRouter>
    </CounterProvider>
  )
}
