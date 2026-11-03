"""Seed study categories and flashcard topics.

Revision ID: 1
Revises: a87fbc21948b
"""

from alembic import op
import sqlalchemy as sa


revision = "1"
down_revision = "a87fbc21948b"
branch_labels = None
depends_on = None


categories = sa.table(
    "Kategoria",
    sa.column("id_category", sa.Integer),
    sa.column("name", sa.Text),
)

flashcards = sa.table(
    "Pytanie_Fiszka",
    sa.column("id_fiszka", sa.Integer),
    sa.column("name", sa.Text),
    sa.column("id_category", sa.Integer),
    sa.column("text_answer", sa.Text),
)


TOPICS = (
    (
        "Architektura komputerów",
        (
            "Struktura i organizacja typowego systemu komputerowego.",
            "Budowa i działanie typowego procesora ogólnego przeznaczenia.",
            "Wykonywanie rozkazów przez procesor(y), przerwania, wyjątki.",
            "Dane i ich przetwarzanie w systemie komputerowym.",
            "Koncepcja „konwencjonalnej maszyny”, język maszynowy, asembler.",
            "Połączenia wewnątrz- i zewnątrz-systemowe, urządzenia wejścia/wyjścia.",
            "Realizacja przetwarzania równoległego w systemach komputerowych.",
            "Optymalizacja wydajności procesora(ów) i systemu komputerowego.",
        ),
    ),
    (
        "Systemy operacyjne i programowanie systemowe",
        (
            "Koncepcja systemu operacyjnego, typowa funkcjonalność, realizacje.",
            "Zarządzanie zasobami, abstrakcje systemowe.",
            "Procesy i wątki, wielozadaniowość/wielowątkowość, wielodostęp.",
            "Mechanizmy komunikacji wewnątrzsystemowej.",
            "Zarządzanie zbiorami danych, pliki, systemy plików.",
            "Interfejsy systemowe dla wykonywanego kodu, dla programisty, dla użytkownika.",
            "Wirtualizacja sprzętu i zasobów systemowych.",
            "Współczesne koncepcje budowy systemów operacyjnych.",
        ),
    ),
    (
        "Sieci komputerowe",
        (
            "Modele referencyjne systemu sieciowego, usługi, protokoły, interfejsy, standaryzacja.",
            "Koncepcja kanału komunikacyjnego, media komunikacyjne, współdzielenie medium.",
            "Sieci komputerowe z komutacją pakietów, enkapsulacja danych, przełączanie, przełączniki.",
            "Sieci komputerowe z komutacją obwodów, obwody wirtualne, tunelowanie.",
            "Trasowanie, sterowanie ruchem, obciążeniem, przepływnością, jakością usług.",
            "Typowe protokoły sieciowe i transportowe.",
            "Typowe usługi sieciowe, związane z nimi protokoły i aplikacje.",
            "Zagrożenia bezpieczeństwa w środowiskach sieciowych, ochrona i przeciwdziałanie.",
        ),
    ),
)


def upgrade() -> None:
    op.bulk_insert(
        categories,
        [
            {"id_category": category_id, "name": name}
            for category_id, (name, _) in enumerate(TOPICS, start=1)
        ],
    )

    rows = []
    flashcard_id = 1
    for category_id, (_, topic_names) in enumerate(TOPICS, start=1):
        for topic_name in topic_names:
            rows.append(
                {
                    "id_fiszka": flashcard_id,
                    "name": topic_name,
                    "id_category": category_id,
                    "text_answer": "",
                }
            )
            flashcard_id += 1
    op.bulk_insert(flashcards, rows)


def downgrade() -> None:
    connection = op.get_bind()
    connection.execute(
        flashcards.delete().where(flashcards.c.id_fiszka.in_(range(1, 25)))
    )
    connection.execute(
        categories.delete().where(categories.c.id_category.in_((1, 2, 3)))
    )
