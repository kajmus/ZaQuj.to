import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { fetchCategories, type Category } from './api'

export default function CategorySelector() {
  const [categories, setCategories] = useState<Category[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchCategories()
      .then(setCategories)
      .catch(() => setError('Nie udało się pobrać kategorii.'))
      .finally(() => setIsLoading(false))
  }, [])

  return (
    <>
      {isLoading && <p role="status">Ładowanie kategorii...</p>}
      {error && <p role="alert">{error}</p>}

      {!isLoading && !error && categories.length === 0 && (
        <p className="mb-4 text-slate-600">Brak kategorii.</p>
      )}

      {!isLoading && !error && (
        <nav aria-label="Kategorie">
          <ul className="divide-y divide-slate-200 border-y border-slate-200">
            {categories.map((category) => (
              <li key={category.id}>
                <Link
                  to={`/categories/${category.id}/topics`}
                  className="flex min-h-14 items-center justify-between gap-4 py-3 font-medium text-slate-800 hover:text-indigo-700"
                >
                  <span>{category.name}</span>
                  <span aria-hidden="true" className="text-slate-400">›</span>
                </Link>
              </li>
            ))}
            <li>
              <Link
                to="/all"
                className="flex min-h-14 items-center justify-between gap-4 py-3 font-semibold text-indigo-700 hover:text-indigo-900"
              >
                <span>Wszystkie</span>
                <span aria-hidden="true">›</span>
              </Link>
            </li>
          </ul>
        </nav>
      )}
    </>
  )
}