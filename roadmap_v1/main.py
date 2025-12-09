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
    
    # Eksportuj do CSV
    export_to_csv(ROADMAP_ITEMS)
    
    # Eksportuj do Markdown
    export_to_markdown(ROADMAP_ITEMS)
    
    # Wyświetl podsumowanie w konsoli
    print_roadmap_summary(ROADMAP_ITEMS)