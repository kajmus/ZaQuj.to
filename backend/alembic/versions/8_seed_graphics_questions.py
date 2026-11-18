from alembic import op
import sqlalchemy as sa


revision = "8"
down_revision = "7"
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
        63,
        "Które zestawienie poprawnie opisuje sposób mieszania barw w RGB i CMY?",
        "RGB dodaje światło, a CMY odejmuje część światła przez barwniki.",
        "RGB odejmuje światło, a CMY dodaje światło emitowane przez piksele.",
        "Oba modele dodają światło, lecz używają innych barw podstawowych.",
        "Oba modele odejmują światło, lecz RGB ma więcej składowych.",
    ),
    (
        63,
        "Co odróżnia opis barwy w HSV od opisu w RGB?",
        "HSV opisuje odcień, nasycenie i jasność; RGB natężenia trzech barw.",
        "HSV opisuje natężenia trzech barw; RGB odcień, nasycenie i jasność.",
        "Oba opisują wyłącznie ilość barwników użytych podczas druku.",
        "Oba opisują wyłącznie jasność światła bez jego barwy.",
    ),
    (
        64,
        "Jaka jest istotna różnica między kompresją bezstratną a stratną obrazu?",
        "Bezstratna odtwarza identyczne dane, stratna może je trwale zmienić.",
        "Bezstratna usuwa szczegóły, stratna zachowuje każdy bit obrazu.",
        "Bezstratna działa tylko na wektorach, stratna tylko na pikselach.",
        "Bezstratna zawsze daje mniejszy plik od kompresji stratnej.",
    ),
    (
        64,
        "Dlaczego kompresja stratna może ograniczać ilość danych bez jednakowo zauważalnej utraty jakości obrazu?",
        "Pomija informacje mniej istotne dla ludzkiego postrzegania obrazu.",
        "Usuwa wyłącznie metadane, bez zmiany reprezentacji obrazu.",
        "Zachowuje wszystkie próbki obrazu, lecz zmienia ich kolejność.",
        "Zwiększa rozdzielczość, aby ukryć utracone szczegóły.",
    ),
    (
        65,
        "Dlaczego wektorowe logo zapisane w SVG można powiększać bez utraty ostrości lepiej niż rastrowy zapis w JPEG?",
        "Opisuje kształty geometrycznie, a nie jako ustaloną siatkę pikseli.",
        "Zapisuje więcej pikseli niż JPEG niezależnie od wielkości obrazu.",
        "Używa kompresji stratnej, która wyostrza krawędzie po powiększeniu.",
        "Przechowuje wyłącznie barwy czarną i białą, więc nie traci jakości.",
    ),
    (
        65,
        "Dlaczego samo rozszerzenie TIFF nie wystarcza, by ocenić, czy zapis obrazu był bezstratny?",
        "Format dopuszcza zarówno kompresję bezstratną, jak i stratną.",
        "Każdy plik TIFF zawiera dwie równoległe wersje obrazu.",
        "TIFF zawsze zapisuje obraz bez żadnej formy kompresji.",
        "TIFF jest formatem wektorowym, więc nie zapisuje pikseli.",
    ),
    (
        66,
        "Dlaczego rzut perspektywiczny zwykle daje obraz bliższy widzeniu człowieka niż rzut równoległy?",
        "Uwzględnia zmianę pozornego rozmiaru obiektu wraz z odległością.",
        "Zachowuje równoległość wszystkich odcinków sceny na obrazie.",
        "Zapewnia każdemu obiektowi ten sam rozmiar niezależnie od głębi.",
        "Pomija położenie obserwatora przy wyznaczaniu obrazu.",
    ),
    (
        66,
        "Która własność jest charakterystyczna dla rzutu równoległego?",
        "Odcinki równoległe w scenie pozostają równoległe na obrazie.",
        "Pozorny rozmiar obiektu maleje wraz z odległością od obserwatora.",
        "Wszystkie promienie rzutujące zbiegają się w punkcie obserwatora.",
        "Odległe powierzchnie są automatycznie usuwane z obrazu.",
    ),
    (
        67,
        "Co odróżnia modelowanie geometrii od renderowania sceny trójwymiarowej?",
        "Modelowanie opisuje geometrię, a renderowanie tworzy obraz sceny.",
        "Modelowanie tworzy obraz sceny, a renderowanie opisuje geometrię.",
        "Oba procesy oznaczają wyłącznie zmianę rozdzielczości obrazu.",
        "Renderowanie jest możliwe tylko w programie do modelowania.",
    ),
    (
        67,
        "Dlaczego sama geometria modelu nie przesądza o końcowym wyglądzie renderowanego obrazu?",
        "Obraz zależy też od obserwatora i oświetlenia sceny.",
        "Podczas renderowania geometria jest zawsze zastępowana losową siatką.",
        "Renderowanie pomija położenie obiektów i używa tylko ich nazw.",
        "Ten sam model musi dawać taki sam obraz w każdej scenie.",
    ),
    (
        68,
        "Co odróżnia algorytm Bresenhama od rysowania odcinka przez wyznaczanie punktów z równania prostej i zaokrąglanie?",
        "Wybiera piksele przyrostowo za pomocą arytmetyki stałoprzecinkowej.",
        "Zamiast pikseli tworzy wyłącznie wektorowy opis odcinka.",
        "Nie musi rozstrzygać, który piksel leży bliżej idealnej prostej.",
        "Zawsze usuwa schodkowanie bez dodatkowego antyaliasingu.",
    ),
    (
        68,
        "Jak antyaliasing może zmniejszać schodkowanie krawędzi w obrazie rastrowym?",
        "Nadaje pikselom przy krawędzi pośrednie poziomy jasności.",
        "Usuwa wszystkie piksele nieleżące dokładnie na idealnej linii.",
        "Przesuwa całą geometrię tak, by każda linia trafiła w środki pikseli.",
        "Sprowadza każdy piksel do jednego z dwóch skrajnych kolorów.",
    ),
    (
        69,
        "Po co w śledzeniu promieni prowadzi się promienie pierwotne od obserwatora przez rzutnię w stronę sceny?",
        "Aby badać promienie, które mogą mieć wpływ na widoczny obraz.",
        "Aby zasymulować fizyczną emisję światła przez oko obserwatora.",
        "Aby wyeliminować potrzebę uwzględniania źródeł światła.",
        "Aby wszystkie promienie biegły równolegle niezależnie od kamery.",
    ),
    (
        69,
        "Które przecięcie promienia pierwotnego z obiektami sceny wyznacza widoczną powierzchnię dla punktu obrazu?",
        "Najbliższe obserwatorowi wzdłuż tego promienia.",
        "Najdalsze od obserwatora wzdłuż tego promienia.",
        "Pierwsze według kolejności obiektów zapisanych w scenie.",
        "Przecięcie z obiektem o najjaśniejszym materiale.",
    ),
    (
        70,
        "Na jakiej informacji opiera się odrzucanie ścian tylnych zamkniętej bryły oglądanej z zewnątrz, gdy normalne ścian są skierowane na zewnątrz?",
        "Na kierunku normalnej ściany względem obserwatora.",
        "Na barwie tekstury przypisanej do danej ściany.",
        "Na liczbie pikseli potrzebnych do narysowania ściany.",
        "Na odległości ściany od najbliższego źródła światła.",
    ),
    (
        70,
        "Dlaczego samo uporządkowanie całych ścian od najdalszej do najbliższej może zawieść w algorytmie malarza?",
        "Fragmenty ścian mogą wzajemnie się zasłaniać w różnej kolejności.",
        "Ścian nie można sortować, jeśli mają przypisane różne materiały.",
        "Rasteryzacja i tak rysuje zawsze tylko powierzchnię najbliższą.",
        "Rzut równoległy uniemożliwia ustalenie barwy pikseli ściany.",
    ),
    (
        71,
        "Przy stałym materiale i źródle światła, który kąt wpływa na składnik oświetlenia lambertowskiego?",
        "Między normalną powierzchni a kierunkiem padania światła.",
        "Między obserwatorem a kierunkiem odbitego światła.",
        "Między dwiema krawędziami siatki wielokątów.",
        "Między osią kamery a płaszczyzną obrazu.",
    ),
    (
        71,
        "Jaki składnik model Phonga dodaje względem oświetlenia lambertowskiego?",
        "Odblask zależny od światła i kierunku patrzenia.",
        "Wyłącznie stałe światło otoczenia niezależne od kierunku.",
        "Zmianę kształtu obiektu w miejscach padania światła.",
        "Automatyczne usunięcie powierzchni zasłoniętych.",
    ),
    (
        72,
        "Które rozróżnienie materiału i tekstury obiektu trójwymiarowego jest poprawne?",
        "Materiał opisuje cechy powierzchni, a tekstura zmienia je lokalnie.",
        "Materiał zapisuje tylko geometrię, a tekstura wyłącznie źródła światła.",
        "Materiał jest obrazem wynikowym, a tekstura położeniem obserwatora.",
        "Oba terminy oznaczają wyłącznie jednolitą barwę całego obiektu.",
    ),
    (
        72,
        "Co odróżnia teksturę proceduralną od tekstury zapisanej jako bitmapa?",
        "Powstaje z procedury matematycznej i można ją skalować swobodnie.",
        "Ma zawsze stałą rozdzielczość, której nie można zmienić przy renderowaniu.",
        "Musi być zdjęciem rzeczywistej powierzchni zapisanym w pliku graficznym.",
        "Wymaga osobnego modelu trójwymiarowego dla każdego szczegółu powierzchni.",
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
