"""Add two ABCD questions for each artificial intelligence topic.

Revision ID: 12
Revises: 11
"""

from alembic import op
import sqlalchemy as sa


revision = "12"
down_revision = "11"
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
        73,
        "Czym różni się uczenie nadzorowane od uczenia nienadzorowanego w kontekście danych treningowych?",
        "Uczenie nadzorowane wykorzystuje zbiór danych zawierający etykiety (wartości docelowe), natomiast uczenie nienadzorowane operuje na danych nieetykietowanych w celu wykrycia ich ukrytej struktury.",
        "Uczenie nadzorowane służy wyłącznie do redukcji wymiarowości, a uczenie nienadzorowane wyłącznie do klasyfikacji binarnej.",
        "Uczenie nienadzorowane wymaga interakcji agenta ze środowiskiem i systemu nagród, w przeciwieństwie do uczenia nadzorowanego.",
        "Uczenie nadzorowane nie wymaga podziału na zbiór treningowy i testowy, ponieważ etykiety gwarantują brak przeuczenia.",
    ),
    (
        73,
        "Na czym polega główna idea uczenia ze wzmocnieniem (Reinforcement Learning)?",
        "Agent uczy się optymalnej polityki działania poprzez interakcję ze środowiskiem, maksymalizując skumulowaną nagrodę otrzymywaną za podejmowane akcje.",
        "Model uczy się na podstawie statycznego zbioru danych, minimalizując błąd średniokwadratowy względem znanych etykiet.",
        "Algorytm grupuje obiekty o podobnych cechach w rozłączne klastry bez udziału funkcji celu.",
        "System wykorzystuje wyłącznie drzewa decyzyjne do przewidywania wartości ciągłych w szeregach czasowych.",
    ),
    (
        74,
        "Jaką rolę pełni funkcja sigmoidalna (logistyczna) w modelu regresji logistycznej?",
        "Przekształca liniową kombinację cech na wartość z przedziału od 0 do 1, którą można interpretować jako prawdopodobieństwo przynależności do klasy pozytywnej.",
        "Służy do eliminacji cech skorelowanych przed rozpoczęciem procesu uczenia modelu.",
        "Zamienia problem klasyfikacji binarnej na problem klasteryzacji hierarchicznej.",
        "Gwarantuje, że funkcja kosztu staje się funkcją liniową względem wag modelu.",
    ),
    (
        74,
        "Jakie jest znaczenie współczynnika uczenia (learning rate) w metodzie gradientu prostego (Gradient Descent)?",
        "Określa rozmiar kroku w kierunku przeciwnym do gradientu funkcji kosztu; zbyt duży może prowadzić do rozbieżności, a zbyt mały do bardzo wolnej zbieżności.",
        "Definiuje maksymalną liczbę cech, które mogą zostać użyte w procesie minimalizacji funkcji kosztu.",
        "Wyznacza liczbę warstw ukrytych wymaganych do osiągnięcia minimum globalnego.",
        "Służy do losowego zerowania wag modelu po każdej epoce w celu przyspieszenia obliczeń.",
    ),
    (
        75,
        "Dlaczego normalizacja lub standaryzacja danych jest kluczowa dla algorytmów takich jak k-NN, SVM czy sieci neuronowe z gradientem prostym?",
        "Zapobiega dominacji cech o dużych zakresach wartości nad cechami o małych zakresach w obliczeniach odległości oraz przyspiesza zbieżność metod gradientowych.",
        "Automatycznie usuwa wszystkie wartości odstające (outliery) ze zbioru treningowego.",
        "Zwiększa wymiarowość przestrzeni cech, co ułatwia liniową separowalność klas.",
        "Eliminuje całkowicie potrzebę stosowania walidacji krzyżowej podczas oceny modelu.",
    ),
    (
        75,
        "Czym różni się standaryzacja (Z-score) od normalizacji Min-Max?",
        "Standaryzacja przekształca dane tak, aby miały średnią równą 0 i odchylenie standardowe równe 1, natomiast normalizacja Min-Max skaluje wartości do zadanego przedziału (najczęściej [0, 1]).",
        "Standaryzacja skaluje dane wyłącznie do przedziału [0, 1], a normalizacja Min-Max wymaga, aby dane miały rozkład normalny.",
        "Normalizacja Min-Max jest całkowicie odporna na wartości odstające, natomiast standaryzacja zawsze obcina wartości powyżej 1.",
        "Standaryzację stosuje się wyłącznie do zmiennych kategorycznych, a normalizację Min-Max wyłącznie do zmiennych tekstowych.",
    ),
    (
        76,
        "Skąd wynika określenie „naiwny” w nazwie Naiwnego Klasyfikatora Bayesa?",
        "Z założenia o warunkowej niezależności wszystkich cech opisujących obiekt pod warunkiem znajomości jego klasy.",
        "Z faktu, że klasyfikator ten nie wykorzystuje twierdzenia Bayesa do obliczania prawdopodobieństwa a posteriori.",
        "Z założenia, że wszystkie klasy w zbiorze danych występują zawsze z dokładnie takim samym prawdopodobieństwem a priori.",
        "Z braku możliwości obsługi więcej niż dwóch klas decyzyjnych jednocześnie.",
    ),
    (
        76,
        "Jaki problem rozwiązuje wygładzanie Laplace’a (Laplace smoothing) w Naiwnym Klasyfikatorze Bayesa?",
        "Zapobiega zerowaniu się całego iloczynu prawdopodobieństw warunkowych, gdy dana wartość cechy nie wystąpiła w zbiorze treningowym dla określonej klasy.",
        "Eliminuje problem współliniowości cech poprzez redukcję ich liczby przed treningiem.",
        "Przekształca rozkład dyskretny cech na rozkład normalny o wariancji równej 1.",
        "Zmniejsza złożoność obliczeniową klasyfikatora z kwadratowej na logarytmiczną.",
    ),
    (
        77,
        "Dlaczego algorytm k-najbliższych sąsiadów (k-NN) nazywany jest modelem leniwego uczenia (lazy learning)?",
        "Ponieważ nie buduje jawnego modelu podczas fazy treningu, lecz jedynie zapamiętuje zbiór uczący, a właściwe obliczenia wykonuje dopiero w momencie klasyfikacji nowego obiektu.",
        "Ponieważ wykorzystuje metodę gradientu prostego z bardzo małym współczynnikiem uczenia.",
        "Ponieważ losowo odrzuca połowę danych treningowych w celu skrócenia czasu działania.",
        "Ponieważ wymaga wielokrotnego przetrenowania przed każdą pojedynczą predykcją.",
    ),
    (
        77,
        "Czym różni się klasyfikator minimalno-odległościowy (NM – Nearest Mean) od algorytmu k-NN?",
        "Klasyfikator minimalno-odległościowy przypisuje nowy obiekt do klasy o najbliższym centroidzie (średniej klasy), natomiast k-NN szuka k najbliższych pojedynczych obiektów ze zbioru treningowego.",
        "Klasyfikator minimalno-odległościowy zawsze wymaga obliczenia odległości do wszystkich próbek treningowych, a k-NN tylko do wektorów nośnych.",
        "Klasyfikator minimalno-odległościowy działa wyłącznie dla danych tekstowych, podczas gdy k-NN wyłącznie dla obrazów.",
        "Algorytm k-NN nie zależy od wybranej metryki odległości, w przeciwieństwie do klasyfikatora minimalno-odległościowego.",
    ),
    (
        78,
        "Jaki jest główny cel algorytmu PCA (Analiza Głównych Składowych) w redukcji wymiarowości danych?",
        "Znalezienie nowego zbioru wzajemnie ortogonalnych zmiennych (głównych składowych), które maksymalizują zachowaną wariancję danych przy jednoczesnym zmniejszeniu liczby wymiarów.",
        "Wybór podzbioru oryginalnych cech, które mają najwyższą korelację z etykietą klasy w uczeniu nadzorowanym.",
        "Podział zbioru danych na k rozłącznych klastrów poprzez minimalizację odległości wewnątrzklastrowych.",
        "Zwiększenie liczby cech poprzez dodanie ich kombinacji wielomianowych w celu poprawy dokładności klasyfikacji.",
    ),
    (
        78,
        "Jakie obiekty matematyczne wyznacza się na podstawie macierzy kowariancji danych w algorytmie PCA?",
        "Wektory własne (wyznaczające kierunki głównych składowych) oraz odpowiadające im wartości własne (określające wielkość wariancji wzdłuż tych kierunków).",
        "Pochodne cząstkowe funkcji kosztu entropii krzyżowej względem wag sieci.",
        "Macierz pomyłek (confusion matrix) dla wszystkich par klas decyzyjnych.",
        "Współczynniki regresji liniowej metodą najmniejszych kwadratów.",
    ),
    (
        79,
        "Na czym polega metoda k-krotnej walidacji krzyżowej (k-fold cross-validation)?",
        "Na podziale zbioru danych na k rozłącznych podzbiorów, a następnie k-krotnym trenowaniu modelu na k-1 podzbiorach i testowaniu na pozostałym jednym, uśredniając końcowy wynik.",
        "Na jednokrotnym losowym podziale danych na zbiór treningowy (80%) i testowy (20%) oraz k-krotnym uruchomieniu tego samego treningu.",
        "Na trenowaniu k różnych algorytmów uczenia maszynowego na całym zbiorze danych bez wydzielania zbioru testowego.",
        "Na usuwaniu k najgorszych próbek ze zbioru danych w każdej iteracji uczenia.",
    ),
    (
        79,
        "Jaki jest główny cel stosowania walidacji krzyżowej w uczeniu maszynowym?",
        "Uzyskanie bardziej wiarygodnej oceny zdolności generalizacji modelu oraz wykrycie przeuczenia (overfittingu), szczególnie przy ograniczonej liczbie danych.",
        "Bezpośrednie przyspieszenie procesu treningu modelu o czynnik równy liczbie podzbiorów k.",
        "Automatyczne zbalansowanie klas w zbiorze danych poprzez generowanie syntetycznych próbek.",
        "Zastąpienie funkcji kosztu w procesie optymalizacji wag sieci neuronowej.",
    ),
    (
        80,
        "Czym różni się podejście algorytmu SVM (Maszyny Wektorów Nośnych) od algorytmu k-NN w fazie predykcji?",
        "SVM wyznacza podczas treningu hiperpłaszczyznę rozdzielającą o maksymalnym marginesie i w predykcji korzysta tylko z wektorów nośnych, podczas gdy k-NN musi obliczać odległość do wszystkich punktów treningowych.",
        "SVM wymaga zapamiętania całego zbioru treningowego, natomiast k-NN redukuje zbiór danych do kilku parametrów wagowych.",
        "k-NN wykorzystuje tzw. sztuczkę jądrową (kernel trick) do rzutowania danych w przestrzeń wyższego wymiaru, czego nie potrafi SVM.",
        "SVM służy wyłącznie do uczenia nienadzorowanego, podczas gdy k-NN wyłącznie do uczenia nadzorowanego.",
    ),
    (
        80,
        "Jaką rolę pełni tzw. sztuczka jądrowa (kernel trick) w algorytmie SVM?",
        "Pozwala na znalezienie nieliniowej granicy decyzyjnej poprzez niejawne odwzorowanie danych do przestrzeni cech o wyższym wymiarze bez konieczności jawnego obliczania współrzędnych w tej przestrzeni.",
        "Służy do automatycznego doboru optymalnej liczby sąsiadów k w przestrzeni euklidesowej.",
        "Zmniejsza liczbę wymiarów danych wejściowych w sposób identyczny jak algorytm PCA.",
        "Eliminuje wszystkie wektory nośne, które leżą wewnątrz marginesu bezpieczeństwa.",
    ),
    (
        81,
        "Jakie kryteria są najczęściej stosowane do wyboru najlepszego podziału w węzłach drzewa decyzyjnego dla problemu klasyfikacji?",
        "Zysk informacyjny (oparty na entropii) oraz indeks Giniego (Gini impurity).",
        "Błąd średniokwadratowy (MSE) oraz współczynnik determinacji R2.",
        "Odległość Mahalanobisa oraz podobieństwo cosinusowe.",
        "Wartość funkcji sigmoidalnej oraz współczynnik korelacji Pearsona.",
    ),
    (
        81,
        "W jaki sposób las losowy (Random Forest) redukuje problem przeuczenia (wysokiej wariancji) typowy dla pojedynczego drzewa decyzyjnego?",
        "Łączy predykcje wielu drzew trenowanych na losowych próbkach bootstrapowych (bagging) oraz losowych podzbiorach cech w każdym węźle, co zmniejsza korelację między drzewami.",
        "Przycinając wszystkie drzewa w lesie do głębokości dokładnie jednego poziomu (stumps) i stosując zawsze ten sam zestaw cech.",
        "Zastępując wszystkie węzły decyzyjne modelami regresji liniowej.",
        "Trenując kolejne drzewa wyłącznie na tych samych danych bez żadnego elementu losowości.",
    ),
    (
        82,
        "Jakie jest główne ograniczenie pojedynczego perceptronu (jednowarstwowego)?",
        "Potrafi poprawnie sklasyfikować wyłącznie zbiory danych, które są liniowo separowalne (nie radzi sobie np. z funkcją logiczną XOR).",
        "Nie potrafi przetwarzać danych wejściowych o wartościach rzeczywistych, a jedynie wartości binarne.",
        "Wymaga zastosowania algorytmu wstecznej propagacji błędu (backpropagation) przez wiele warstw ukrytych.",
        "Zawsze zbiega do rozwiązania optymalnego w dokładnie jednej iteracji, niezależnie od danych.",
    ),
    (
        82,
        "W jaki sposób obliczane jest wyjście klasycznego perceptronu Rosenblatta?",
        "Jako wynik zastosowania progowej (skokowej) funkcji aktywacji na sumie ważonej sygnałów wejściowych powiększonej o wyraz wolny (bias).",
        "Jako średnia arytmetyczna wszystkich cech wejściowych bez użycia jakichkolwiek wag.",
        "Jako iloczyn wszystkich cech wejściowych poddany działaniu funkcji softmax.",
        "Jako odległość euklidesowa wektora wejściowego od wektora wag.",
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