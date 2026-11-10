"""Add two ABCD questions for each database topic.

Revision ID: 3
Revises: 2
"""

from alembic import op
import sqlalchemy as sa


revision = "3"
down_revision = "2"
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
    (52, "Czym jest dziedzina atrybutu w relacyjnym modelu danych?", "Zbiorem wartości dopuszczalnych dla atrybutu.", "Zbiorem wszystkich krotek relacji.", "Liczbą kolumn w relacji.", "Wynikiem projekcji relacji."),
    (52, "Czym różni się selekcja od projekcji w algebrze relacji?", "Selekcja wybiera krotki, a projekcja atrybuty.", "Selekcja wybiera atrybuty, a projekcja krotki.", "Selekcja łączy relacje, a projekcja je odejmuje.", "Selekcja usuwa duplikaty, a projekcja sortuje krotki."),
    (53, "Do czego służy klauzula GROUP BY w zapytaniu SQL?", "Do łączenia wierszy w grupy według wskazanych kolumn.", "Do sortowania wierszy według wskazanych kolumn.", "Do ograniczania liczby zwracanych kolumn.", "Do aktualizowania wierszy spełniających warunek."),
    (53, "Czym charakteryzuje się podzapytanie skorelowane?", "Odwołuje się do wartości z zapytania zewnętrznego.", "Zawsze zwraca dokładnie jeden wiersz.", "Może wystąpić tylko w klauzuli FROM.", "Nie może korzystać z funkcji agregujących."),
    (54, "Która instrukcja DML służy do dodawania nowych wierszy do tabeli?", "INSERT.", "UPDATE.", "DELETE.", "ALTER TABLE."),
    (54, "Jaką rolę pełni klauzula WHERE w instrukcjach UPDATE i DELETE?", "Wskazuje wiersze objęte zmianą lub usunięciem.", "Wskazuje kolumny tworzące klucz główny.", "Ustala kolejność wykonania zmian.", "Zatwierdza wykonaną transakcję."),
    (55, "Która instrukcja DDL służy do zmiany struktury istniejącej tabeli?", "ALTER TABLE.", "CREATE TABLE.", "INSERT INTO.", "UPDATE."),
    (55, "Czym różni się DROP TABLE od DELETE FROM bez klauzuli WHERE?", "DROP TABLE usuwa tabelę, a DELETE usuwa jej wiersze.", "DROP TABLE usuwa wiersze, a DELETE usuwa tabelę.", "Obie instrukcje usuwają wyłącznie definicję tabeli.", "Obie instrukcje zmieniają tylko strukturę kolumn."),
    (56, "Co oznacza zależność funkcyjna X → Y?", "Wartości X jednoznacznie wyznaczają wartości Y.", "Wartości Y jednoznacznie wyznaczają wartości X.", "X i Y muszą być kluczami głównymi.", "X i Y mają zawsze identyczne wartości."),
    (56, "Co oznacza opcja ON DELETE CASCADE dla klucza obcego?", "Usunięcie wiersza nadrzędnego usuwa powiązane wiersze podrzędne.", "Usunięcie wiersza podrzędnego usuwa wiersz nadrzędny.", "Usunięcie wiersza nadrzędnego ustawia klucz obcy na NULL.", "Usunięcie wiersza nadrzędnego jest zawsze blokowane."),
    (57, "Jaki warunek dotyczący wartości atrybutów wynika z pierwszej postaci normalnej?", "Każde pole zawiera wartość atomową.", "Każdy wyznacznik jest nadkluczem.", "Nie występują zależności przechodnie.", "Nie występują zależności wielowartościowe."),
    (57, "Jaki rodzaj zależności eliminuje druga postać normalna?", "Zależność atrybutu niekluczowego od części klucza kandydującego.", "Zależność przechodnią między atrybutami niekluczowymi.", "Każdą zależność między kluczem obcym a głównym.", "Każdą zależność wielowartościową."),
    (58, "Jaka jest podstawowa rola indeksu w bazie danych?", "Przyspieszanie wyszukiwania wierszy według indeksowanych wartości.", "Automatyczne tworzenie kopii zapasowej tabeli.", "Zastępowanie kluczy obcych w relacjach.", "Wykonywanie kodu po zmianie danych."),
    (58, "Czym jest wyzwalacz w bazie danych?", "Kod wykonywany automatycznie po określonym zdarzeniu.", "Zapytanie zapisane jako wirtualna tabela.", "Struktura służąca do szybszego wyszukiwania.", "Procedura uruchamiana wyłącznie ręcznie."),
    (59, "Co przedstawia encja w modelu związków encji?", "Typ obiektów, o których przechowuje się dane.", "Pojedynczą wartość klucza obcego.", "Instrukcję pobierającą dane z tabeli.", "Regułę sortowania wyników zapytania."),
    (59, "Jak w modelu relacyjnym zwykle odwzorowuje się związek jeden do wielu?", "Kluczem obcym w tabeli po stronie wielu.", "Kluczem obcym w tabeli po stronie jeden.", "Połączeniem obu tabel w jedną kolumnę.", "Usunięciem klucza głównego po stronie wielu."),
    (60, "Co jest charakterystyczne dla systemu OLTP?", "Wiele krótkich operacji na bieżących danych.", "Nieliczne analizy obejmujące duże zbiory historyczne.", "Wyłącznie odczyt danych uzupełnianych okresowo.", "Przetwarzanie tylko po zamknięciu dnia."),
    (60, "Co jest charakterystyczne dla systemu OLAP?", "Analiza i agregacja dużych zbiorów danych.", "Częsta aktualizacja pojedynczych rekordów.", "Obsługa wielu krótkich transakcji zapisu.", "Wymóg natychmiastowej aktualności każdego rekordu."),
    (61, "Co oznacza atomowość transakcji?", "Wszystkie jej operacje wykonują się albo żadna z nich.", "Każda transakcja wykonuje się równolegle z innymi.", "Dane są zawsze odczytywane w tej samej kolejności.", "Każda operacja jest trwale zapisywana przed zatwierdzeniem."),
    (61, "Czego nie dopuszcza poziom izolacji READ COMMITTED?", "Odczytu zmian, których inna transakcja jeszcze nie zatwierdziła.", "Ponownego odczytu tego samego wiersza.", "Zmiany wiersza przez inną transakcję po zatwierdzeniu.", "Odczytu danych zatwierdzonych przez inne transakcje."),
    (62, "Do czego służy instrukcja GRANT?", "Do nadawania użytkownikom uprawnień.", "Do odbierania użytkownikom uprawnień.", "Do usuwania kont użytkowników.", "Do zmiany hasła użytkownika."),
    (62, "Który mechanizm chroni dane przesyłane między klientem a bazą przed podsłuchem?", "Szyfrowanie połączenia.", "Indeksowanie tabel.", "Grupowanie wyników zapytań.", "Zmiana nazw tabel."),
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
