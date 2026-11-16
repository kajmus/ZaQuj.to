import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import { fetchCategory, fetchTopics, type Topic } from './api'

export default function TopicsPage() {
  const { categoryId } = useParams()
  const isAllCategories = categoryId === 'all'
  const hasValidCategoryId = isAllCategories || Boolean(categoryId && /^\d+$/.test(categoryId))
  const [categoryName, setCategoryName] = useState(isAllCategories ? 'Wszystkie' : '')
  const [topics, setTopics] = useState<Topic[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!hasValidCategoryId || !categoryId) return

    const id = isAllCategories ? 'all' : Number(categoryId)
    const requests = [fetchTopics(id)]

    if (!isAllCategories) {
      requests.push(fetchCategory(Number(categoryId)).then((category) => {
        setCategoryName(category.name)
        return []
      }))
    }

    Promise.all(requests)
      .then(([loadedTopics]) => setTopics(loadedTopics))
      .catch(() => setError('Nie udało się pobrać tematów.'))
      .finally(() => setIsLoading(false))
  }, [categoryId, hasValidCategoryId, isAllCategories])

  return (
    <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-900 sm:px-8">
      <div className="mx-auto max-w-3xl">
        <Link
          to="/categories"
          className="text-sm font-medium text-indigo-700 underline-offset-4 hover:underline"
        >
          Kategorie
        </Link>

        <header className="mb-8 mt-10">
          <p className="text-sm font-semibold uppercase tracking-wide text-indigo-700">
            Tematy
          </p>
          <h1 className="mt-2 text-3xl font-bold">
            {categoryName || 'Ładowanie kategorii...'}
          </h1>
        </header>

        {!hasValidCategoryId && <p role="alert">Nie znaleziono kategorii.</p>}
        {hasValidCategoryId && isLoading && <p role="status">Ładowanie tematów...</p>}
        {error && <p role="alert">{error}</p>}

        {hasValidCategoryId && !isLoading && !error && topics.length === 0 && (
          <p className="mb-4 text-slate-600">Brak tematów.</p>
        )}

        {hasValidCategoryId && !isLoading && !error && (
          <ul aria-label="Tematy" className="divide-y divide-slate-200 border-y border-slate-200">
            {topics.map((topic) => (
              <li key={topic.id}>
                <button
                  type="button"
                  disabled
                  className="flex min-h-14 w-full cursor-not-allowed items-center justify-between gap-4 py-3 text-left font-medium text-slate-500"
                >
                  <span>{topic.name}</span>
                </button>
              </li>
            ))}
            <li>
              <button
                type="button"
                disabled
                className="flex min-h-14 w-full cursor-not-allowed items-center justify-between gap-4 py-3 text-left font-semibold text-indigo-400"
              >
                <span>Wszystkie</span>
              </button>
            </li>
          </ul>
        )}
      </div>
    </main>
  )
}