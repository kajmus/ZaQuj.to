import type { FlashcardData } from './Flashcard'
import { fetchCategoryTopicIds } from '../categories/api'

interface FlashcardApiResponse {
  items: {
    id: number
    front_text: string
    back_text: string
  }[]
}

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? ''

export async function fetchFlashcards(
  topicId?: number | string,
  signal?: AbortSignal,
): Promise<FlashcardData[]> {
  const endpoint = topicId === undefined
    ? '/api/flashcards/'
    : `/api/flashcards/topic/${encodeURIComponent(topicId)}`
  const response = await fetch(`${apiBaseUrl.replace(/\/$/, '')}${endpoint}`, { signal })

  if (!response.ok) {
    throw new Error(`Flashcards request failed with status ${response.status}`)
  }

  const data = await response.json() as FlashcardApiResponse
  return data.items.map((item) => ({
    id: String(item.id),
    frontText: item.front_text,
    backText: item.back_text,
  }))
}

export async function fetchCategoryFlashcards(
  categoryId: number,
  signal?: AbortSignal,
): Promise<FlashcardData[]> {
  const topicIds = await fetchCategoryTopicIds(categoryId)
  const cardsByTopic = await Promise.all(
    topicIds.map((topicId) => fetchFlashcards(topicId, signal)),
  )
  return cardsByTopic.flat()
}