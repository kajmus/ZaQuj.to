from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient

from app.main import app
from app.models.abcd_question import ABCDQuestion
from app.models.category import Category
from app.models.topic import Topic

client = TestClient(app)

V1_MODULE = "app.api.v1.endpoints.flashcards"
BASE_URL = "/api/flashcards"

# Dummy model instance for test assertions
mock_question_1 = ABCDQuestion(
    id_pytanie=1,
    text="What is 2 + 2?",
    id_temat=10,
    correct_answer="4",
    wrong_answer_1="3",
    wrong_answer_2="5",
    wrong_answer_3="22",
)

mock_question_2 = ABCDQuestion(
    id_pytanie=2,
    text="What is the capital of France?",
    id_temat=10,
    correct_answer="Paris",
    wrong_answer_1="London",
    wrong_answer_2="Berlin",
    wrong_answer_3="Madrid",
)

mock_category_1 = Category(id_category=1, name="Mathematics")
mock_category_2 = Category(id_category=2, name="Geography")

mock_topic_1 = Topic(id_temat=10, name="Arithmetic", id_category=1)
mock_topic_2 = Topic(id_temat=20, name="Countries", id_category=2)


@patch("app.api.v1.endpoints.categories.get_all_categories", new_callable=AsyncMock)
def test_get_all_categories_success(mock_get_all_categories):
    mock_get_all_categories.return_value = [mock_category_1, mock_category_2]

    response = client.get("/api/categories/")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"id": 1, "name": "Mathematics"},
            {"id": 2, "name": "Geography"},
        ],
        "total": 2,
    }
    mock_get_all_categories.assert_called_once()


@patch("app.api.v1.endpoints.categories.get_all_categories", new_callable=AsyncMock)
def test_get_all_categories_empty(mock_get_all_categories):
    mock_get_all_categories.return_value = []

    response = client.get("/api/categories/")

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}
    mock_get_all_categories.assert_called_once()


@patch("app.api.v1.endpoints.categories.get_category_by_id", new_callable=AsyncMock)
def test_get_category_success(mock_get_category):
    mock_get_category.return_value = mock_category_1

    response = client.get("/api/categories/1")

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Mathematics"}
    mock_get_category.assert_called_once()


@patch("app.api.v1.endpoints.categories.get_category_by_id", new_callable=AsyncMock)
def test_get_category_not_found(mock_get_category):
    mock_get_category.return_value = None

    response = client.get("/api/categories/999")
    payload = response.json()

    assert response.status_code == 404
    assert "detail" in payload
    assert isinstance(payload["detail"], str)
    mock_get_category.assert_called_once()


@patch("app.api.v1.endpoints.questions.get_all_questions", new_callable=AsyncMock)
def test_get_all_questions_success(mock_get_all_questions):
    mock_get_all_questions.return_value = [mock_question_1, mock_question_2]

    response = client.get("/api/questions/")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {
                "text": "What is 2 + 2?",
                "correct_answer": "4",
                "wrong_answer_1": "3",
                "wrong_answer_2": "5",
                "wrong_answer_3": "22",
                "id": 1,
            },
            {
                "text": "What is the capital of France?",
                "correct_answer": "Paris",
                "wrong_answer_1": "London",
                "wrong_answer_2": "Berlin",
                "wrong_answer_3": "Madrid",
                "id": 2,
            },
        ],
        "total": 2,
    }
    mock_get_all_questions.assert_called_once()


@patch("app.api.v1.endpoints.questions.get_all_questions", new_callable=AsyncMock)
def test_get_all_questions_empty(mock_get_all_questions):
    mock_get_all_questions.return_value = []

    response = client.get("/api/questions/")

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}
    mock_get_all_questions.assert_called_once()


@patch("app.api.v1.endpoints.questions.get_questions_by_topic", new_callable=AsyncMock)
def test_get_questions_by_topic_success(mock_get_questions):
    mock_get_questions.return_value = [mock_question_1, mock_question_2]

    response = client.get("/api/questions/topic/10")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {
                "text": "What is 2 + 2?",
                "correct_answer": "4",
                "wrong_answer_1": "3",
                "wrong_answer_2": "5",
                "wrong_answer_3": "22",
                "id": 1,
            },
            {
                "text": "What is the capital of France?",
                "correct_answer": "Paris",
                "wrong_answer_1": "London",
                "wrong_answer_2": "Berlin",
                "wrong_answer_3": "Madrid",
                "id": 2,
            },
        ],
        "total": 2,
    }
    mock_get_questions.assert_called_once()


@patch("app.api.v1.endpoints.questions.get_question_by_id", new_callable=AsyncMock)
def test_get_question_success(mock_get_question):
    mock_get_question.return_value = mock_question_1

    response = client.get("/api/questions/1")

    assert response.status_code == 200
    assert response.json() == {
        "text": "What is 2 + 2?",
        "correct_answer": "4",
        "wrong_answer_1": "3",
        "wrong_answer_2": "5",
        "wrong_answer_3": "22",
        "id": 1,
    }
    mock_get_question.assert_called_once()


@patch("app.api.v1.endpoints.questions.get_question_by_id", new_callable=AsyncMock)
def test_get_question_not_found(mock_get_question):
    mock_get_question.return_value = None

    response = client.get("/api/questions/999")
    payload = response.json()

    assert response.status_code == 404
    assert "detail" in payload
    assert isinstance(payload["detail"], str)
    mock_get_question.assert_called_once()


@patch("app.api.v1.endpoints.topics.get_all_topics", new_callable=AsyncMock)
def test_get_all_topics_success(mock_get_all_topics):
    mock_get_all_topics.return_value = [mock_topic_1, mock_topic_2]

    response = client.get("/api/topics/")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"id": 10, "name": "Arithmetic"},
            {"id": 20, "name": "Countries"},
        ],
        "total": 2,
    }
    mock_get_all_topics.assert_called_once()


@patch("app.api.v1.endpoints.topics.get_all_topics", new_callable=AsyncMock)
def test_get_all_topics_empty(mock_get_all_topics):
    mock_get_all_topics.return_value = []

    response = client.get("/api/topics/")

    assert response.status_code == 200
    assert response.json() == {"items": [], "total": 0}
    mock_get_all_topics.assert_called_once()


@patch("app.api.v1.endpoints.topics.get_topics_by_category", new_callable=AsyncMock)
def test_get_topics_by_category_success(mock_get_topics):
    mock_get_topics.return_value = [mock_topic_1, mock_topic_2]

    response = client.get("/api/topics/category/1")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"id": 10, "name": "Arithmetic"},
            {"id": 20, "name": "Countries"},
        ],
        "total": 2,
    }
    mock_get_topics.assert_called_once()


@patch("app.api.v1.endpoints.topics.get_topic_by_id", new_callable=AsyncMock)
def test_get_topic_success(mock_get_topic):
    mock_get_topic.return_value = mock_topic_1

    response = client.get("/api/topics/10")

    assert response.status_code == 200
    assert response.json() == {"id": 10, "name": "Arithmetic"}
    mock_get_topic.assert_called_once()


@patch("app.api.v1.endpoints.topics.get_topic_by_id", new_callable=AsyncMock)
def test_get_topic_not_found(mock_get_topic):
    mock_get_topic.return_value = None

    response = client.get("/api/topics/999")
    payload = response.json()

    assert response.status_code == 404
    assert "detail" in payload
    assert isinstance(payload["detail"], str)
    mock_get_topic.assert_called_once()


@patch(f"{V1_MODULE}.get_all_questions", new_callable=AsyncMock)
def test_get_all_flashcards_success(mock_get_all_questions):
    mock_get_all_questions.return_value = [mock_question_1, mock_question_2]

    response = client.get(f"{BASE_URL}/")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {
                "id": 1,
                "front_text": "What is 2 + 2?",
                "back_text": "4",
            },
            {
                "id": 2,
                "front_text": "What is the capital of France?",
                "back_text": "Paris",
            },
        ],
        "total": 2,
    }
    mock_get_all_questions.assert_called_once()


@patch(f"{V1_MODULE}.get_all_questions", new_callable=AsyncMock)
def test_get_all_flashcards_empty(mock_get_all_questions):
    mock_get_all_questions.return_value = []

    response = client.get(f"{BASE_URL}/")

    assert response.status_code == 200
    assert response.json() == {
        "items": [],
        "total": 0,
    }
    mock_get_all_questions.assert_called_once()


@patch(f"{V1_MODULE}.get_questions_by_topic", new_callable=AsyncMock)
def test_get_flashcards_by_topic_success(mock_get_questions):
    mock_get_questions.return_value = [mock_question_1, mock_question_2]

    response = client.get(f"{BASE_URL}/topic/10")

    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {
                "id": 1,
                "front_text": "What is 2 + 2?",
                "back_text": "4",
            },
            {
                "id": 2,
                "front_text": "What is the capital of France?",
                "back_text": "Paris",
            },
        ],
        "total": 2,
    }
    mock_get_questions.assert_called_once()


@patch(f"{V1_MODULE}.get_questions_by_topic", new_callable=AsyncMock)
def test_get_flashcards_by_topic_empty(mock_get_questions):
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
    mock_get_question.return_value = mock_question_1

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
    payload = response.json()

    assert response.status_code == 404
    assert "detail" in payload
    assert isinstance(payload["detail"], str)
    mock_get_question.assert_called_once()