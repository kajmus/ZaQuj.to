"""Add two ABCD questions for each computer architecture topic.

Revision ID: 11
Revises: 10
"""

from alembic import op
import sqlalchemy as sa


revision = "11"
down_revision = "10"
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
        1,
        "Czym charakteryzuje się tzw. „wąskie gardło von Neumanna” w klasycznej architekturze komputerowej?",
        "Współdzieleniem jednej magistrali przez rozkazy i dane, co uniemożliwia jednoczesne pobranie instrukcji oraz operanda z pamięci głównej.",
        "Zbyt małą liczbą rejestrów ogólnego przeznaczenia w jednostce arytmetyczno-logicznej (ALU) względem pojemności pamięci RAM.",
        "Koniecznością stosowania dwóch fizycznie oddzielnych pamięci dla kodu programu oraz dla danych, co komplikuje budowę kompilatorów.",
        "Ograniczeniem maksymalnej częstotliwości taktowania zegara procesora wynikającym z pojemności pamięci podręcznej L1.",
    ),
    (
        1,
        "Na jakiej zasadzie opiera się skuteczność wielopoziomowej hierarchii pamięci (rejestry, cache L1/L2/L3, RAM, pamięć masowa)?",
        "Na zasadzie lokalności odwołań (czasowej i przestrzennej), zgodnie z którą programy wielokrotnie korzystają z tych samych danych oraz danych leżących pod sąsiednimi adresami.",
        "Na równomiernym rozkładzie odwołań do całej przestrzeni adresowej, co pozwala na statyczne przypisanie stron pamięci do poszczególnych poziomów.",
        "Na fakcie, że pamięć SRAM jest znacznie tańsza w produkcji na jednostkę pojemności niż pamięć DRAM, lecz charakteryzuje się większym czasem dostępu.",
        "Na mechanizmie bezpośredniego dostępu procesora do pamięci masowej z pominięciem pamięci operacyjnej RAM.",
    ),
    (
        2,
        "Jaką funkcję w typowym procesorze pełni rejestr licznika rozkazów (PC – Program Counter / IP – Instruction Pointer)?",
        "Przechowuje adres w pamięci kolejnej instrukcji, która ma zostać pobrana i wykonana przez procesor.",
        "Zlicza całkowitą liczbę rozkazów wykonanych przez procesor od momentu uruchomienia systemu operacyjnego.",
        "Przechowuje kod maszynowy aktualnie dekodowanej instrukcji w jednostce sterującej.",
        "Wskazuje adres szczytu stosu wywołań aktualnie wykonywanego wątku.",
    ),
    (
        2,
        "Czym różni się jednostka sterująca realizowana sprzętowo (hardwired) od jednostki mikroprogramowanej?",
        "Jednostka sprzętowa generuje sygnały sterujące za pomocą dedykowanych układów kombinacyjnych i sekwencyjnych, co zapewnia wyższą szybkość działania kosztem mniejszej elastyczności.",
        "Jednostka sprzętowa przechowuje sekwencje sygnałów sterujących w pamięci ROM wewnątrz procesora, co pozwala na łatwą aktualizację listy rozkazów.",
        "Jednostka mikroprogramowana jest stosowana wyłącznie w architekturach RISC ze względu na minimalny czas dekodowania prostych rozkazów.",
        "Jednostka mikroprogramowana nie wymaga zegara systemowego, ponieważ wykonuje mikrorozkazy w sposób całkowicie asynchroniczny.",
    ),
    (
        3,
        "Jaka jest podstawowa różnica między przerwaniem sprzętowym a wyjątkiem (pułapką)?",
        "Przerwanie sprzętowe jest zdarzeniem asynchronicznym generowanym przez urządzenia zewnętrzne względem wykonywanego strumienia instrukcji, natomiast wyjątek jest synchroniczny i wynika bezpośrednio z wykonania konkretnego rozkazu.",
        "Przerwania sprzętowe są obsługiwane wyłącznie w trybie użytkownika (user mode), a wyjątki wyłącznie w trybie jądra (kernel mode).",
        "Obsługa wyjątku nigdy nie wymaga zapisywania kontekstu procesora na stosie, w przeciwieństwie do obsługi przerwania sprzętowego.",
        "Wyjątki mogą być maskowane za pomocą flagi przerwań w rejestrze stanu procesora, natomiast żadnego przerwania sprzętowego nie da się zamaskować.",
    ),
    (
        3,
        "Co dzieje się w procesorze bezpośrednio przed skokiem do procedury obsługi przerwania (ISR – Interrupt Service Routine)?",
        "Procesor kończy bieżącą instrukcję, zapisuje na stosie co najmniej rejestr flag oraz licznik rozkazów (PC), a następnie ładuje do PC adres procedury pobrany z tablicy wektorów przerwań.",
        "Procesor natychmiast przerywa bieżący cykl zegarowy, czyści zawartość pamięci podręcznej L1 i przekazuje sterowanie do harmonogramu zadań systemu operacyjnego.",
        "Procesor kopiuje całą zawartość pamięci operacyjnej bieżącego procesu na dysk twardy, aby zwolnić miejsce dla procedury obsługi przerwania.",
        "Procesor przełącza się w tryb rzeczywisty (real mode) i wyłącza mechanizm stronicowania pamięci na czas trwania przerwania.",
    ),
    (
        4,
        "Dlaczego kod uzupełnieniowy do dwóch (U2) jest powszechnie stosowany do reprezentacji liczb całkowitych ze znakiem w komputerach?",
        "Zapewnia jednoznaczną reprezentację zera oraz pozwala na wykonywanie operacji dodawania i odejmowania za pomocą tego samego układu sumatora, bez oddzielnego traktowania bitu znaku.",
        "Pozwala na zapisanie dwukrotnie większego zakresu liczb dodatnich niż w kodzie znak-moduł przy tej samej liczbie bitów.",
        "Eliminuje całkowicie problem przepełnienia arytmetycznego (overflow) podczas dodawania dwóch liczb o tym samym znaku.",
        "Umożliwia bezpośrednie mnożenie liczb zmiennoprzecinkowych bez konieczności normalizacji mantysy.",
    ),
    (
        4,
        "Z jakich pól składa się standardowa reprezentacja liczby zmiennoprzecinkowej pojedynczej precyzji (32-bitowej) w standardzie IEEE 754?",
        "Z 1 bitu znaku, 8 bitów wykładnika zapisanego z obciążeniem (bias równym 127) oraz 23 bitów części ułamkowej mantysy (z niejawnym bitem wiodącym dla liczb znormalizowanych).",
        "Z 1 bitu znaku, 11 bitów wykładnika w kodzie U2 oraz 20 bitów mantysy w kodzie BCD.",
        "Z 2 bitów znaku (dla mantysy i wykładnika), 8 bitów wykładnika oraz 22 bitów mantysy.",
        "Z 1 bitu znaku, 15 bitów części całkowitej oraz 16 bitów części ułamkowej w formacie stałoprzecinkowym.",
    ),
    (
        5,
        "Czym jest architektura zestawu rozkazów (ISA – Instruction Set Architecture) na poziomie „konwencjonalnej maszyny”?",
        "Formalną specyfikacją interfejsu między sprzętem a oprogramowaniem, definiującą m.in. dostępne rozkazy, typy danych, rejestry widoczne dla programisty oraz tryby adresowania.",
        "Szczegółowym schematem bramek logicznych i połączeń tranzystorowych użytych do budowy konkretnego modelu procesora.",
        "Zestawem wywołań systemowych (syscalls) udostępnianych przez jądro systemu operacyjnego aplikacjom użytkownika.",
        "Środowiskiem uruchomieniowym tłumaczącym kod bajtowy (bytecode) w czasie rzeczywistym za pomocą kompilacji JIT.",
    ),
    (
        5,
        "Jaka jest główna rola asemblera w procesie tworzenia oprogramowania niskopoziomowego?",
        "Tłumaczenie mnemoników, etykiet i dyrektyw języka asemblera na odpowiadający im binarny kod maszynowy (plik obiektowy) w relacji zbliżonej do 1:1.",
        "Automatyczna optymalizacja algorytmów wysokiego poziomu oraz zarządzanie pamięcią dynamiczną poprzez mechanizm garbage collection.",
        "Łączenie gotowych bibliotek współdzielonych z kodem źródłowym w języku C przed uruchomieniem preprocesora.",
        "Emulowanie architektury procesora docelowego na maszynie o innej architekturze sprzętowej.",
    ),
    (
        6,
        "Na czym polega główna zaleta mechanizmu DMA (Direct Memory Access) w obsłudze urządzeń wejścia/wyjścia?",
        "Umożliwia kontrolerowi DMA bezpośrednie przesyłanie bloków danych między urządzeniem I/O a pamięcią operacyjną bez angażowania procesora w transfer każdego pojedynczego bajtu lub słowa.",
        "Eliminuje konieczność stosowania przerwań sprzętowych, ponieważ procesor nie jest w ogóle informowany o zakończeniu transferu danych.",
        "Pozwala urządzeniom zewnętrznym na bezpośrednie wykonywanie rozkazów w jednostce arytmetyczno-logicznej (ALU) procesora.",
        "Zastępuje magistralę systemową połączeniem szeregowym, co zapobiega powstawaniu konfliktów dostępu do pamięci RAM.",
    ),
    (
        6,
        "Czym charakteryzuje się technika wejścia/wyjścia odwzorowanego w pamięci (Memory-Mapped I/O)?",
        "Rejestry kontrolerów urządzeń I/O mają przypisane adresy w tej samej przestrzeni adresowej co pamięć RAM, dzięki czemu dostęp do nich odbywa się za pomocą standardowych rozkazów odczytu i zapisu pamięci.",
        "Urządzenia wejścia/wyjścia posiadają całkowicie oddzielną przestrzeń adresową i wymagają dedykowanych rozkazów procesora, takich jak IN oraz OUT.",
        "Dane z urządzeń I/O są zawsze zapisywane bezpośrednio w pamięci podręcznej L1 procesora z pominięciem pamięci operacyjnej.",
        "Dostęp do urządzeń I/O jest możliwy wyłącznie po wcześniejszym wyłączeniu jednostki zarządzania pamięcią (MMU).",
    ),
    (
        7,
        "Do której kategorii w taksonomii Flynna zaliczają się współczesne jednostki wektorowe (np. rozszerzenia AVX/SSE) wykonujące tę samą operację jednocześnie na wielu elementach tablicy?",
        "SIMD (Single Instruction, Multiple Data).",
        "SISD (Single Instruction, Single Data).",
        "MISD (Multiple Instruction, Single Data).",
        "MIMD (Multiple Instruction, Multiple Data).",
    ),
    (
        7,
        "Jaki problem rozwiązują protokoły spójności pamięci podręcznej (np. MESI) w systemach wieloprocesorowych ze wspólną pamięcią?",
        "Zapewniają, że wszystkie rdzenie procesora widzą spójną i aktualną wartość danych, gdy wiele lokalnych pamięci cache przechowuje kopię tej samej linii pamięci operacyjnej.",
        "Zapobiegają zakleszczeniom (deadlock) między wątkami aplikacji korzystającymi z tych samych semaforów w systemie operacyjnym.",
        "Synchronizują częstotliwość taktowania zegarów poszczególnych rdzeni w celu zmniejszenia poboru mocy.",
        "Rozdzielają automatycznie kod jednowątkowy na wiele niezależnych wątków wykonywanych równolegle.",
    ),
    (
        8,
        "Czym jest hazard sterowania (control hazard) w procesorze z przetwarzaniem potokowym (pipelining) i jak się go minimalizuje?",
        "Jest to opóźnienie wynikające z niepewności co do adresu kolejnej instrukcji przy rozkazach skoku warunkowego; minimalizuje się go m.in. poprzez mechanizmy przewidywania skoków (branch prediction) i wykonanie spekulatywne.",
        "Jest to sytuacja, w której dwie instrukcje próbują jednocześnie skorzystać z tej samej jednostki wykonawczej ALU; minimalizuje się go poprzez zwiększenie pojemności pamięci RAM.",
        "Jest to błąd wynikający z próby odczytu rejestru przed jego zapisaniem przez poprzednią instrukcję; minimalizuje się go wyłącznie poprzez wyłączenie pamięci podręcznej.",
        "Jest to przepełnienie bufora rozkazów podczas obsługi przerwania; minimalizuje się go poprzez obniżenie częstotliwości taktowania zegara procesora.",
    ),
    (
        8,
        "Co wynika z prawa Amdahla w kontekście optymalizacji i zrównoleglania systemu komputerowego?",
        "Maksymalne przyspieszenie programu jest ściśle ograniczone przez ułamek kodu, który musi zostać wykonany sekwencyjnie, niezależnie od tego, jak wiele procesorów dodamy do systemu.",
        "Przyspieszenie systemu rośnie zawsze liniowo wraz ze wzrostem liczby rdzeni procesora, pod warunkiem zapewnienia odpowiedniej przepustowości pamięci RAM.",
        "Podwojenie częstotliwości taktowania procesora zawsze prowadzi do dokładnie dwukrotnego skrócenia czasu wykonania dowolnego programu.",
        "Wydajność procesora wielordzeniowego zależy wyłącznie od rozmiaru pamięci podręcznej L3, a nie od stopnia zrównoleglenia algorytmu.",
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