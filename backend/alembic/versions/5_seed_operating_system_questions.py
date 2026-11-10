"""Add two ABCD questions for each operating systems topic.

Revision ID: 5
Revises: 4
"""

from alembic import op
import sqlalchemy as sa


revision = "5"
down_revision = "4"
branch_labels = None
depends_on = None


questions = sa.table(
    "Pytanie_ABCD",
    sa.column("text", sa.Text),
    sa.column("id_temat", sa.Integer),
    sa.column("correct_answer", sa.Text),
    sa.column("wrong_answer_1", sa.Text),
    sa.column("wrong_answer_2", sa.Text),
    sa.column("wrong_answer_3", sa.Text),
)

QUESTIONS = (
    (9, "Jaka jest podstawowa rola systemu operacyjnego?", "Zarządzanie zasobami komputera i udostępnianie usług programom.", "Tłumaczenie każdego programu na kod maszynowy.", "Przechowywanie wyłącznie dokumentów użytkownika.", "Zastępowanie procesora podczas wykonywania instrukcji."),
    (9, "Czym jest jądro systemu operacyjnego?", "Częścią systemu realizującą podstawowe usługi i zarządzającą zasobami.", "Programem użytkownika służącym tylko do edycji plików.", "Wyłącznie graficznym interfejsem logowania.", "Zbiorem aplikacji instalowanych niezależnie od systemu."),
    (10, "Co obejmuje przydział zasobów przez system operacyjny?", "Udostępnianie procesom zasobów zgodnie z zasadami ich użycia.", "Przydzielanie każdemu procesowi wszystkich zasobów na stałe.", "Usuwanie procesu przy każdej próbie dostępu do urządzenia.", "Zastępowanie sprzętu samym oprogramowaniem."),
    (10, "Po co system operacyjny stosuje abstrakcje zasobów?", "Aby udostępniać jednolity sposób korzystania ze sprzętu bez ujawniania jego szczegółów.", "Aby uniemożliwić programom korzystanie z urządzeń.", "Aby wszystkie urządzenia miały identyczną budowę fizyczną.", "Aby zrezygnować z ochrony dostępu do zasobów."),
    (11, "Czym proces różni się od programu zapisanego w pliku?", "Proces jest wykonywaną instancją programu z własnym stanem.", "Proces jest wyłącznie kodem źródłowym programu.", "Program zawsze ma własny licznik rozkazów, zanim zostanie uruchomiony.", "Proces istnieje tylko po zakończeniu programu."),
    (11, "Co współdzielą wątki tego samego procesu?", "Przestrzeń adresową i zasoby procesu.", "Własny stos każdego wątku.", "Własny licznik rozkazów każdego wątku.", "Oddzielną przestrzeń adresową dla każdego wątku."),
    (12, "Do czego służy pamięć współdzielona w komunikacji między procesami?", "Pozwala procesom korzystać z tego samego obszaru pamięci.", "Przesyła dane wyłącznie przez plik na dysku.", "Zapewnia osobną kopię pamięci dla każdego procesu bez wymiany danych.", "Zastępuje planistę procesów przy przydziale procesora."),
    (12, "Jaką rolę pełni semafor w programach współbieżnych?", "Pomaga synchronizować dostęp do wspólnego zasobu.", "Przechowuje kod wykonywalny procesu.", "Zastępuje system plików w zapisie danych.", "Nadaje każdemu procesowi nowy identyfikator."),
    (13, "Czym jest system plików?", "Sposobem organizowania, przechowywania i udostępniania plików.", "Wyłącznie fizycznym nośnikiem danych.", "Programem służącym tylko do kompresji plików.", "Pamięcią operacyjną przydzieloną jednemu procesowi."),
    (13, "Czym jest dowiązanie symboliczne?", "Odwołaniem do innego pliku lub katalogu przez jego ścieżkę.", "Osobną kopią zawartości pliku docelowego.", "Listą uprawnień użytkowników do pliku.", "Blokiem danych zawierającym wyłącznie kod programu."),
    (14, "Czym jest wywołanie systemowe?", "Interfejsem, przez który program żąda usługi jądra.", "Instrukcją wykonywaną wyłącznie przez użytkownika w powłoce.", "Funkcją służącą tylko do formatowania tekstu.", "Sposobem bezpośredniej zmiany sprzętu z pominięciem systemu."),
    (14, "Co opisuje interfejs API udostępniony programiście?", "Funkcje oraz zasady ich użycia przez program.", "Fizyczny układ ścieżek na dysku.", "Wyłącznie wygląd okien systemowych.", "Zawartość rejestrów procesora po wyłączeniu komputera."),
    (15, "Co umożliwia wirtualizacja sprzętu?", "Uruchamianie maszyn wirtualnych korzystających z zasobów komputera fizycznego.", "Zwiększanie fizycznej liczby rdzeni procesora bez zmiany sprzętu.", "Usunięcie potrzeby przydzielania pamięci procesom.", "Wykonywanie programów bez żadnego systemu zarządzającego zasobami."),
    (15, "Na czym polega pamięć wirtualna?", "Na oddzieleniu adresów widzianych przez proces od adresów pamięci fizycznej.", "Na zapisaniu całej pamięci operacyjnej wyłącznie na dysku.", "Na przydzieleniu wszystkim procesom tych samych adresów fizycznych.", "Na zastąpieniu pamięci RAM pamięcią podręczną procesora."),
    (16, "Czym wyróżnia się mikrojądro?", "Pozostawia w jądrze niewielki zestaw podstawowych mechanizmów.", "Umieszcza wszystkie usługi systemowe w jednym dużym jądrze.", "Nie obsługuje komunikacji między procesami.", "Wymaga uruchamiania tylko jednego programu naraz."),
    (16, "Jaką rolę pełni powłoka systemowa?", "Pośredniczy w komunikacji użytkownika z usługami systemu.", "Zastępuje sprzętową jednostkę zarządzania pamięcią.", "Przechowuje wszystkie dane plików w pamięci procesora.", "Wykonuje wyłącznie sterowniki urządzeń w trybie jądra."),
)


def upgrade() -> None:
    op.bulk_insert(
        questions,
        [dict(zip(("id_temat", "text", "correct_answer", "wrong_answer_1", "wrong_answer_2", "wrong_answer_3"), row)) for row in QUESTIONS],
    )


def downgrade() -> None:
    connection = op.get_bind()
    for topic_id, text, *_ in QUESTIONS:
        connection.execute(
            questions.delete().where(
                sa.and_(questions.c.id_temat == topic_id, questions.c.text == text)
            )
        )
