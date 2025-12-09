# Program Digitalizacji - Struktura Projektu

**Okres realizacji:** 2026-01-01 - 2028-02-15

---

## E1 - Start i przygotowanie

**Okres:** 2026-01-01 - 2026-03-31

| ID | Zadanie | Data rozpoczęcia | Data zakończenia | Kamień milowy | Zasoby | Obszar kosztów |
|---|---|---|---|---|---|---|
| E1.1 | 🎯 Formalne uruchomienie programu | 2026-01-01 | 2026-01-15 | ✅ | Zarząd / Właściciel | Szkolenia i konsultacje |
| E1.2 | 📋 Inwentaryzacja obecnych narzędzi | 2026-01-16 | 2026-02-28 | ❌ | PM + IT | Szkolenia i konsultacje |
| E1.3 | 📋 Określenie budżetu IT na 2026-2027 | 2026-02-01 | 2026-02-28 | ❌ | Zarząd + PM | Szkolenia i konsultacje |
| E1.4 | 📋 Wybór dostawcy PMS/booking engine i wstępny brief nowej strony www | 2026-02-15 | 2026-03-31 | ❌ | PM + IT + Marketing | PMS + booking engine + channel manager |

![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/mateuszdolega/Repos/private/BE/harmonogram/gantt_chart_digitalizacja.png?version%3D1765277703378)**Zależności:**
- **E1.2** zależy od: E1.1
- **E1.3** zależy od: E1.2
- **E1.4** zależy od: E1.2

---

## E2 - Strona www + identyfikacja

**Okres:** 2026-04-01 - 2026-09-30

| ID | Zadanie | Data rozpoczęcia | Data zakończenia | Kamień milowy | Zasoby | Obszar kosztów |
|---|---|---|---|---|---|---|
| E2.1 | 📋 Projekt nowej strony www | 2026-04-01 | 2026-05-31 | ❌ | PM + Marketing + Dostawca WWW | Nowa strona www + identyfikacja |
| E2.2 | 📋 Przygotowanie logo i szablonów graficznych | 2026-04-01 | 2026-05-15 | ❌ | Marketing + Dostawca WWW | Nowa strona www + identyfikacja |
| E2.3 | 📋 Wdrożenie nowej strony www | 2026-06-01 | 2026-08-31 | ❌ | Dostawca WWW + PM | Nowa strona www + identyfikacja |
| E2.4 | 📋 Aktualizacja treści i zdjęć + podstawowe SEO | 2026-07-01 | 2026-09-30 | ❌ | Marketing | Nowa strona www + identyfikacja |
| E2.5 | 🎯 Finalizacja strony www i identyfikacji | 2026-09-01 | 2026-09-30 | ✅ | PM + Marketing | Nowa strona www + identyfikacja |

**Zależności:**
- **E2.1** zależy od: E1.4
- **E2.2** zależy od: E1.4
- **E2.3** zależy od: E2.1, E2.2
- **E2.4** zależy od: E2.1
- **E2.5** zależy od: E2.3, E2.4

---

## E3 - System rezerwacji i płatności

**Okres:** 2026-10-01 - 2027-01-15

| ID | Zadanie | Data rozpoczęcia | Data zakończenia | Kamień milowy | Zasoby | Obszar kosztów |
|---|---|---|---|---|---|---|
| E3.1 | 📋 Uruchomienie booking engine | 2026-10-01 | 2026-10-31 | ❌ | Dostawca PMS + PM | PMS + booking engine + channel manager |
| E3.2 | 📋 Uruchomienie płatności online | 2026-11-01 | 2026-11-30 | ❌ | Dostawca PMS + operator płatności | PMS + booking engine + channel manager |
| E3.3 | 📋 Integracja z OTA (channel manager) | 2026-11-01 | 2026-12-15 | ❌ | Dostawca PMS | PMS + booking engine + channel manager |
| E3.4 | 📋 Testy procesu rezerwacji | 2026-12-01 | 2026-12-31 | ❌ | Recepcja + PM | PMS + booking engine + channel manager |
| E3.5 | 🎯 Start produkcyjny systemu rezerwacji | 2027-01-01 | 2027-01-15 | ✅ | PM + Recepcja | PMS + booking engine + channel manager |

**Zależności:**
- **E3.1** zależy od: E1.4, E2.5
- **E3.2** zależy od: E3.1
- **E3.3** zależy od: E3.1
- **E3.4** zależy od: E3.2, E3.3
- **E3.5** zależy od: E3.4

---

## E4 - CRM i lojalność

**Okres:** 2027-01-16 - 2027-06-15

| ID | Zadanie | Data rozpoczęcia | Data zakończenia | Kamień milowy | Zasoby | Obszar kosztów |
|---|---|---|---|---|---|---|
| E4.1 | 📋 Wdrożenie CRM | 2027-01-16 | 2027-03-15 | ❌ | PM + Marketing | CRM + narzędzie e-mail marketingu |
| E4.2 | 📋 Import dotychczasowych kontaktów | 2027-03-16 | 2027-04-15 | ❌ | Marketing | CRM + narzędzie e-mail marketingu |
| E4.3 | 📋 Uruchomienie programu lojalnościowego (kody rabatowe) | 2027-04-16 | 2027-05-15 | ❌ | Marketing + PM | CRM + narzędzie e-mail marketingu |
| E4.4 | 🎯 Automatyczne e-maile przed/po pobycie | 2027-05-16 | 2027-06-15 | ✅ | Marketing | CRM + narzędzie e-mail marketingu |

**Zależności:**
- **E4.1** zależy od: E2.5
- **E4.2** zależy od: E4.1
- **E4.3** zależy od: E4.2
- **E4.4** zależy od: E4.1, E4.3

---

## E5 - Analityka i dynamic pricing

**Okres:** 2027-06-16 - 2027-11-15

| ID | Zadanie | Data rozpoczęcia | Data zakończenia | Kamień milowy | Zasoby | Obszar kosztów |
|---|---|---|---|---|---|---|
| E5.1 | 📋 Konfiguracja raportów (obłożenie, kanały, RevPAR) | 2027-06-16 | 2027-08-15 | ❌ | PM + Zarząd | Szkolenia i konsultacje |
| E5.2 | 📋 Wdrożenie zasad dynamicznego ustalania cen | 2027-08-16 | 2027-10-15 | ❌ | PM + Revenue Manager | PMS + booking engine + channel manager |
| E5.3 | 🎯 Szkolenia z analityki i pracy na danych | 2027-10-16 | 2027-11-15 | ✅ | Szkoleniowiec zewnętrzny + PM | Szkolenia i konsultacje |

**Zależności:**
- **E5.1** zależy od: E3.5
- **E5.2** zależy od: E5.1
- **E5.3** zależy od: E5.2

---

## E6 - Optymalizacja i rozwój

**Okres:** 2027-11-16 - 2028-02-15

| ID | Zadanie | Data rozpoczęcia | Data zakończenia | Kamień milowy | Zasoby | Obszar kosztów |
|---|---|---|---|---|---|---|
| E6.1 | 📋 Przegląd KPI z IT BSC | 2027-11-16 | 2027-12-15 | ❌ | PM + Zarząd | Szkolenia i konsultacje |
| E6.2 | 📋 Korekta procesów | 2027-12-16 | 2028-01-15 | ❌ | PM + Właściciel procesów | Szkolenia i konsultacje |
| E6.3 | 🎯 Decyzja o dalszych inwestycjach (chatbot, kolejne integracje) | 2028-01-16 | 2028-02-15 | ✅ | Zarząd + PM | Sprzęt / Rozwiązania SaaS (wg potrzeb) |

**Zależności:**
- **E6.1** zależy od: E5.1
- **E6.2** zależy od: E6.1
- **E6.3** zależy od: E6.2

---

## 🎯 Kamienie Milowe

| Data | Etap | Kamień milowy |
|---|---|---|
| 2026-01-15 | E1 | Formalne uruchomienie programu |
| 2026-09-30 | E2 | Finalizacja strony www i identyfikacji |
| 2027-01-15 | E3 | Start produkcyjny systemu rezerwacji |
| 2027-06-15 | E4 | Automatyczne e-maile przed/po pobycie |
| 2027-11-15 | E5 | Szkolenia z analityki i pracy na danych |
| 2028-02-15 | E6 | Decyzja o dalszych inwestycjach (chatbot, kolejne integracje) |

---

## 👥 Zasoby

**Dostawca PMS:**
- E3.1 (2026-10 - 2026-10)
- E3.2 (2026-11 - 2026-11)
- E3.3 (2026-11 - 2026-12)

**Dostawca WWW:**
- E2.1 (2026-04 - 2026-05)
- E2.2 (2026-04 - 2026-05)
- E2.3 (2026-06 - 2026-08)

**IT:**
- E1.2 (2026-01 - 2026-02)
- E1.4 (2026-02 - 2026-03)

**Marketing:**
- E1.4 (2026-02 - 2026-03)
- E2.1 (2026-04 - 2026-05)
- E2.2 (2026-04 - 2026-05)
- E2.4 (2026-07 - 2026-09)
- E2.5 (2026-09 - 2026-09)
- E4.1 (2027-01 - 2027-03)
- E4.2 (2027-03 - 2027-04)
- E4.3 (2027-04 - 2027-05)
- E4.4 (2027-05 - 2027-06)

**PM:**
- E1.2 (2026-01 - 2026-02)
- E1.3 (2026-02 - 2026-02)
- E1.4 (2026-02 - 2026-03)
- E2.1 (2026-04 - 2026-05)
- E2.3 (2026-06 - 2026-08)
- E2.5 (2026-09 - 2026-09)
- E3.1 (2026-10 - 2026-10)
- E3.2 (2026-11 - 2026-11)
- E3.3 (2026-11 - 2026-12)
- E3.4 (2026-12 - 2026-12)
- E3.5 (2027-01 - 2027-01)
- E4.1 (2027-01 - 2027-03)
- E4.3 (2027-04 - 2027-05)
- E5.1 (2027-06 - 2027-08)
- E5.2 (2027-08 - 2027-10)
- E5.3 (2027-10 - 2027-11)
- E6.1 (2027-11 - 2027-12)
- E6.2 (2027-12 - 2028-01)
- E6.3 (2028-01 - 2028-02)

**Recepcja:**
- E3.4 (2026-12 - 2026-12)
- E3.5 (2027-01 - 2027-01)

**Revenue Manager:**
- E5.2 (2027-08 - 2027-10)

**Szkoleniowiec zewnętrzny:**
- E5.3 (2027-10 - 2027-11)

**Właściciel procesów:**
- E6.2 (2027-12 - 2028-01)

**Zarząd:**
- E1.1 (2026-01 - 2026-01)
- E1.3 (2026-02 - 2026-02)
- E5.1 (2027-06 - 2027-08)
- E6.1 (2027-11 - 2027-12)
- E6.3 (2028-01 - 2028-02)

**Zarząd / Właściciel:**
- E1.1 (2026-01 - 2026-01)

**operator płatności:**
- E3.2 (2026-11 - 2026-11)

## 💰 Obszary Kosztów

**CRM + narzędzie e-mail marketingu**
- Zadania: E4.1, E4.2, E4.3, E4.4
- Okres: 2027-01-16 - 2027-06-15

**Nowa strona www + identyfikacja**
- Zadania: E2.1, E2.2, E2.3, E2.4, E2.5
- Okres: 2026-04-01 - 2026-09-30

**PMS + booking engine + channel manager**
- Zadania: E1.4, E3.1, E3.2, E3.3, E3.4, E3.5, E5.2
- Okres: 2026-02-15 - 2027-10-15

**Sprzęt / Rozwiązania SaaS (wg potrzeb)**
- Zadania: E6.3
- Okres: 2028-01-16 - 2028-02-15

**Szkolenia i konsultacje**
- Zadania: E1.1, E1.2, E1.3, E5.1, E5.3, E6.1, E6.2
- Okres: 2026-01-01 - 2028-01-15

