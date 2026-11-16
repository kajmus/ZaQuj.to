export interface Category {
  id: number
  name: string
}

export interface Topic {
  id: number
  name: string
}

interface ListResponse<T> {
  items: T[]
  total: number
}

const apiBaseUrl = (import.meta.env.VITE_API_BASE_URL ?? '').replace(/\/$/, '')

async function getJson<T>(path: string): Promise<T> {
  const response = await fetch(`${apiBaseUrl}/api${path}`)

  if (!response.ok) {
    throw new Error(`Błąd pobierania danych (${response.status}).`)
  }

  return response.json() as Promise<T>
}

export async function fetchCategories(): Promise<Category[]> {
  const response = await getJson<ListResponse<Category>>('/categories/')
  return response.items
}

export function fetchCategory(categoryId: number): Promise<Category> {
  return getJson<Category>(`/categories/${categoryId}`)
}

export async function fetchTopics(categoryId: number | 'all'): Promise<Topic[]> {
  const path = categoryId === 'all'
    ? '/topics/'
    : `/topics/category/${categoryId}`
  const response = await getJson<ListResponse<Topic>>(path)
  return response.items
}