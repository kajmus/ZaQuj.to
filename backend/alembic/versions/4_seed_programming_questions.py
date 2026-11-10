"""Add two ABCD questions for each programming topic.

Revision ID: 4
Revises: 3
"""

from alembic import op
import sqlalchemy as sa


revision = "4"
down_revision = "3"
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
    (37, "Czym różni się składnia języka programowania od jego semantyki?", "Składnia określa poprawną budowę programu, a semantyka jego znaczenie.", "Składnia określa znaczenie programu, a semantyka jego budowę.", "Składnia opisuje typy danych, a semantyka tylko biblioteki.", "Składnia dotyczy kompilacji, a semantyka wyłącznie interpretacji."),
    (37, "Czym charakteryzuje się programowanie deklaratywne?", "Opisuje oczekiwany wynik bez szczegółowego wskazywania kolejnych kroków.", "Opisuje wyłącznie ciąg instrukcji zmieniających stan programu.", "Wymaga zapisu programu bezpośrednio w kodzie maszynowym.", "Wymaga tworzenia klas dla każdego typu danych."),
    (38, "Czym jest literał w kodzie źródłowym?", "Bezpośrednim zapisem określonej wartości.", "Nazwą zmiennej przechowującej wartość.", "Deklaracją nowego typu danych.", "Adresem funkcji w pamięci."),
    (38, "Co odróżnia unię od struktury danych z osobną pamięcią dla każdego pola?", "Pola unii współdzielą ten sam obszar pamięci.", "Unia może zawierać tylko pola liczbowe.", "Wszystkie pola unii muszą mieć ten sam typ.", "Unia nie może mieć więcej niż jednego pola."),
    (39, "Na czym polega przeszukiwanie wyczerpujące?", "Na sprawdzeniu wszystkich rozważanych kandydatów na rozwiązanie.", "Na wybraniu pierwszego kandydata bez sprawdzania warunków.", "Na podziale problemu na niezależne funkcje.", "Na obliczeniu wyniku bez analizowania kandydatów."),
    (39, "Co jest wspólną cechą metod siłowych?", "Opierają się na systematycznym sprawdzaniu możliwości zamiast wykorzystania szczególnej własności problemu.", "Zawsze mają liniową złożoność czasową.", "Zawsze znajdują wynik bez sprawdzania warunków zadania.", "Wymagają użycia rekurencji i stosu wywołań."),
    (40, "Czym jest podprogram?", "Wydzieloną częścią programu, którą można wywołać do wykonania określonego zadania.", "Zmienną dostępną w całym programie.", "Plikiem zawierającym wyłącznie dane wejściowe.", "Instrukcją kończącą działanie programu."),
    (40, "Czym różni się deklaracja funkcji od jej definicji?", "Deklaracja podaje jej interfejs, a definicja zawiera implementację.", "Deklaracja zawiera implementację, a definicja tylko nazwę.", "Deklaracja wykonuje funkcję, a definicja zwraca jej wynik.", "Deklaracja dotyczy procedur, a definicja wyłącznie funkcji."),
    (41, "Na czym polega dekompozycja problemu?", "Na podziale problemu na mniejsze części możliwe do osobnego opracowania.", "Na ukrywaniu wszystkich danych przed programistą.", "Na zamianie parametrów formalnych na argumenty.", "Na wykonywaniu wszystkich operacji w jednej funkcji."),
    (41, "Czym jest parametr domyślny funkcji?", "Parametrem z wartością używaną, gdy wywołanie nie poda dla niego argumentu.", "Parametrem, którego wartość zawsze musi zostać podana przy wywołaniu.", "Argumentem zwracanym przez każdą funkcję.", "Zmienną globalną widoczną w każdej funkcji."),
    (42, "Co określa zasięg nazwy zmiennej?", "Obszar programu, w którym można odwoływać się do tej nazwy.", "Wyłącznie czas wykonywania całego programu.", "Liczbę wartości, które może przyjąć zmienna.", "Rozmiar pamięci zajmowanej przez zmienną."),
    (42, "Czym zwykle różni się zmienna lokalna od globalnej?", "Lokalna jest dostępna w określonym bloku, a globalna w szerszym zakresie programu.", "Lokalna zawsze jest stała, a globalna zawsze zmienna.", "Lokalna ma zawsze typ liczbowy, a globalna tekstowy.", "Lokalna jest współdzielona przez wszystkie funkcje, a globalna przez jedną."),
    (43, "Jaką zasadę dostępu do elementów stosu opisuje skrót LIFO?", "Ostatni dodany element jest pobierany jako pierwszy.", "Pierwszy dodany element jest pobierany jako pierwszy.", "Elementy są pobierane według wartości klucza.", "Elementy są pobierane w losowej kolejności."),
    (43, "Co zwykle przechowuje ramka stosu wywołania funkcji?", "Dane potrzebne do wykonania i powrotu z tego wywołania.", "Wszystkie pliki otwarte przez system operacyjny.", "Wyłącznie kod maszynowy całego programu.", "Trwałą kopię wszystkich zmiennych globalnych."),
    (44, "Na czym polega programowanie defensywne?", "Na uwzględnianiu niepoprawnych danych i nieoczekiwanych warunków działania.", "Na pomijaniu obsługi błędów w celu uproszczenia kodu.", "Na zakładaniu, że dane wejściowe zawsze są poprawne.", "Na zastąpieniu testów przez komentarze w kodzie."),
    (44, "Do czego służy mechanizm wyjątków?", "Do przekazania sterowania do obsługi sytuacji wyjątkowej.", "Do deklarowania wartości domyślnych parametrów.", "Do przyspieszenia każdego wywołania funkcji.", "Do zapewnienia poprawności składni programu."),
    (45, "Na czym opierają się testy strukturalne?", "Na znajomości wewnętrznej budowy programu i ścieżek jego wykonania.", "Wyłącznie na wymaganiach użytkownika bez wglądu w kod.", "Wyłącznie na analizie wyglądu interfejsu.", "Na pomiarze szybkości sieci zamiast działania programu."),
    (45, "Co sprawdzają testy funkcjonalne?", "Czy program spełnia wymagania określone dla jego zachowania.", "Czy wykonano każdą instrukcję kodu co najmniej raz.", "Czy kod ma określoną liczbę funkcji.", "Czy program używa wskazanego algorytmu wewnętrznego."),
    (46, "Czym jest błąd składniowy?", "Naruszeniem reguł budowy poprawnych instrukcji języka.", "Zwróceniem poprawnie obliczonego, lecz nieoczekiwanego wyniku.", "Przekroczeniem dostępnej pamięci podczas działania.", "Niespełnieniem wymagania mimo poprawnego działania kodu."),
    (46, "Czym charakteryzuje się błąd logiczny?", "Program może się wykonać, ale daje wynik niezgodny z zamierzeniem.", "Kod nie przechodzi analizy składniowej.", "W kodzie występuje znak spoza alfabetu języka.", "Program zawsze kończy się wyjątkiem przed pierwszą instrukcją."),
    (47, "Na czym polega metoda dziel i zwyciężaj?", "Na podziale problemu na mniejsze podproblemy i połączeniu ich rozwiązań.", "Na sprawdzeniu wszystkich możliwych wyników bez podziału problemu.", "Na zastąpieniu każdej funkcji jedną pętlą.", "Na pominięciu rozwiązania najmniejszych podproblemów."),
    (47, "Jaką rolę pełni przypadek podstawowy w rekurencji?", "Kończy dany ciąg wywołań rekurencyjnych.", "Rozpoczyna każde kolejne wywołanie bez warunku stopu.", "Przechowuje wszystkie zmienne globalne.", "Łączy wyniki niezależnych procesów."),
    (48, "Czym jest instancja klasy?", "Konkretnym obiektem utworzonym według definicji klasy.", "Definicją wszystkich klas w programie.", "Nazwą metody statycznej.", "Typem wyjątku zgłaszanego przez klasę."),
    (48, "Czym charakteryzuje się klasa abstrakcyjna?", "Stanowi wzorzec dla klas pochodnych i nie tworzy się bezpośrednio jej instancji.", "Nie może zawierać żadnych metod.", "Zawsze jest klasą bez pól i stanu.", "Może istnieć tylko jako pojedynczy obiekt."),
    (49, "Co oznacza dziedziczenie między klasami?", "Klasa pochodna przejmuje dostępne cechy i zachowania klasy bazowej.", "Klasa bazowa powstaje jako instancja klasy pochodnej.", "Obie klasy muszą mieć identyczne implementacje wszystkich metod.", "Klasa pochodna traci możliwość dodawania własnych pól."),
    (49, "Czym jest nadpisanie metody w klasie pochodnej?", "Dostarczeniem własnej implementacji metody odziedziczonej z klasy bazowej.", "Usunięciem definicji klasy bazowej z programu.", "Wywołaniem tej samej metody kilka razy.", "Zmianą nazwy metody bez zmiany jej działania."),
    (50, "Na czym polega debugowanie programu?", "Na ustalaniu przyczyn błędów i ich usuwaniu.", "Na samym uruchomieniu kompilatora bez analizy wyniku.", "Na zastąpieniu testów dokumentacją.", "Na usuwaniu wszystkich komunikatów o błędach."),
    (50, "Do czego służy punkt przerwania w debuggerze?", "Do zatrzymania wykonywania programu w wybranym miejscu i zbadania jego stanu.", "Do trwałego zakończenia programu przy każdym uruchomieniu.", "Do automatycznego poprawienia błędu składniowego.", "Do pominięcia wszystkich testów jednostkowych."),
    (51, "Na czym polega polimorfizm w programowaniu obiektowym?", "Na użyciu wspólnego interfejsu do pracy z obiektami różnych klas.", "Na zakazie nadpisywania metod w klasach pochodnych.", "Na przechowywaniu każdego obiektu wyłącznie jako tekstu.", "Na tworzeniu jednej instancji dla wszystkich klas."),
    (51, "Czym jest przeciążanie operatorów?", "Nadaniem operatorowi działania dla określonych typów obiektów.", "Wykonaniem operatora wielokrotnie w jednej instrukcji.", "Zamianą każdego operatora na funkcję rekurencyjną.", "Automatyczną konwersją wszystkich wartości na jeden typ."),
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
