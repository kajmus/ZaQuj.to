import { Link } from 'react-router-dom'
import CategorySelector from './CategorySelector'

export default function CategoriesPage() {
  return (
    <main className="min-h-screen bg-slate-50 px-5 py-8 text-slate-900 sm:px-8">
      <div className="mx-auto max-w-3xl">
        <Link
          to="/"
          className="text-sm font-medium text-indigo-700 underline-offset-4 hover:underline"
        >
          Strona główna
        </Link>

        <header className="mb-8 mt-10">
          <p className="text-sm font-semibold uppercase tracking-wide text-indigo-700">
            Nauka
          </p>
          <h1 className="mt-2 text-3xl font-bold">Kategorie</h1>
        </header>

        <CategorySelector />
      </div>
    </main>
  )
}