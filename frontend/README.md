# Dla osób pracujących na frontendzie:

## 1. Kilka uwag na szybko
- `npm install -y` po pierwszym fetchu. W dodatku, ilekroć odpalenie `npm run build` albo `npm run dev` szwankuje. Ktoś po drodze mógł doinstalować jakąś zależność z NPM, a jeżeli nie, to `npm install -y` nic nie zrobi.
- Jest ustawiony ESLint i TypeScript, a o ile Github i tak będzie od razu testowało lintowanie i kompilację przed MR, to najlepiej się zabezpieczyć i przed commitem rutynowo odpalić `npm run lint` i `npm run build`, żeby się upewnić, że wszystko na miejscu.
- Proszę w związku z tym nie babrać w plikach poza folderami src, pages i public na oślep. Jeżeli czat powie żeby babrać, to najpierw spytać na Discordzie.
- Style robimy przez Tailwind żeby zachować jednolitość.

## 2. Kiedy zabieramy się za zadanie

1. Tworzymy nową gałąź na podstawie aktualnej gałęzi **`dev-branch`**, a następnie otwieramy na GitHubie nowy Draft PR i łączymy go z Issue ([Instrukcja](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#manually-linking-a-pull-request-or-branch-to-an-issue-using-the-issue-sidebar)). Draft PR służy do sygnalizowania postępu prac i nie oznacza, że kod jest gotowy na review.
2. Checkoutujemy nowo utworzoną gałąź na własnym komputerze.
3. Gdy chcemy dodać nowy feature, tworzymy folder na jego kod w `src/features/<nazwa-feature'a>/`.
4. Gdy nowy feature **wymaga** własnego entrypointa (tj. oddzielnej strony w aplikacji), tworzymy odpowiednie pliki:
   - `src/entrypoints/<nazwa-feature'a>.tsx`
   - odpowiedni plik HTML w `pages/` zgodnie z przyjętą konfiguracją Vite.
5. Gdy implementacja feature'a wymaga nowego kodu, komponentów, funkcji pomocniczych itp., postępujemy według poniższych zasad:
   1. **Sprawdzamy, czy potrzebny kod już istnieje.**
      - Przeszukujemy odpowiednie katalogi `src/components/`, `src/lib/` oraz `src/features/`.
      - Jeżeli istniejący kod spełnia nasze wymagania, korzystamy z niego zamiast tworzyć duplikat.
   2. Jeżeli potrzebny kod nie istnieje, ustalamy, czy jest specyficzny dla danego feature'a, czy powinien być współdzielony.
      - Jeżeli kod jest specyficzny dla danego feature'a, umieszczamy go w odpowiednim katalogu `src/features/<nazwa-feature'a>/`.
      - Jeżeli jest to komponent UI przeznaczony do wykorzystania w różnych częściach aplikacji, rozważamy umieszczenie go w `src/components/`.
      - Jeżeli jest to funkcja pomocnicza lub narzędzie o ogólnym zastosowaniu, rozważamy umieszczenie go w `src/lib/`.
   3. Jeżeli potrzebny jest nowy element współdzielony, sprawdzamy, **czy jego implementacja nie jest już przedmiotem innego Issue lub PR-a**.
      - Jeżeli ktoś już nad nim pracuje, kontaktujemy się z tą osobą i uzgadniamy sposób integracji oraz oczekiwany interfejs.
      - Jeżeli nikt nad nim nie pracuje, oceniamy zakres:
        - **Mały, samodzielny element:** możemy zaimplementować go w ramach aktualnego feature'a i uwzględnić w jego PR-ze.
        - **Większy element lub rozwiązanie potrzebne kilku feature'om:** tworzymy osobne Issue opisujące cel, oczekiwany interfejs i kryteria akceptacji. Łączymy je z Issue aktualnego feature'a i uzgadniamy kolejność prac z zespołem.
   4. **Przed oddaniem kodu do review** sprawdzamy, czy nowe elementy znajdują się we właściwych katalogach, nie dublują istniejących rozwiązań i — w przypadku współdzielonego kodu — posiadają odpowiednie testy.
   5. Jeżeli nie mamy pewności, czy dany element powinien być współdzielony, konsultujemy decyzję z zespołem na Discordzie, aby uniknąć równoległego implementowania tego samego rozwiązania.
   6. **Aktualizujemy własną gałąź, gdy potrzebne współdzielone rozwiązanie zostanie dodane do `dev-branch`.**
      - Pobieramy najnowsze informacje z repozytorium:
        ```bash
        git fetch origin
        ```
      - Upewniamy się, że mamy zapisane lub zacommitowane własne zmiany.
      - Włączamy najnowsze zmiany z `origin/dev-branch` do własnej gałęzi zgodnie z procedurą opisaną poniżej w punkcie 7.
      - Sprawdzamy, czy nasz feature nadal działa i korzysta z oficjalnej, współdzielonej implementacji zamiast z jej tymczasowej kopii.
6. Podczas pracy regularnie commitujemy zmiany i wypychamy je na GitHuba:
   ```bash
   git add .
   git commit -m "Opis wprowadzonych zmian"
   git push
   ```
   W razie potrzeby aktualizujemy opis Draft PR-a, aby pozostałe osoby wiedziały, nad czym pracujemy i od czego zależymy.
7. **Przed oddaniem feature'a do review obowiązkowo aktualizujemy własną gałąź względem najnowszego `dev-branch`.**
   1. Upewniamy się, że wszystkie lokalne zmiany są zapisane lub zacommitowane.
   2. Pobieramy najnowszy stan repozytorium:
      ```bash
      git fetch origin
      ```
   3. Upewniamy się, że znajdujemy się na własnej gałęzi feature'a:
      ```bash
      git switch <nazwa-własnej-gałęzi>
      ```
   4. Włączamy najnowsze zmiany z `dev-branch` do własnej gałęzi:
      ```bash
      git merge origin/dev-branch
      ```
      Jeżeli wystąpią konflikty, rozwiązujemy je, sprawdzamy poprawność kodu i kończymy merge. W razie wątpliwości konsultujemy konflikty z autorem zmian.
   5. Uruchamiamy wymagane kontrole projektu, w szczególności lint, testy i build.
   6. Wypychamy zaktualizowaną gałąź:
      ```bash
      git push
      ```
   7. Sprawdzamy, czy PR nie ma konfliktów i czy spełnia wymagania dotyczące review.
8. Gdy praca nad feature'em jest zakończona, zmieniamy Draft PR na gotowy do review. Bazą PR-a (`base`) jest **`dev-branch`**, a porównywaną gałęzią (`compare`) jest **nasza gałąź feature'a**. Następnie oczekujemy na review Scrum Mastera i członków odpowiedzialnych za frontend. Jeżeli otrzymamy uwagi, wprowadzamy poprawki na tej samej gałęzi, commitujemy je i pushujemy aktualizacje do istniejącego PR-a.

### Ważne: jak aktualizujemy gałąź

W tym procesie przyjmujemy strategię **merge `origin/dev-branch` do własnej gałęzi feature'a**. Dzięki temu nie przepisujemy historii opublikowanej gałęzi i unikamy konieczności używania `git push --force`.

Nie wykonujemy merge'a własnego feature'a do `dev-branch` samodzielnie — integracja następuje przez zatwierdzony PR.

## 3. Jak wygląda struktura:
- src/features/ zawiera w sobie foldery poszczególnych feature'ów frontendu nad którymi pracujemy zazwyczaj oddzielnie (tj. dwie osoby nie klepią w jednym feature folderze w tym samym czasie, chyba, że to konieczne), żeby zminimalizować kolizje.
- src/entrypoints/ zawiera pliki .tsx poszczególnych entrypointów, które powinny tylko stanowić ramkę dla komponentów z odpowiedniego folderu w src/features/. Np. src/entrypoints/home.tsx ma bardzo minimalny kod, podczas gdy src/features/home/HomePage.tsx faktycznie stanowi zawartość strony głównej.
- Analogicznie, pages/ zawiera proste pliki HTML, które odpalają odpowiednie moduły z src/entrypoints/. Np. pages/study.html odpala moduł z src/entrypoints/study.tsx. Wzorowym przykładem takiego pliku jest index.html (który nie jest w pages/ jako przypadek szczególny).
- src/components/ui/ przechowuje komponenty UI do wielokrotnego użytku na stronie - guziki, inputy, karty, rozwijane menu, itp.
- src/components/layout/ natomiast przechowuje komponenty layoutu strony - nagłówki, menu nawigacji, stopki, itp.
- src/lib/ to wspólna infrastuktura, jak np. klient API.
- src/styles/ to wspólne style (przede wszystkim import Tailwinda).