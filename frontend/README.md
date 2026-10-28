# Dla osób pracujących na frontendzie

## 1. Kilka uwag na szybko

- Po pierwszym pobraniu repozytorium oraz po zmianie zależności w `package.json` instalujemy zależności poleceniem `npm install`. W CI można korzystać z `npm ci`, jeśli repozytorium zawiera aktualny `package-lock.json`. Jeśli `npm run dev` lub `npm run build` nie działa, najpierw sprawdzamy komunikat błędu i zgodność zależności, zamiast bezwarunkowo ponawiać instalację.
- Jest ustawiony ESLint i TypeScript. Przed commitem rutynowo uruchamiamy `npm run lint` i `npm run build`, aby wychwycić błędy przed wypchnięciem zmian.
- Projekt korzysta z testów jednostkowych i integracyjnych opartych na Vitest oraz React Testing Library. Testy uruchamiamy poleceniem `npm run test`. W razie potrzeby możemy skorzystać z `npm run test:watch`, aby uruchamiać je ponownie podczas pracy nad kodem.
- **Pliki demonstracyjne:** w kodzie mogą znajdować się tymczasowe komponenty, funkcje lub przykłady służące do nauki i testowania rozwiązań, oznaczone odpowiednim komentarzem, np. `USUŃ MNIE, GDY PRZESTANĘ BYĆ PRZYDATNY JAKO DEMO`. Nie należy traktować ich jako docelowej części aplikacji. Przed usunięciem sprawdzamy, czy nadal są potrzebne, czy korzystają z nich testy oraz czy nie zależą od nich inne komponenty.
- Proszę nie wprowadzać pochopnych zmian w plikach poza folderami `src`, `pages` i `public`. Jeżeli zadanie wymaga zmiany plików konfiguracyjnych, workflow lub innych elementów poza tym zakresem, najpierw konsultujemy to na Discordzie.
- Style tworzymy za pomocą Tailwind CSS, aby zachować jednolity sposób stylowania w całej aplikacji.

## 2. Kiedy zabieramy się za zadanie

### 1. Przygotowanie gałęzi i PR-a

1. Tworzymy nową gałąź na podstawie aktualnej gałęzi **`dev-branch`**.
2. Otwieramy na GitHubie nowy Draft PR i łączymy go z odpowiednim Issue ([instrukcja GitHub](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue#manually-linking-a-pull-request-or-branch-to-an-issue-using-the-issue-sidebar)).
3. Draft PR służy do sygnalizowania postępu prac i nie oznacza, że kod jest gotowy na review.
4. Checkoutujemy nowo utworzoną gałąź na własnym komputerze.

### 2. Organizacja kodu i routing

Gdy dodajemy nowy feature, tworzymy folder na jego kod w `src/features/<nazwa-feature'a>/`.

Aplikacja korzysta z jednego punktu wejścia i routingu SPA:

- `index.html` uruchamia aplikację przez wspólny entrypoint `src/entrypoints/home.tsx`.
- `src/entrypoints/home.tsx` montuje główny komponent aplikacji `App`.
- `App` konfiguruje routing za pomocą React Routera i przypisuje ścieżki URL do odpowiednich komponentów.
- Nowy ekran dodajemy jako komponent w odpowiednim feature'ze i podłączamy do routingu.
- Nie tworzymy osobnego pliku HTML ani entrypointa dla każdej trasy.
- Nowe pliki HTML lub dodatkowe entrypointy tworzymy wyłącznie wtedy, gdy zespół świadomie zdecyduje o wprowadzeniu osobnego punktu wejścia poza standardowym routingiem SPA.

### 3. Dodawanie nowego kodu

Gdy implementacja feature'a wymaga nowych komponentów, funkcji pomocniczych, hooków lub innych elementów, postępujemy według poniższych zasad.

1. **Sprawdzamy, czy potrzebny kod już istnieje.**
   - Przeszukujemy odpowiednie katalogi `src/components/`, `src/lib/` oraz `src/features/`.
   - Jeżeli istniejący kod spełnia nasze wymagania, korzystamy z niego zamiast tworzyć duplikat.

2. **Ustalamy, gdzie powinien znaleźć się nowy kod.**
   - Kod specyficzny dla danego feature'a umieszczamy w `src/features/<nazwa-feature'a>/`.
   - Komponenty UI przeznaczone do wykorzystania w różnych częściach aplikacji rozważamy umieścić w `src/components/`.
   - Uniwersalne funkcje pomocnicze i narzędzia umieszczamy w `src/lib/`.

3. **Sprawdzamy, czy ktoś już pracuje nad współdzielonym rozwiązaniem.**
   - Weryfikujemy, czy jego implementacja nie jest przedmiotem innego Issue lub PR-a.
   - Jeżeli ktoś już nad nim pracuje, kontaktujemy się z tą osobą i uzgadniamy sposób integracji oraz oczekiwany interfejs.
   - Jeżeli nikt nad nim nie pracuje, oceniamy zakres:
     - Mały, samodzielny element możemy zaimplementować w ramach aktualnego feature'a i uwzględnić w jego PR-ze.
     - Większy element lub rozwiązanie potrzebne kilku feature'om wymaga osobnego Issue opisującego cel, oczekiwany interfejs i kryteria akceptacji. Łączymy je z Issue aktualnego feature'a i uzgadniamy kolejność prac z zespołem.

4. **Dodajemy lub aktualizujemy testy.**
   - Nowy kod powinien mieć testy adekwatne do swojej odpowiedzialności.
   - Dla funkcji pomocniczych i logiki niezależnej od UI preferujemy testy jednostkowe.
   - Dla komponentów React testujemy zachowanie widoczne dla użytkownika, np. kliknięcia, zmianę stanu, wyświetlanie danych i obsługę formularzy.
   - Dla przepływów obejmujących kilka komponentów lub ekranów dodajemy testy integracyjne, gdy pomagają sprawdzić współpracę tych elementów.
   - Przy poprawianiu błędu, jeśli to możliwe, dodajemy test odtwarzający problem, aby uniknąć jego ponownego pojawienia się.
   - Testy powinny weryfikować zachowanie kodu, a nie wyłącznie szczegóły jego implementacji.

5. **Przed oddaniem kodu do review** sprawdzamy, czy nowe elementy znajdują się we właściwych katalogach, nie dublują istniejących rozwiązań i mają odpowiednie testy.

6. Jeżeli nie mamy pewności, czy dany element powinien być współdzielony, konsultujemy decyzję z zespołem na Discordzie.

7. **Aktualizujemy własną gałąź, gdy potrzebne współdzielone rozwiązanie zostanie dodane do `dev-branch`.**
   - Pobieramy najnowsze informacje z repozytorium:
     ```bash
     git fetch origin
     ```
   - Upewniamy się, że mamy zapisane lub zacommitowane własne zmiany.
   - Włączamy najnowsze zmiany z `origin/dev-branch` do własnej gałęzi zgodnie z procedurą opisaną w punkcie 5.
   - Sprawdzamy, czy nasz feature nadal działa i korzysta z oficjalnej, współdzielonej implementacji zamiast z jej tymczasowej kopii.

### 4. Testy i kontrole jakości

W projekcie korzystamy z Vitest oraz React Testing Library. Testy umieszczamy obok testowanego kodu, używając konwencji nazw `*.test.ts` lub `*.test.tsx`.

Przykładowa struktura:

```text
src/
├── features/
│   └── example/
│       ├── Example.tsx
│       └── Example.test.tsx
└── lib/
    ├── helper.ts
    └── helper.test.ts
```

Zasady pisania testów:

- Testujemy najważniejsze zachowania i przypadki brzegowe.
- W testach komponentów preferujemy wyszukiwanie elementów przez role, etykiety i tekst widoczny dla użytkownika.
- Do symulowania interakcji użytkownika wykorzystujemy `@testing-library/user-event`.
- Testy powinny być niezależne od siebie. Nie powinny wymagać konkretnej kolejności uruchamiania ani pozostawiać po sobie stanu wpływającego na kolejne testy.
- W testach korzystających z cookies, `localStorage`, nawigacji lub innych współdzielonych zasobów dbamy o odpowiednie przygotowanie i czyszczenie stanu.
- Gdy zmieniamy zachowanie istniejącego kodu, aktualizujemy testy, których dotyczy zmiana.
- __Nie usuwamy ani nie osłabiamy testów tylko po to, aby uzyskać zielony wynik.__

Przed commitem uruchamiamy:

```bash
npm run lint
npm run test
npm run build
```

Wszystkie trzy polecenia powinny zakończyć się powodzeniem. Jeżeli testy nie przechodzą, najpierw analizujemy przyczynę i poprawiamy kod lub testy zgodnie z zamierzonym zachowaniem.

### 5. Commitowanie i aktualizowanie PR-a

Podczas pracy regularnie commitujemy zmiany i wypychamy je na GitHuba:

```bash
git add .
git commit -m "Opis wprowadzonych zmian"
git push
```

W razie potrzeby aktualizujemy opis Draft PR-a, aby pozostałe osoby wiedziały, nad czym pracujemy i od czego zależymy.

### 6. Aktualizacja gałęzi przed review

Przed oddaniem feature'a do review obowiązkowo aktualizujemy własną gałąź względem najnowszego `dev-branch`.

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
5. Uruchamiamy wymagane kontrole projektu:
   ```bash
   npm run lint
   npm run test
   npm run build
   ```
6. Wypychamy zaktualizowaną gałąź:
   ```bash
   git push
   ```
7. Sprawdzamy, czy PR nie ma konfliktów i czy spełnia wymagania dotyczące review.

### 7. Zakończenie pracy nad feature'em

Gdy praca nad feature'em jest zakończona:

1. Upewniamy się, że implementacja i testy są kompletne.
2. Sprawdzamy, czy `npm run lint`, `npm run test` i `npm run build` przechodzą poprawnie.
3. Zmieniamy Draft PR na gotowy do review.
4. Upewniamy się, że bazą PR-a (`base`) jest **`dev-branch`**, a porównywaną gałęzią (`compare`) jest nasza gałąź feature'a.
5. Oczekujemy na review Scrum Mastera i członków odpowiedzialnych za frontend.
6. Jeżeli otrzymamy uwagi, wprowadzamy poprawki na tej samej gałęzi, aktualizujemy odpowiednie testy, commitujemy zmiany i pushujemy aktualizacje do istniejącego PR-a.

## 3. Ważne: gdzie siedzi stan

- **Stan lokalny komponentu:** używamy `useState` lub `useReducer`, jeśli dane są potrzebne wyłącznie w danym komponencie albo jego bezpośredniej funkcjonalności.
- **Stan współdzielony:** gdy kilka ekranów lub komponentów potrzebuje tych samych danych, rozważamy React Context lub inne rozwiązanie dopasowane do skali problemu. Context umieszczamy blisko funkcjonalności, za którą odpowiada, zamiast automatycznie tworzyć globalny folder `contexts/`.
- **Kod związany z feature'em:** jeśli stan, hook lub komponent służy konkretnej funkcjonalności, umieszczamy go w katalogu odpowiedniego feature'a, o ile nie ma uzasadnienia, by go współdzielić.
- **Kod ogólny:** uniwersalne funkcje pomocnicze i narzędzia umieszczamy w `src/lib/`. Wielokrotnie używane komponenty UI umieszczamy w `src/components/ui/`, a wspólne elementy layoutu w `src/components/layout/`.
- **Dane trwałe:** stan React i Context nie zastępują trwałego zapisu. Dane, które mają przetrwać zamknięcie lub odświeżenie aplikacji, przechowujemy zgodnie z wymaganiami danej funkcjonalności. Nie wprowadzamy dodatkowych mechanizmów persystencji bez uzasadnionej potrzeby.
- **Testowalność:** logikę warto oddzielać od warstwy prezentacji w takim zakresie, aby można ją było testować bez konieczności odtwarzania całej aplikacji.

## 4. Jak wygląda struktura

- `src/features/` zawiera foldery poszczególnych funkcjonalności frontendu. Staramy się ograniczać równoległe zmiany w tych samych feature'ach, aby zmniejszać ryzyko konfliktów.
- `src/entrypoints/` zawiera punkt wejścia aplikacji. Obecnie `src/entrypoints/home.tsx` montuje główny komponent `App`. Nie tworzymy osobnego entrypointa dla każdej trasy SPA.
- `index.html` jest głównym dokumentem HTML uruchamiającym aplikację. Routing pomiędzy ekranami realizuje React Router; nie tworzymy osobnych plików HTML dla standardowych tras.
- `src/components/ui/` przechowuje współdzielone komponenty UI, np. przyciski, pola formularzy, karty i menu.
- `src/components/layout/` przechowuje wspólne elementy layoutu, np. nagłówki, nawigację i stopki.
- `src/lib/` zawiera ogólne narzędzia i infrastrukturę, np. funkcje pomocnicze, obsługę ciasteczek i klienta API.
- `src/styles/` zawiera wspólne style, w tym import Tailwind CSS.
- Pliki specyficzne dla jednej funkcjonalności — w tym komponenty, hooki, konteksty, logikę stanu i powiązane testy — przechowujemy w katalogu odpowiedniego feature'a, o ile nie ma uzasadnienia, by je współdzielić.
- `public/` przechowuje zasoby statyczne udostępniane bez przetwarzania przez Vite.