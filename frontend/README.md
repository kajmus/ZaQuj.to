# Dla osób pracujących na frontendzie:

## 1. Kilka uwag na szybko
- Po pierwszym pobraniu repozytorium oraz po zmianie zależności w `package.json` instalujemy zależności poleceniem `npm install` (w CI można korzystać z `npm ci`, jeśli repozytorium zawiera aktualny `package-lock.json`). Jeśli `npm run dev` lub `npm run build` nie działa, najpierw sprawdzamy komunikat błędu i zgodność zależności, zamiast bezwarunkowo ponawiać instalację.
- Jest ustawiony ESLint i TypeScript, a o ile Github i tak będzie od razu testowało lintowanie i kompilację przed MR, to najlepiej się zabezpieczyć i przed commitem rutynowo odpalić `npm run lint` i `npm run build`, żeby się upewnić, że wszystko na miejscu.
- Proszę w związku z tym nie babrać w plikach poza folderami src, pages i public na oślep. Jeżeli czat powie żeby babrać, to najpierw spytać na Discordzie.
- Style robimy przez Tailwind żeby zachować jednolitość.

## 2. Kiedy zabieramy się za zadanie

1. Tworzymy nową gałąź na podstawie aktualnej gałęzi **`dev-branch`**, a następnie otwieramy na GitHubie nowy Draft PR i łączymy go z Issue ([Instrukcja](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#manually-linking-a-pull-request-or-branch-to-an-issue-using-the-issue-sidebar)). Draft PR służy do sygnalizowania postępu prac i nie oznacza, że kod jest gotowy na review.
2. Checkoutujemy nowo utworzoną gałąź na własnym komputerze.
3. Gdy dodajemy nowy feature, tworzymy folder na jego kod w `src/features/<nazwa-feature'a>/`.
4. **Aplikacja korzysta z jednego punktu wejścia i routingu SPA.**
   - `index.html` uruchamia aplikację przez wspólny entrypoint `src/entrypoints/home.tsx`.
   - `src/entrypoints/home.tsx` montuje główny komponent aplikacji `App`.
   - `App` konfiguruje routing za pomocą React Routera i przypisuje ścieżki URL do odpowiednich komponentów.
   - Nowy ekran dodajemy jako komponent w odpowiednim feature'ze i podłączamy do routingu. Nie tworzymy osobnego pliku HTML ani entrypointa dla każdej trasy.
   - Jeżeli potrzebujemy nowej trasy, sprawdzamy najpierw istniejącą konfigurację w `App.tsx` i rozszerzamy ją zgodnie z potrzebą.
   - Nowe pliki HTML lub dodatkowe entrypointy tworzymy wyłącznie wtedy, gdy zespół świadomie zdecyduje o wprowadzeniu osobnego punktu wejścia poza standardowym routingiem SPA.
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

### Ważne: gdzie siedzi stan
- **Stan lokalny komponentu:** używamy `useState` lub `useReducer`, jeśli dane są potrzebne wyłącznie w danym komponencie albo jego bezpośredniej funkcjonalności.
- **Stan współdzielony:** gdy kilka ekranów lub komponentów potrzebuje tych samych danych, rozważamy React Context lub inne rozwiązanie dopasowane do skali problemu. Context umieszczamy blisko funkcjonalności, za którą odpowiada, zamiast automatycznie tworzyć globalny folder `contexts/`.
- **Kod związany z feature'em:** jeśli stan, hook lub komponent służy konkretnej funkcjonalności, umieszczamy go w `src/features/<nazwa-feature'a>/`.
- **Kod ogólny:** uniwersalne funkcje pomocnicze i narzędzia, które nie należą do konkretnego feature'a, umieszczamy w `src/lib/`. Wielokrotnie używane komponenty UI umieszczamy w `src/components/ui/`, a wspólne elementy layoutu w `src/components/layout/`.
- **Dane trwałe:** stan React i Context nie zastępują trwałego zapisu. Dane, które mają przetrwać zamknięcie lub odświeżenie aplikacji, docelowo przechowujemy za pośrednictwem API i backendu, zgodnie z wymaganiami danej funkcjonalności. Nie wprowadzamy dodatkowych mechanizmów persystencji bez uzasadnionej potrzeby.

### Ważne: jak aktualizujemy gałąź

W tym procesie przyjmujemy strategię **merge `origin/dev-branch` do własnej gałęzi feature'a**. Dzięki temu nie przepisujemy historii opublikowanej gałęzi i unikamy konieczności używania `git push --force`.

Nie wykonujemy merge'a własnego feature'a do `dev-branch` samodzielnie — integracja następuje przez zatwierdzony PR.

## 3. Jak wygląda struktura:
- `src/features/` zawiera foldery poszczególnych funkcjonalności frontendu. Staramy się ograniczać równoległe zmiany w tych samych feature'ach, aby zmniejszać ryzyko konfliktów.
- `src/entrypoints/` zawiera punkt wejścia aplikacji. Obecnie `src/entrypoints/home.tsx` montuje główny komponent `App`. Nie tworzymy osobnego entrypointa dla każdej trasy SPA.
- `index.html` jest głównym dokumentem HTML uruchamiającym aplikację. Routing pomiędzy ekranami realizuje React Router; nie tworzymy osobnych plików HTML dla standardowych tras.
- `src/components/ui/` przechowuje współdzielone komponenty UI, np. przyciski, pola formularzy, karty i menu.
- `src/components/layout/` przechowuje wspólne elementy layoutu, np. nagłówki, nawigację i stopki.
- `src/lib/` zawiera ogólne narzędzia i infrastrukturę, np. funkcje pomocnicze, obsługę ciasteczek i klienta API.
- `src/styles/` zawiera wspólne style, w tym import Tailwind CSS.
- Pliki specyficzne dla jednej funkcjonalności — w tym komponenty, hooki, konteksty i logikę stanu — przechowujemy w katalogu odpowiedniego feature'a, o ile nie ma uzasadnienia, by je współdzielić.
- `public/` przechowuje zasoby statyczne udostępniane bez przetwarzania przez Vite.

