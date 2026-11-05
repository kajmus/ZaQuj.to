"""Seed exam categories and topics.

Revision ID: 1
Revises: 0fb079029fe7
"""

from alembic import op
import sqlalchemy as sa


revision = "1"
down_revision = "0fb079029fe7"
branch_labels = None
depends_on = None


categories = sa.table(
    "Kategoria",
    sa.column("id_category", sa.Integer),
    sa.column("name", sa.Text),
)

topics = sa.table(
    "Temat",
    sa.column("id_temat", sa.Integer),
    sa.column("name", sa.Text),
    sa.column("id_category", sa.Integer),
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
    (
        "Algorytmy i struktury danych",
        (
            "Pojęcie algorytmu.",
            "Klasyczne algorytmy:",
            "Czasowa i pamięciowa złożoność obliczeniowa algorytmu. Złożoność optymistyczna, pesymistyczna, średnia.",
            "Notacja asymptotyczna i jej znaczenie w teorii algorytmów, rzędy wielkości funkcji.",
            "Algorytmy sortowania. Dokładny opis wraz z pseudokodem, sortowania bąbelkowego, przez wstawianie oraz sortowania przez wybieranie. Zasada działania sortowania przez scalanie oraz sortowania szybkiego. Właściwości wszystkich powyższych algorytmów oraz ich złożoności czasowe.",
            "Algorytmy rekurencyjne; zapisywanie wybranych klasycznych algorytmów w postaci rekurencyjnej.",
            "Metoda dziel i zwyciężaj. Metoda równego podziału, metoda Newtona-Raphsona (stycznych).",
            "Abstrakcyjne struktury danych: stosy, kolejki FIFO, kolejki priorytetowe, słowniki - ich implementacje (np tablice, listy dowiązane, kopce, drzewa binarne, drzewa BST) oraz zastosowania.",
            "Kodowanie Huffmana.",
            "Algorytm Kruskala.",
            "Tablice z haszowaniem (asocjacyjne). Rozwiązywanie kolizji - metoda łańcuchowa i adresowanie otwarte.",
            "Szyfrowanie Cezara.",
        ),
    ),
    (
        "Programowanie",
        (
            "Budowa języków programowania i ich podział.",
            "Podstawowe typy danych, typy podzielne, literały.",
            "Metoda siłowa. Zgadnij i sprawdź. Przeszukiwanie wyczerpujące.",
            "Modularyzacja programu: podprogramy. Funkcje oraz procedury. Deklaracja i definicja funkcji. Zasady wywoływania funkcji. Komunikacja z innymi podprogramami.",
            "Dekompozycja i abstrakcja. Parametry formalne i argumenty. Parametry domyślne.",
            "Zasięg i jego funkcja. Zmienne lokalne i globalne.",
            "Stos i jego funkcja.",
            "Programowanie defensywne. Wyjątki.",
            "Testowanie oprogramowania. Testy strukturalne i funkcjonalne.",
            "Błędy i ich podział.",
            "Dziel i zwyciężaj. Rekurencja. Przypadek podstawowy i część indukcyjna. Przykłady.",
            "Programowanie zorientowane obiektowo. Obiekty i ich identyfikatory, typy, tożsamość, stan. Instancje. Funkcje klas i metody instancji. Klasy abstrakcyjne.",
            "Dziedziczenie. Hierarchia klas, klasy bazowe i pochodne.",
            "Debugowanie, usuwanie błędów.",
            "Polimorfizm. Przeciążanie operatorów. Rzutowanie.",
        ),
    ),
    (
        "Bazy danych",
        (
            "Relacyjny model danych i algebra relacji: atrybuty, dziedziny atrybutów, krotki i relacje; operacje na relacjach.",
            "Język SQL – zapytania, selekcja, sortowanie, grupowanie, funkcje agregujące, podzapytania.",
            "Instrukcje DML – usuwanie, aktualizacja i dołączanie danych.",
            "Instrukcje DDL – tworzenie tabel, modyfikacje struktury tabel, usuwanie tabel.",
            "Zależności funkcyjne. Aksjomaty Armstronga. Integralność danych (klucze, klucze obce). Opcje propagacji.",
            "Postacie normalne: 1NF, 2NF, 3NF, BCNF, 4NF. Normalizacja.",
            "Indeksy. Widoki. Procedury składowane. Wyzwalacze.",
            "Modelowanie danych: model logiczny (diagram związków encji - ERD) i model relacyjny.",
            "Systemy transakcyjne i analityczne - podstawowe różnice.",
            "Transakcje. Własności ACID. Poziomy izolacji.",
            "Administrowanie użytkownikami bazy danych i ochrona danych.",
        ),
    ),
    (
        "Elementy grafiki komputerowej",
        (
            "Modele barw w grafice komputerowej.",
            "Metody kompresji obrazów.",
            "Formaty plików graficznych.",
            "Rzutowanie.",
            "Rendering.",
            "Rasteryzacja, algorytmy rysowania prymitywów graficznych (w szczególności algorytm rysowania odcinka), antyaliasing.",
            "Generowanie sceny przy pomocy ,,śledzenia promieni”.",
            "Algorytmy eliminowania powierzchni zasłoniętych.",
            "Modele oświetlenia.",
            "Materiały, tekstury.",
        ),
    ),
    (
        "Podstawy sztucznej inteligencji",
        (
            "Rodzaje uczenia maszynowego: Uczenie nadzorowane, nienadzorowane, ze wzmocnieniem.",
            "Model Regresji logistycznej. Metoda gradientu prostego i jej znaczenie w minimalizacji funkcji kosztów.",
            "Znaczenie normalizacji danych w technikach uczenia maszynowego.",
            "Koncepcja Naiwnego Klasyfikatora Bayesa.",
            "Klasyfikator minimalno-odległościowy i algorytm k-najbliższych sąsiadów, model leniwego uczenia.",
            "Algorytm PCA w redukcji wymiarowości danych.",
            "Znaczenie i idea metody walidacji krzyżowej w metodach uczenia maszynowego.",
            "Porównanie algorytmów k-najbliższych sąsiadów (k-NN) oraz SVM (maszyny wektorów nośnych).",
            "Modele drzew decyzyjnych i lasów losowych.",
            "Model Perceptronu.",
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
    topic_id = 1
    for category_id, (_, topic_names) in enumerate(TOPICS, start=1):
        for topic_name in topic_names:
            rows.append(
                {
                    "id_temat": topic_id,
                    "name": topic_name,
                    "id_category": category_id,
                }
            )
            topic_id += 1
    op.bulk_insert(topics, rows)


def downgrade() -> None:
    connection = op.get_bind()
    connection.execute(
        topics.delete().where(
            topics.c.id_temat.in_(range(1, 1 + sum(len(items) for _, items in TOPICS)))
        )
    )
    connection.execute(
        categories.delete().where(
            categories.c.id_category.in_(range(1, 1 + len(TOPICS)))
        )
    )
