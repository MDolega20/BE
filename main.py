from dataclasses import dataclass, asdict
from datetime import date
from typing import List
import csv

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import timedelta


# --- 1. Definicja struktury danych --- #

@dataclass
class RoadmapItem:
    id: str
    name: str
    stream: str
    start: date
    end: date
    description: str


ROADMAP_ITEMS: List[RoadmapItem] = [
    RoadmapItem(
        id="E1",
        name="Start i przygotowanie",
        stream="S1 - Ład IT i zarządzanie inicjatywą",
        start=date(2025, 10, 1),      # Q4 2025
        end=date(2025, 12, 31),
        description=(
            "Formalne uruchomienie programu, inwentaryzacja narzędzi, "
            "określenie budżetu IT 2026, wybór PMS/booking engine i brief nowej strony www."
        ),
    ),
    RoadmapItem(
        id="E2",
        name="Strona www + identyfikacja",
        stream="S2 - Kanały sprzedaży cyfrowej",
        start=date(2026, 1, 1),       # Q1 2026
        end=date(2026, 6, 30),        # Q2 2026
        description=(
            "Projekt i wdrożenie nowej responsywnej strony www, nowe logo, szablony graficzne, "
            "aktualizacja treści, zdjęć oraz podstawowe SEO."
        ),
    ),
    RoadmapItem(
        id="E3",
        name="System rezerwacji i płatności",
        stream="S2 - Kanały sprzedaży cyfrowej",
        start=date(2026, 4, 1),       # Q2 2026
        end=date(2026, 9, 30),        # Q3 2026
        description=(
            "Uruchomienie booking engine oraz płatności online, integracja z OTA przez channel manager, "
            "testy procesu rezerwacji end-to-end."
        ),
    ),
    RoadmapItem(
        id="E4",
        name="CRM i lojalność",
        stream="S3 - Relacje z klientami i lojalność",
        start=date(2026, 7, 1),       # Q3 2026
        end=date(2026, 12, 31),       # Q4 2026
        description=(
            "Wdrożenie CRM, import dotychczasowych kontaktów, uruchomienie programu lojalnościowego "
            "oraz automatycznych wiadomości e-mail przed i po pobycie."
        ),
    ),
    RoadmapItem(
        id="E5",
        name="Analityka i dynamic pricing",
        stream="S5 - Analityka i zarządzanie przychodem",
        start=date(2026, 10, 1),      # Q4 2026
        end=date(2027, 6, 30),        # Q2 2027
        description=(
            "Konfiguracja raportów (obłożenie, ADR, RevPAR, udział kanałów), wdrożenie zasad "
            "dynamicznego ustalania cen oraz szkolenia z analityki."
        ),
    ),
    RoadmapItem(
        id="E6",
        name="Optymalizacja i rozwój",
        stream="S1/S2/S3/S5 - Optymalizacja",
        start=date(2027, 7, 1),       # Q3 2027
        end=date(2027, 12, 31),       # Q4 2027
        description=(
            "Przegląd KPI z IT BSC, korekty procesów i konfiguracji systemów, decyzje o dalszych "
            "inwestycjach (np. chatbot AI, dodatkowe integracje kanałów)."
        ),
    ),
]


# --- 2. Eksport roadmapy do CSV --- #

def export_to_csv(items: List[RoadmapItem], filename: str = "roadmap_wedrowiec.csv") -> None:
    """
    Zapisuje roadmapę do pliku CSV, który można otworzyć w Excelu, Google Sheets
    albo zaimportować do narzędzi typu Miro / FigJam jako dane.
    """
    fieldnames = ["id", "name", "stream", "start", "end", "description"]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            row = asdict(item)
            # Daty zapisujemy w formacie RRRR-MM-DD
            row["start"] = item.start.isoformat()
            row["end"] = item.end.isoformat()
            writer.writerow(row)

    print(f"Zapisano roadmapę do pliku: {filename}")


# --- 3. Rysowanie prostego wykresu Gantta --- #
#     """
#     Rysuje prosty wykres Gantta (poziome słupki) dla etapów roadmapy
#     i zapisuje go do pliku PNG.
#     """
#     # Sortujemy po dacie startu, żeby wykres był czytelny
#     items_sorted = sorted(items, key=lambda x: x.start)

#     fig, ax = plt.subplots(figsize=(10, 5))

#     # Oś Y – nazwy etapów
#     y_positions = range(len(items_sorted))

#     for i, item in enumerate(items_sorted):
#         start_num = mdates.date2num(item.start)
#         end_num = mdates.date2num(item.end)
#         duration = end_num - start_num

#         ax.barh(
#             y=i,
#             width=duration,
#             left=start_num,
#         )

#         # Podpis ID etapu na belce
#         ax.text(
#             start_num,
#             i,
#             f" {item.id}",
#             va="center",
#             ha="left",
#         )

#     # Opis osi Y
#     ax.set_yticks(list(y_positions))
#     ax.set_yticklabels([f"{item.name}" for item in items_sorted])

#     # Formatowanie osi X jako dat
#     ax.xaxis_date()
#     ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # co kwartał
#     ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

#     plt.xlabel("Czas")
#     plt.title('Roadmapa transformacji cyfrowej "Wędrowiec" (2025–2027)')
#     plt.tight_layout()
#     plt.grid(axis="x", linestyle="--", linewidth=0.5)

#     plt.savefig(filename, dpi=150)
#     plt.close(fig)

#     print(f"Zapisano wykres Gantta do pliku: {filename}")

def plot_gantt(items: List[RoadmapItem], filename: str = "roadmap_wedrowiec.png") -> None:
    """
    Rysuje wykres Gantta dla etapów roadmapy i zapisuje go do pliku PNG.
    Poprawiona wersja:
    - ręcznie ustawia zakres osi X, żeby nic nie było ucięte,
    - pokazuje na osi Y ID + nazwę etapu.
    """
    # Sortujemy po dacie startu, żeby wykres był czytelny
    items_sorted = sorted(items, key=lambda x: x.start)

    fig, ax = plt.subplots(figsize=(10, 5))

    y_positions = range(len(items_sorted))

    for i, item in enumerate(items_sorted):
        start_num = mdates.date2num(item.start)
        end_num = mdates.date2num(item.end)
        duration = end_num - start_num

        ax.barh(
            y=i,
            width=duration,
            left=start_num,
        )

        # Podpis ID na słupku
        ax.text(
            start_num,
            i,
            f" {item.id}",
            va="center",
            ha="left",
        )

    # Opisy osi Y: ID + nazwa
    ax.set_yticks(list(y_positions))
    ax.set_yticklabels([f"{item.id} – {item.name}" for item in items_sorted])

    # Zakres osi X: od najwcześniejszego startu do najpóźniejszego końca + margines
    min_start = min(item.start for item in items_sorted)
    max_end = max(item.end for item in items_sorted)

    left = mdates.date2num(min_start - timedelta(days=15))
    right = mdates.date2num(max_end + timedelta(days=15))
    ax.set_xlim(left, right)

    # Formatowanie osi X (daty co kwartał)
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    plt.xlabel("Czas")
    plt.title('Roadmapa transformacji cyfrowej "Wędrowiec" (2025–2027)')
    plt.grid(axis="x", linestyle="--", linewidth=0.5)
    plt.tight_layout()

    plt.savefig(filename, dpi=150)
    plt.close(fig)

    print(f"Zapisano wykres Gantta do pliku: {filename}")

# --- 4. Główna funkcja --- #

if __name__ == "__main__":
    export_to_csv(ROADMAP_ITEMS)
    plot_gantt(ROADMAP_ITEMS)