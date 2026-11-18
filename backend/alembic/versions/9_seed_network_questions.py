from alembic import op
import sqlalchemy as sa


revision = "9"
down_revision = "8"
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
        17,
        "Które przypisanie zadań do warstw modelu OSI jest poprawne?",
        "Sieciowa wyznacza drogę przez węzły, transportowa obsługuje wymianę między procesami.",
        "Transportowa wyznacza drogę przez węzły, sieciowa obsługuje wymianę między procesami.",
        "Łącza danych wyznacza drogę między sieciami, prezentacji nadaje adresy IP.",
        "Fizyczna zarządza sesją, aplikacji przesyła pojedyncze bity przez medium.",
    ),
    (
        17,
        "Jak odróżnić usługę sieciową od protokołu?",
        "Usługa określa, co jest dostępne, protokół reguły komunikacji.",
        "Protokół określa, co jest dostępne, usługa reguły komunikacji.",
        "Usługa jest zawsze sprzętem, protokół wyłącznie programem.",
        "Oba pojęcia oznaczają ten sam fizyczny nośnik transmisji.",
    ),
    (
        18,
        "Jaką możliwość daje kanał full duplex, której nie zapewnia half duplex?",
        "Jednoczesne nadawanie danych w obu kierunkach.",
        "Naprzemienne nadawanie danych w obu kierunkach.",
        "Przesył danych tylko w jednym ustalonym kierunku.",
        "Rezerwację całej trasy między sieciami przed transmisją.",
    ),
    (
        18,
        "Dwa urządzenia komunikują się raz przez skrętkę, raz przez fale radiowe. Co jest potrzebne w obu przypadkach, niezależnie od medium?",
        "Uzgodnione reguły wymiany i interpretacji informacji.",
        "Ten sam typ złącza fizycznego po obu stronach.",
        "Transmisja jednocześnie w obu kierunkach.",
        "Trwale zarezerwowany obwód między urządzeniami.",
    ),
    (
        19,
        "Która cecha jest charakterystyczna dla komutacji pakietów?",
        "Pakiety jednej wiadomości mogą być trasowane niezależnie.",
        "Dla wszystkich pakietów rezerwuje się jedną trasę na cały czas połączenia.",
        "Dane wysyła się dopiero po zestawieniu fizycznego obwodu.",
        "Pakiety muszą dotrzeć do odbiorcy w kolejności nadania.",
    ),
    (
        19,
        "Co zachodzi podczas enkapsulacji danych po stronie nadawczej?",
        "Dane warstwy wyższej umieszcza się w jednostce warstwy niższej.",
        "Dane warstwy niższej usuwa się przed przekazaniem do medium.",
        "Odbiorca wydobywa dane aplikacji jeszcze przed ich nadaniem.",
        "Pakiety zastępuje się trwale zarezerwowanym obwodem.",
    ),
    (
        20,
        "Które stwierdzenie opisuje komutację obwodów?",
        "Kanały są zajęte przez cały czas zestawionego połączenia.",
        "Każdy pakiet wybiera własną trasę bez rezerwacji kanałów.",
        "Trasę ustala się dopiero po zakończeniu przesyłania danych.",
        "Kanały są zwalniane po wysłaniu każdego pakietu osobno.",
    ),
    (
        20,
        "Co odróżnia przełączany obwód wirtualny SVC od stałego PVC?",
        "SVC zestawia się na żądanie, PVC utrzymuje się na stałe.",
        "PVC zestawia się na żądanie, SVC utrzymuje się na stałe.",
        "SVC wymaga osobnego przewodu, PVC jest obwodem logicznym.",
        "SVC służy do szyfrowania, a PVC wyłącznie do kompresji.",
    ),
    (
        21,
        "Po co hostowi adres bramy domyślnej?",
        "Aby przekazywać ruch do sieci spoza sieci lokalnej.",
        "Aby kierować do innych sieci wyłącznie po adresie MAC odbiorcy.",
        "Aby przypisać osobny adres IP każdemu hostowi lokalnemu.",
        "Aby zastąpić tablicę tras we wszystkich routerach.",
    ),
    (
        21,
        "Dlaczego wybór trasy nie musi zależeć wyłącznie od długości drogi do celu?",
        "Znaczenie mogą mieć też obciążenie segmentów i priorytet pakietu.",
        "Najkrótsza droga jest zawsze jednocześnie najmniej obciążona.",
        "Priorytet pakietu określa fizyczną długość każdego łącza.",
        "Tablica tras przechowuje wyłącznie adres nadawcy pakietu.",
    ),
    (
        22,
        "Które rozróżnienie ról IP oraz protokołów transportowych jest poprawne?",
        "IP obsługuje adresowanie i trasowanie, TCP i UDP transport.",
        "TCP i UDP wyznaczają adresy IP, a IP potwierdza dostarczenie danych.",
        "IP steruje wyłącznie aplikacjami, TCP i UDP sygnałem w przewodzie.",
        "IP służy do szyfrowania, TCP i UDP tylko do nazw domenowych.",
    ),
    (
        22,
        "Co odróżnia TCP od UDP w zakresie kontroli dostarczenia danych?",
        "TCP ma mechanizmy kontroli dostarczenia, UDP ich nie zapewnia.",
        "UDP ma mechanizmy kontroli dostarczenia, TCP ich nie zapewnia.",
        "Oba protokoły dają identyczne gwarancje dostarczenia.",
        "Tylko UDP może przesyłać dane między różnymi komputerami.",
    ),
    (
        23,
        "Które przypisanie protokołów do pracy z pocztą elektroniczną jest poprawne?",
        "SMTP przesyła pocztę, IMAP udostępnia skrzynkę na serwerze.",
        "IMAP służy do wysyłania poczty, SMTP do przeglądania folderów.",
        "POP3 służy do wysyłania poczty, SMTP do dostępu do skrzynki.",
        "FTP służy do wysyłania poczty, IMAP do przesyłania plików.",
    ),
    (
        23,
        "Które rozróżnienie najlepiej opisuje FTP i NFS?",
        "FTP służy do przesyłania plików, NFS udostępnia zdalny system plików.",
        "NFS służy do przesyłania plików, FTP udostępnia zdalny system plików.",
        "Oba protokoły służą wyłącznie do obsługi stron internetowych.",
        "Oba protokoły służą wyłącznie do wysyłania wiadomości pocztowych.",
    ),
    (
        24,
        "Co wyróżnia rozproszony atak DDoS na tle ataku DoS prowadzonego z jednego źródła?",
        "Próby przeciążenia usługi pochodzą z wielu źródeł.",
        "Atak dotyczy wyłącznie urządzeń w sieci prywatnej.",
        "Celem jest odczyt danych zamiast ograniczenia dostępności.",
        "Atak nie może prowadzić do niedostępności usługi.",
    ),
    (
        24,
        "Który środek ogranicza odczyt przechwyconej transmisji, ale sam nie usuwa podatności oprogramowania serwera?",
        "Szyfrowanie połączenia, na przykład przy użyciu TLS.",
        "Łatanie podatności w oprogramowaniu serwera.",
        "Monitorowanie natężenia ruchu w sieci.",
        "Skanowanie portów dostępnych na serwerze.",
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
