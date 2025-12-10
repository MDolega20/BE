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
    key_actions: List[str]
    main_results: List[str]


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
        key_actions=[
            "formalne uruchomienie programu",
            "inwentaryzacja obecnych narzędzi",
            "określenie budżetu IT na 2026",
            "wybór dostawcy PMS/booking engine i wstępny brief dla nowej strony www"
        ],
        main_results=[
            "jasny zakres programu",
            "wstępnie wybrani dostawcy",
            "projekt planu wdrożeń"
        ],
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
        key_actions=[
            "projekt i wdrożenie nowej strony www",
            "przygotowanie logo i szablonów graficznych",
            "aktualizacja treści i zdjęć",
            "SEO podstawowe"
        ],
        main_results=[
            "nowa strona www ukierunkowana na rezerwacje",
            "spójna identyfikacja online (I2, I9)"
        ],
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
        key_actions=[
            "uruchomienie booking engine i płatności online",
            "integracja z OTA (channel manager)",
            "testy procesu rezerwacji"
        ],
        main_results=[
            "pełna możliwość rezerwacji online",
            "brak podwójnych rezerwacji",
            "wstępna realizacja I1"
        ],
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
        key_actions=[
            "wdrożenie CRM",
            "import dotychczasowych kontaktów",
            "uruchomienie programu lojalnościowego (kody rabatowe) i automatycznych e-maili przed/po pobycie"
        ],
        main_results=[
            "baza klientów w CRM",
            "pierwsze kampanie e-mail",
            "realizacja I7-I8"
        ],
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
        key_actions=[
            "konfiguracja raportów (obłożenie, kanały, RevPAR)",
            "wdrożenie zasad dynamicznego ustalania cen",
            "szkolenia z analityki"
        ],
        main_results=[
            "regularne raporty miesięczne",
            "realizacja I3 i I6",
            "lepsza kontrola przychodów"
        ],
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
        key_actions=[
            "przegląd KPI z IT BSC",
            "korekta procesów",
            "decyzja o dalszych inwestycjach (np. chatbot, integracje z dodatkowymi kanałami)"
        ],
        main_results=[
            "ustabilizowane systemy",
            "dalsza poprawa udziału rezerwacji bezpośrednich i rentowności"
        ],
    ),
]


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

def plot_detailed_gantt(items: List[RoadmapItem], filename: str = "roadmap_wedrowiec_szczegolowy.png") -> None:
    """
    Rysuje szczegółowy wykres Gantta z każdym działaniem jako osobnym elementem.
    """
    items_sorted = sorted(items, key=lambda x: x.start)

    # Obliczenie liczby wierszy potrzebnych dla każdego etapu
    max_items_per_stage = 0
    for item in items_sorted:
        total_items = len(item.key_actions) + len(item.main_results)
        max_items_per_stage = max(max_items_per_stage, total_items)
    
    # Wysokość dla każdego etapu: główna belka + działania + rezultaty + margines
    stage_height = max_items_per_stage + 2
    total_height = len(items_sorted) * stage_height

    fig, ax = plt.subplots(figsize=(20, max(12, total_height * 0.5)))

    # Kolory dla różnych etapów
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3']
    
    current_y = 0
    y_ticks = []
    y_labels = []
    
    for i, item in enumerate(items_sorted):
        start_num = mdates.date2num(item.start)
        end_num = mdates.date2num(item.end)
        duration = end_num - start_num
        
        # Główna belka etapu
        main_y = current_y
        ax.barh(
            y=main_y,
            width=duration,
            left=start_num,
            height=0.8,
            color=colors[i % len(colors)],
            alpha=0.9,
            edgecolor='black',
            linewidth=1.5
        )

        # ID i nazwa etapu na belce
        ax.text(
            start_num + duration/2,
            main_y,
            f"{item.id}",
            va="center",
            ha="center",
            fontweight='bold',
            color='white',
            fontsize=11
        )
        
        # Etykieta głównego etapu
        start_q = f"Q{((item.start.month-1)//3)+1} {item.start.year}"
        end_q = f"Q{((item.end.month-1)//3)+1} {item.end.year}"
        period = start_q if start_q == end_q else f"{start_q}-{end_q}"
        
        y_ticks.append(main_y)
        y_labels.append(f"{item.id} - {item.name}\n({period})")
        
        current_y += 1.5  # Odstęp po głównej belce
        
        # Działania - każde jako osobny element
        for j, action in enumerate(item.key_actions):
            action_y = current_y + j * 0.6
            
            # Mniejsza belka dla działania
            ax.barh(
                y=action_y,
                width=duration * 0.7,  # Krótsza niż główna belka
                left=start_num,
                height=0.4,
                color=colors[i % len(colors)],
                alpha=0.4,
                edgecolor='gray',
                linewidth=0.5
            )
            
            # Tekst działania
            ax.text(
                start_num - timedelta(days=5).days,
                action_y,
                f"• {action}",
                va="center",
                ha="right",
                fontsize=8,
                color='#333333'
            )
        
        if item.key_actions:
            current_y += len(item.key_actions) * 0.6 + 0.3
        
        # Rezultaty - każdy jako osobny element  
        for j, result in enumerate(item.main_results):
            result_y = current_y + j * 0.6
            
            # Mniejsza belka dla rezultatu
            ax.barh(
                y=result_y,
                width=duration * 0.7,
                left=start_num + duration * 0.3,  # Przesunięta w prawo
                height=0.4,
                color='#90EE90',
                alpha=0.6,
                edgecolor='green',
                linewidth=0.5
            )
            
            # Tekst rezultatu
            ax.text(
                end_num + timedelta(days=5).days,
                result_y,
                f"• {result}",
                va="center",
                ha="left",
                fontsize=8,
                color='#006400'
            )
        
        if item.main_results:
            current_y += len(item.main_results) * 0.6 + 1.5
        else:
            current_y += 1.5
    
    # Ustawienie osi Y
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels, fontsize=10, fontweight='bold')
    ax.set_ylim(-1, current_y + 1)

    # Zakres osi X - szerszy dla tekstów
    min_start = min(item.start for item in items_sorted)
    max_end = max(item.end for item in items_sorted)
    left = mdates.date2num(min_start - timedelta(days=90))
    right = mdates.date2num(max_end + timedelta(days=90))
    ax.set_xlim(left, right)

    # Formatowanie osi X
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.xticks(rotation=45)

    # Linie separujące etapy
    separator_positions = []
    current_pos = 0
    for item in items_sorted:
        total_items = len(item.key_actions) + len(item.main_results)
        section_height = max(total_items * 0.6 + 3, 4)  # Minimum 4 dla czytelności
        current_pos += section_height
        separator_positions.append(current_pos - 0.5)
    
    for pos in separator_positions[:-1]:  # Bez ostatniej linii
        ax.axhline(y=pos, color='gray', linestyle='-', linewidth=1, alpha=0.6)

    plt.xlabel("Czas", fontsize=12, fontweight='bold')
    plt.title('Szczegółowa roadmapa transformacji cyfrowej "Wędrowiec" (2025–2027)\nKażde działanie jako osobny element', 
              fontsize=16, fontweight='bold', pad=20)
    
    # Siatka tylko na osi X
    ax.grid(axis="x", linestyle="--", linewidth=0.5, alpha=0.7)
    ax.set_axisbelow(True)
    
    # Większe marginesy
    plt.tight_layout()
    plt.subplots_adjust(left=0.2, right=0.85, top=0.90, bottom=0.15)

    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)

    print(f"Zapisano szczegółowy wykres Gantta do pliku: {filename}")

def export_to_csv(items: List[RoadmapItem], filename: str = "roadmap_szczegoly.csv") -> None:
    """
    Eksportuje szczegółową roadmapę do pliku CSV.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Etap', 'Nazwa', 'Horyzont czasowy', 'Data start', 'Data koniec', 
                     'Kluczowe działania', 'Główne rezultaty', 'Opis']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in items:
            start_q = f"Q{((item.start.month-1)//3)+1} {item.start.year}"
            end_q = f"Q{((item.end.month-1)//3)+1} {item.end.year}"
            period = start_q if start_q == end_q else f"{start_q}-{end_q}"
            
            writer.writerow({
                'Etap': item.id,
                'Nazwa': item.name,
                'Horyzont czasowy': period,
                'Data start': item.start.strftime('%Y-%m-%d'),
                'Data koniec': item.end.strftime('%Y-%m-%d'),
                'Kluczowe działania': ' • ' + ' • '.join(item.key_actions),
                'Główne rezultaty': ' • ' + ' • '.join(item.main_results),
                'Opis': item.description
            })
    
    print(f"Wyeksportowano szczegóły do pliku: {filename}")

def export_to_markdown(items: List[RoadmapItem], filename: str = "roadmap_tabela.md") -> None:
    """
    Eksportuje roadmapę do tabeli w formacie Markdown.
    """
    with open(filename, 'w', encoding='utf-8') as mdfile:
        mdfile.write("# Roadmapa transformacji cyfrowej \"Wędrowiec\" (2025-2027)\n\n")
        
        # Tabela główna
        mdfile.write("| **Etap** | **Horyzont czasowy** | **Kluczowe działania** | **Główne rezultaty** |\n")
        mdfile.write("| --- | --- | --- | --- |\n")
        
        for item in sorted(items, key=lambda x: x.start):
            start_q = f"Q{((item.start.month-1)//3)+1} {item.start.year}"
            end_q = f"Q{((item.end.month-1)//3)+1} {item.end.year}"
            period = start_q if start_q == end_q else f"{start_q}-{end_q}"
            
            # Formatowanie działań
            actions = '<br>'.join([f"• {action}" for action in item.key_actions])
            
            # Formatowanie rezultatów
            results = '<br>'.join([f"• {result}" for result in item.main_results])
            
            mdfile.write(f"| **{item.id} - {item.name}** | **{period}** | {actions} | {results} |\n")
        
        mdfile.write("\n## Szczegółowe opisy etapów\n\n")
        
        for item in sorted(items, key=lambda x: x.start):
            start_q = f"Q{((item.start.month-1)//3)+1} {item.start.year}"
            end_q = f"Q{((item.end.month-1)//3)+1} {item.end.year}"
            period = start_q if start_q == end_q else f"{start_q}-{end_q}"
            
            mdfile.write(f"### {item.id} - {item.name} ({period})\n\n")
            mdfile.write(f"**Stream:** {item.stream}\n\n")
            mdfile.write(f"**Czas trwania:** {item.start.strftime('%d.%m.%Y')} - {item.end.strftime('%d.%m.%Y')}\n\n")
            mdfile.write(f"**Opis:** {item.description}\n\n")
            
            mdfile.write("**Kluczowe działania:**\n")
            for action in item.key_actions:
                mdfile.write(f"- {action}\n")
            
            mdfile.write("\n**Główne rezultaty:**\n")
            for result in item.main_results:
                mdfile.write(f"- {result}\n")
            
            mdfile.write("\n---\n\n")
    
    print(f"Wyeksportowano tabelę Markdown do pliku: {filename}")

def generate_clean_roadmap_table(tasks=None, filename_prefix="roadmap_clean_table"):
    """
    Generuje czytelną roadmapę w stylu tabelarycznym z konkretnymi zadaniami z harmonogramu
    """
    # Definicja struktrury tabeli z precyzyjnymi przedziałami
    columns = [
        "Przygotowania\n2025-10-01 do 2025-12-31",
        "Podstawowa infrastruktura\n2026-01-01 do 2026-09-30", 
        "System rezerwacji\n2026-10-01 do 2027-01-15",
        "Infrastruktura relacyjna\n2027-01-16 do 2027-06-15",
        "Analityka i rozwój\n2027-06-16 do 2028-02-15"
    ]
    
    rows = [
        {"id": 0, "title": "Poziom 0 – Stan wyjściowy", "color": "#4472C4"},
        {"id": 1, "title": "Poziom 1 – Podstawowa infrastruktura rezerwacyjna", "color": "#E97132"},
        {"id": 2, "title": "Poziom 2 – Infrastruktura relacyjna", "color": "#70AD47"},
        {"id": 3, "title": "Poziom 3 – Infrastruktura analityczna i rozwojowa", "color": "#C55A5A"}
    ]
    
    # Zawartość komórek - konkretne zadania z harmonogramu
    cell_content = {
        (0, 0): [  # Poziom 0, Przygotowania
            {
                "text": "Brak PMS/CRM\nTylko OTA + Excel\nBrak integracji",
                "color": "#4472C4"
            },
            {
                "text": "Inwentaryzacja narzędzi\nOcena łącza i sprzętu\nIdentyfikacja luk",
                "color": "#4472C4"
            }
        ],
        (1, 1): [  # Poziom 1, Podstawowa infrastruktura (2026-01-01 do 2026-09-30)
            {
                "text": "E1.1: Formalne uruchomienie programu\n(2026-01-01 do 2026-01-15) 🎯",
                "color": "#E97132"
            },
            {
                "text": "E1.2: Inwentaryzacja obecnych narzędzi\n(2026-01-16 do 2026-02-28)",
                "color": "#E97132"
            },
            {
                "text": "E1.3: Określenie budżetu IT\n(2026-02-01 do 2026-02-28)",
                "color": "#E97132"
            },
            {
                "text": "E1.4: Wybór dostawcy PMS/booking engine\n(2026-02-15 do 2026-03-31)",
                "color": "#E97132"
            },
            {
                "text": "E2.1: Projekt nowej strony www\n(2026-04-01 do 2026-05-31)",
                "color": "#E97132"
            },
            {
                "text": "E2.2: Logo i szablony graficzne\n(2026-04-01 do 2026-05-15)",
                "color": "#E97132"
            },
            {
                "text": "E2.3: Wdrożenie nowej strony www\n(2026-06-01 do 2026-08-31)",
                "color": "#E97132"
            },
            {
                "text": "E2.4: Treści i zdjęcia + SEO\n(2026-07-01 do 2026-09-30)",
                "color": "#E97132"
            },
            {
                "text": "E2.5: Finalizacja strony www\n(2026-09-01 do 2026-09-30) 🎯",
                "color": "#E97132"
            }
        ],
        (1, 2): [  # Poziom 1, System rezerwacji (2026-10-01 do 2027-01-15)
            {
                "text": "E3.1: Uruchomienie booking engine\n(2026-10-01 do 2026-10-31)",
                "color": "#E97132"
            },
            {
                "text": "E3.2: Uruchomienie płatności online\n(2026-11-01 do 2026-11-30)",
                "color": "#E97132"
            },
            {
                "text": "E3.3: Integracja z OTA\n(2026-11-01 do 2026-12-15)",
                "color": "#E97132"
            },
            {
                "text": "E3.4: Testy procesu rezerwacji\n(2026-12-01 do 2026-12-31)",
                "color": "#E97132"
            },
            {
                "text": "E3.5: Start produkcyjny systemu\n(2027-01-01 do 2027-01-15) 🎯",
                "color": "#E97132"
            }
        ],
        (2, 3): [  # Poziom 2, Infrastruktura relacyjna (2027-01-16 do 2027-06-15)
            {
                "text": "E4.1: Wdrożenie CRM\n(2027-01-16 do 2027-03-15)",
                "color": "#70AD47"
            },
            {
                "text": "E4.2: Import dotychczasowych kontaktów\n(2027-03-16 do 2027-04-15)",
                "color": "#70AD47"
            },
            {
                "text": "E4.3: Program lojalnościowy\n(2027-04-16 do 2027-05-15)",
                "color": "#70AD47"
            },
            {
                "text": "E4.4: Automatyczne e-maile\n(2027-05-16 do 2027-06-15) 🎯",
                "color": "#70AD47"
            }
        ],
        (3, 4): [  # Poziom 3, Analityka i rozwój (2027-06-16 do 2028-02-15)
            {
                "text": "E5.1: Konfiguracja raportów\n(2027-06-16 do 2027-08-15)",
                "color": "#C55A5A"
            },
            {
                "text": "E5.2: Dynamic pricing\n(2027-08-16 do 2027-10-15)",
                "color": "#C55A5A"
            },
            {
                "text": "E5.3: Szkolenia z analityki\n(2027-10-16 do 2027-11-15) 🎯",
                "color": "#C55A5A"
            },
            {
                "text": "E6.1: Przegląd KPI z IT BSC\n(2027-11-16 do 2027-12-15)",
                "color": "#C55A5A"
            },
            {
                "text": "E6.2: Korekta procesów\n(2027-12-16 do 2028-01-15)",
                "color": "#C55A5A"
            },
            {
                "text": "E6.3: Decyzje o dalszych inwestycjach\n(2028-01-16 do 2028-02-15) 🎯",
                "color": "#C55A5A"
            }
        ]
    }
    
    # Utworzenie figury
    fig, ax = plt.subplots(figsize=(20, 14))
    ax.set_xlim(0, len(columns))
    ax.set_ylim(0, len(rows) + 0.5)  # Dodatkowe miejsce na daty
    
    # Pokazanie osi X z precyzyjnymi datami
    ax.set_xticks([i + 0.5 for i in range(len(columns))])
    ax.set_xticklabels([
        "2025-10-01\ndo\n2025-12-31",
        "2026-01-01\ndo\n2026-09-30",
        "2026-10-01\ndo\n2027-01-15",
        "2027-01-16\ndo\n2027-06-15",
        "2027-06-16\ndo\n2028-02-15"
    ], rotation=0, fontsize=10, ha='center')
    
    # Ukrycie osi Y ale pokazanie X
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(True)  # Pokazujemy dolną oś dla dat
    ax.tick_params(axis='x', which='both', bottom=True, top=False)
    
    # Rysowanie nagłówków kolumn (turkusowe)
    for i, col_title in enumerate(columns):
        ax.add_patch(plt.Rectangle((i, len(rows)-0.15), 1, 0.15, 
                                 facecolor='#17A2B8', alpha=0.9, edgecolor='white', linewidth=2))
        col_text = col_title.split('\n')[0]  # Tylko pierwsza linia dla nagłówka
        ax.text(i + 0.5, len(rows) - 0.075, col_text, 
               ha='center', va='center', fontsize=11, fontweight='bold', color='white')
    
    # Rysowanie nagłówków wierszy (kolorowe)
    for j, row_info in enumerate(rows):
        row_idx = len(rows) - 1 - j  # Odwracamy kolejność (Poziom 0 na górze)
        ax.text(-0.05, row_idx + 0.5, row_info['title'], 
               ha='right', va='center', fontsize=10, fontweight='bold', 
               color=row_info['color'])
    
    # Rysowanie siatki i zawartości komórek
    for i in range(len(columns)):
        for j in range(len(rows)):
            # Współrzędne komórki
            x, y = i, len(rows) - 1 - j
            
            # Rysowanie białej komórki z lekką ramką
            ax.add_patch(plt.Rectangle((x, y), 1, 1, 
                                     facecolor='white', edgecolor='#E0E0E0', linewidth=1))
            
            # Dodawanie prostokątów z opisami
            if (j, i) in cell_content:
                pills = cell_content[(j, i)]
                pill_height = 0.12
                pill_margin = 0.03
                start_y = y + 0.85
                
                for idx, pill in enumerate(pills):
                    pill_y = start_y - idx * (pill_height + pill_margin)
                    
                    # Rysowanie zaokrąglonego prostokąta (pill)
                    from matplotlib.patches import FancyBboxPatch
                    pill_rect = FancyBboxPatch(
                        (x + 0.03, pill_y - pill_height/2), 0.94, pill_height,
                        boxstyle="round,pad=0.01",
                        facecolor=pill['color'],
                        alpha=0.85,
                        edgecolor='white',
                        linewidth=1
                    )
                    ax.add_patch(pill_rect)
                    
                    # Dodawanie tekstu do prostokąta
                    ax.text(x + 0.5, pill_y, pill['text'],
                           ha='center', va='center', fontsize=7.5,
                           color='white', fontweight='bold',
                           wrap=True)
    
    # Tytuł całej roadmapy
    ax.text(len(columns)/2, len(rows) + 0.4, 
           "Roadmapa Digitalizacji Hotelu - Szczegółowy Harmonogram",
           ha='center', va='center', fontsize=18, fontweight='bold', color='#2C3E50')
    
    # Podtytuł
    ax.text(len(columns)/2, len(rows) + 0.25, 
           "Konkretne zadania według precyzyjnych przedziałów czasowych",
           ha='center', va='center', fontsize=14, color='#34495E')
    
    # Etykieta osi X
    ax.set_xlabel("Precyzyjne okresy realizacji", fontsize=12, fontweight='bold', color='#2C3E50')
    
    plt.tight_layout()
    
    # Zapisanie do plików
    plt.savefig(f"{filename_prefix}.png", dpi=300, bbox_inches="tight", 
               facecolor='white', edgecolor='none')
    plt.savefig(f"{filename_prefix}.pdf", bbox_inches="tight", 
               facecolor='white', edgecolor='none')
    
    print(f"Zapisano czytelną roadmapę tabelaryczną do pliku: {filename_prefix}.png")
    print(f"Zapisano czytelną roadmapę tabelaryczną do pliku: {filename_prefix}.pdf")
    
    return fig, ax

def print_roadmap_summary(items: List[RoadmapItem]) -> None:
    """
    Wyświetla podsumowanie roadmapy w konsoli.
    """
    print("\n" + "="*80)
    print("ROADMAPA TRANSFORMACJI CYFROWEJ 'WĘDROWIEC' (2025-2027)")
    print("="*80)
    
    for item in sorted(items, key=lambda x: x.start):
        start_q = f"Q{((item.start.month-1)//3)+1} {item.start.year}"
        end_q = f"Q{((item.end.month-1)//3)+1} {item.end.year}"
        period = start_q if start_q == end_q else f"{start_q}-{end_q}"
        
        print(f"\n{item.id} - {item.name} ({period})")
        print("-" * 50)
        
        print("Kluczowe działania:")
        for action in item.key_actions:
            print(f"  • {action}")
            
        print("Główne rezultaty:")
        for result in item.main_results:
            print(f"  • {result}")

# --- 4. Główna funkcja --- #

if __name__ == "__main__":
    # Generuj podstawowy wykres Gantta
    plot_gantt(ROADMAP_ITEMS)
    
    # Generuj szczegółowy wykres Gantta
    plot_detailed_gantt(ROADMAP_ITEMS)
    
    # Generuj czytelną roadmapę tabelaryczną z konkretnymi zadaniami
    generate_clean_roadmap_table(ROADMAP_ITEMS)
    
    # Eksportuj do CSV
    export_to_csv(ROADMAP_ITEMS)
    
    # Eksportuj do Markdown
    export_to_markdown(ROADMAP_ITEMS)
    
    # Wyświetl podsumowanie w konsoli
    print_roadmap_summary(ROADMAP_ITEMS)