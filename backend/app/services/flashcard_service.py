from app.schemas.flashcards import FlashcardResponse, FlashcardListResponse
from app.models.abcd_question import ABCDQuestion
from typing import Sequence

"""Converts database model question to flashcard schema"""
def map_abcd_question_to_flashcard(question: ABCDQuestion) -> FlashcardResponse:
    if question is None: 
        return None
    return FlashcardResponse(
        id=question.id_pytanie,
        front_text=question.text,
        back_text=question.correct_answer
    )

"""Converts sequence of database model questions to flashcard list schema"""
def map_abcd_questions_seq_to_flashcard(questions: Sequence[ABCDQuestion]) -> FlashcardListResponse:
    flashcards = [
        map_abcd_question_to_flashcard(q) 
        for q in questions 
        if q is not None
    ]

    return FlashcardListResponse(
        items=flashcards,
        total=len(flashcards)
    )