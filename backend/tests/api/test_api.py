from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient

from app.main import app
from app.models.abcd_question import ABCDQuestion

client = TestClient(app)

V1_MODULE = "app.api.v1.endpoints.flashcards"
BASE_URL = "/api/flashcards"

# Dummy model instance for test assertions
mock_question = ABCDQuestion(
    id_pytanie=1,
    text="What is 2 + 2?",
    id_temat=10,
    correct_answer="4",
    wrong_answer_1="3",
    wrong_answer_2="5",
    wrong_answer_3="22",
)

@patch(f"{V1_MODULE}.get_questions_by_topic", new_callable=AsyncMock)
def test_get_flashcards_by_topic_success(mock_get_questions):
    mock_get_questions.return_value = [mock_question]

    response = client.get(f"{BASE_URL}/topic/10")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {
                "id": 1,
                "front_text": "What is 2 + 2?",
                "back_text": "4",
            }
        ],
        "total": 1,
    }
    mock_get_questions.assert_called_once()


@patch(f"{V1_MODULE}.get_questions_by_topic", new_callable=AsyncMock)
def test_get_flashcards_by_topic_empty(mock_get_questions):
    # Mock CRUD returning zero results
    mock_get_questions.return_value = []

    response = client.get(f"{BASE_URL}/topic/999")

    assert response.status_code == 200
    assert response.json() == {
        "items": [],
        "total": 0,
    }
    mock_get_questions.assert_called_once()


@patch(f"{V1_MODULE}.get_question_by_id", new_callable=AsyncMock)
def test_get_flashcard_success(mock_get_question):
    # Mock CRUD returning single found question
    mock_get_question.return_value = mock_question

    response = client.get(f"{BASE_URL}/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "front_text": "What is 2 + 2?",
        "back_text": "4",
    }
    mock_get_question.assert_called_once()


@patch(f"{V1_MODULE}.get_question_by_id", new_callable=AsyncMock)
def test_get_flashcard_not_found(mock_get_question):
    mock_get_question.return_value = None

    response = client.get(f"{BASE_URL}/999")

    assert response.status_code == 404
    mock_get_question.assert_called_once()