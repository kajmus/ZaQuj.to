from alembic import op
import sqlalchemy as sa


revision = "7"
down_revision = "6"
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
    (
        25,
        "W opisie procedury jeden krok brzmi: „wybierz odpowiednio duży dzielnik”, bez reguły wyboru. Którą cechę algorytmu narusza ten krok?",
        "Określoność sposobu wykonania operacji.",
        "Ogólność względem danych wejściowych.",
        "Możliwość przedstawienia kroków schematem.",
        "Uporządkowanie kolejnych operacji.",
    ),
    (
        25,
        "Co można stwierdzić o tym samym algorytmie opisanym raz pseudokodem, a raz schematem blokowym?",
        "Zmienia się forma zapisu, lecz opisane kroki mogą pozostać te same.",
        "Schemat blokowy gwarantuje zakończenie, a pseudokod tego nie robi.",
        "Pseudokod musi opisywać inną kolejność operacji niż schemat.",
        "Wybór formy zapisu przesądza o złożoności czasowej algorytmu.",
    ),
    (
        26,
        "Dlaczego przy sprawdzaniu, czy liczba naturalna n > 1 jest pierwsza, wystarczy badać możliwe dzielniki nie większe od √n?",
        "Liczba złożona ma dzielnik od 2 do √n.",
        "Każdy dzielnik liczby złożonej leży w tym zakresie.",
        "Pierwiastek każdej liczby złożonej jest jej dzielnikiem.",
        "Liczby większe od pierwiastka nie mogą być dzielnikami.",
    ),
    (
        26,
        "Co pozwala odrzucić połowę elementów po porównaniu ze środkiem w wyszukiwaniu binarnym?",
        "Uporządkowanie danych według używanej relacji porównania.",
        "Brak powtarzających się wartości w przeszukiwanym zbiorze.",
        "Parzysta liczba elementów w każdym badanym zakresie.",
        "Równe odstępy między sąsiednimi wartościami.",
    ),
    (
        27,
        "Dwa algorytmy rozwiązują ten sam problem i wykonują podobną liczbę operacji. Co można stwierdzić o ich złożoności pamięciowej?",
        "Może być różna, jeśli przechowują różną ilość danych pośrednich.",
        "Musi być taka sama, bo wykonują podobną liczbę operacji.",
        "Musi być taka sama, bo rozwiązują ten sam problem.",
        "Zależy wyłącznie od długości ich kodu źródłowego.",
    ),
    (
        27,
        "Jak określa się pesymistyczny czas działania algorytmu dla wejść o ustalonym rozmiarze?",
        "Bierze się największy czas spośród dopuszczalnych wejść.",
        "Bierze się najmniejszy czas spośród dopuszczalnych wejść.",
        "Bierze się średni czas spośród dopuszczalnych wejść.",
        "Mierzy się wykonanie na najwolniejszym komputerze.",
    ),
    (
        28,
        "Co odróżnia zapis Θ(f(n)) od O(f(n)) w opisie wzrostu funkcji?",
        "Θ wymaga granicy od góry i od dołu, O tylko od góry.",
        "Θ oznacza jedynie dolną granicę, a O dokładną wartość.",
        "Θ opisuje pamięć, a O wyłącznie czas działania.",
        "Θ dotyczy małych danych, a O dużych danych.",
    ),
    (
        28,
        "Co wolno wywnioskować z samego stwierdzenia, że czas T(n) należy do O(f(n))?",
        "f(n) ogranicza T(n) od góry, lecz T(n) może rosnąć wolniej.",
        "T(n) musi mieć dokładnie ten sam rząd wzrostu co f(n).",
        "f(n) ogranicza T(n) od dołu dla dużych danych.",
        "T(n) jest równe f(n) dla każdego rozmiaru wejścia.",
    ),
    (
        29,
        "Dlaczego sortowanie przez wstawianie bywa korzystne dla danych prawie uporządkowanych w porównaniu z sortowaniem przez wybieranie?",
        "Zwykle wymaga niewielu przesunięć, a wybieranie nadal szuka minimum.",
        "Zawsze dzieli dane na połowy, a wybieranie używa pivota.",
        "Nie porównuje elementów, gdy tablica jest częściowo uporządkowana.",
        "Ma stałą złożoność czasową niezależnie od układu danych.",
    ),
    (
        29,
        "Które stwierdzenie poprawnie odróżnia sortowanie przez scalanie od sortowania szybkiego?",
        "Scalanie łączy posortowane części; szybkie dzieli względem pivota.",
        "Scalanie dzieli względem pivota; szybkie łączy posortowane części.",
        "Oba zawsze dzielą tablicę na części o identycznej liczbie elementów.",
        "Oba wybierają minimum z pozostałych elementów w każdym kroku.",
    ),
    (
        30,
        "Dlaczego sama obecność przypadku podstawowego w funkcji rekurencyjnej nie wystarcza do zagwarantowania zakończenia?",
        "Kolejne wywołania muszą jeszcze zbliżać się do tego przypadku.",
        "Każde wywołanie musi wykonywać się w stałym czasie.",
        "Przypadek podstawowy musi być zapisany poza funkcją.",
        "Funkcja musi zwracać wyłącznie liczby naturalne.",
    ),
    (
        30,
        "Co pozostaje niezmienne przy rekurencyjnym zastąpieniu pary argumentów (a, b), gdzie a ≠ 0, przez (b mod a, a) w algorytmie Euklidesa?",
        "Największy wspólny dzielnik.",
        "Suma obu argumentów.",
        "Wartość pierwszego argumentu.",
        "Reszta z dzielenia obu argumentów.",
    ),
    (
        31,
        "Jakie warunki uzasadniają użycie bisekcji do znalezienia miejsca zerowego funkcji w przedziale [a, b]?",
        "Ciągłość funkcji oraz przeciwne znaki na końcach przedziału.",
        "Stały znak pochodnej oraz równe wartości na końcach.",
        "Brak pochodnej oraz dodatnie wartości na obu końcach.",
        "Dwa znane miejsca zerowe leżące poza przedziałem.",
    ),
    (
        31,
        "Jak metoda Newtona wyznacza następne przybliżenie miejsca zerowego, w odróżnieniu od bisekcji?",
        "Jako punkt przecięcia stycznej do wykresu z osią x.",
        "Jako środek przedziału o wartościach przeciwnych znaków.",
        "Jako średnią wszystkich wcześniejszych przybliżeń.",
        "Jako punkt o najmniejszej wartości funkcji w przedziale.",
    ),
    (
        32,
        "Kolejkę priorytetową zaimplementowano kopcem zamiast listą. Co powinno pozostać takie samo z punktu widzenia użytkownika struktury?",
        "Kolejny element wybiera się według priorytetu.",
        "Czas wykonania każdej operacji na strukturze.",
        "Fizyczne ułożenie elementów w pamięci.",
        "Pobieranie elementów w kolejności ich dodania.",
    ),
    (
        32,
        "Dlaczego w drzewie BST przy szukaniu klucza mniejszego od klucza bieżącego węzła można pominąć jego prawe poddrzewo?",
        "Są w nim klucze nie mniejsze od klucza bieżącego węzła.",
        "Jest ono zawsze puste, gdy lewe poddrzewo nie jest puste.",
        "Ma ono zawsze większą głębokość niż lewe poddrzewo.",
        "Zawiera ono wyłącznie duplikaty klucza bieżącego węzła.",
    ),
    (
        33,
        "Jaką decyzję powtarza się przy budowie drzewa kodowania Huffmana?",
        "Łączy się dwa drzewa o najmniejszych sumach częstości symboli.",
        "Łączy się dwa drzewa o największych sumach częstości symboli.",
        "Łączy się symbole sąsiadujące ze sobą w kodowanym tekście.",
        "Łączy się wyłącznie drzewa o identycznych częstościach.",
    ),
    (
        33,
        "Co pozwala dekodować ciąg kodów Huffmana bez separatorów między kolejnymi symbolami?",
        "Żaden kod symbolu nie jest prefiksem kodu innego symbolu.",
        "Każdy symbol otrzymuje kod o jednakowej liczbie bitów.",
        "Kody wszystkich symboli kończą się tym samym bitem.",
        "Każdy znak wiadomości otrzymuje osobne drzewo kodowe.",
    ),
    (
        34,
        "Które dwie reguły decydują o dodaniu krawędzi w algorytmie Kruskala?",
        "Rosnąca kolejność wag oraz odrzucanie krawędzi tworzących cykl.",
        "Rosnąca kolejność wag oraz dodawanie każdej rozważanej krawędzi.",
        "Malejąca kolejność wag oraz odrzucanie krawędzi tworzących cykl.",
        "Kolejność wierzchołków oraz wybór krawędzi o największej wadze.",
    ),
    (
        34,
        "Jaki warunek dotyczący grafu jest konieczny, aby algorytm Kruskala mógł zbudować jedno drzewo rozpinające wszystkie wierzchołki?",
        "Graf musi być spójny.",
        "Wagi krawędzi muszą być różne.",
        "Każdy wierzchołek musi mieć taki sam stopień.",
        "Liczba krawędzi musi być parzysta.",
    ),
    (
        35,
        "Jak zwykle różnią się metoda łańcuchowa i adresowanie otwarte przy obsłudze dwóch kluczy o tym samym wyniku funkcji mieszającej?",
        "Łańcuchowa używa listy; otwarte szuka innej komórki tablicy.",
        "Łańcuchowa szuka innej wolnej komórki tablicy; otwarte używa listy.",
        "Obie metody zastępują wcześniej zapisany klucz nowym.",
        "Obie metody wymagają zmiany funkcji mieszającej.",
    ),
    (
        35,
        "Co odróżnia mieszanie podwójne od sondowania liniowego przy rozwiązywaniu kolizji?",
        "Krok prób zależy także od drugiej funkcji mieszającej klucz.",
        "Odstęp między próbami jest taki sam dla wszystkich kluczy.",
        "Klucze z kolizją przechowuje się na liście przy indeksie.",
        "Kolejne próby nie korzystają z wartości funkcji mieszającej.",
    ),
    (
        36,
        "Dlaczego szyfr Cezara jest szyfrem monoalfabetycznym?",
        "Przy stałym kluczu każda litera ma zawsze ten sam zamiennik.",
        "Każda pozycja w wiadomości używa innego przesunięcia alfabetu.",
        "Każde słowo w wiadomości otrzymuje własny alfabet podstawienia.",
        "Litery są zamieniane na znaki zależnie od ich częstości w tekście.",
    ),
    (
        36,
        "Która cecha układu liter pozostaje zachowana po zastosowaniu szyfru Cezara ze stałym przesunięciem?",
        "Wzór powtórzeń liter na poszczególnych pozycjach.",
        "Częstość występowania każdej konkretnej litery alfabetu.",
        "Tożsamość litery na każdej pozycji tekstu.",
        "Położenie liter względem początku alfabetu.",
    ),
)


def upgrade() -> None:
    op.bulk_insert(
        questions,
        [
            dict(
                zip(
                    (
                        "id_temat",
                        "text",
                        "correct_answer",
                        "wrong_answer_1",
                        "wrong_answer_2",
                        "wrong_answer_3",
                    ),
                    row,
                )
            )
            for row in QUESTIONS
        ],
    )


def downgrade() -> None:
    connection = op.get_bind()
    for topic_id, text, correct_answer, *_ in QUESTIONS:
        connection.execute(
            questions.delete().where(
                sa.and_(
                    questions.c.id_temat == topic_id,
                    questions.c.text == text,
                    questions.c.correct_answer == correct_answer,
                )
            )
        )
