from datetime import datetime

tasks = [
    # --- E1 - Start i przygotowanie (Q1 2026) ---
    {
        "id": "E1.1",
        "name": "Formalne uruchomienie programu",
        "phase": "E1 - Start i przygotowanie",
        "start": datetime(2026, 1, 1),
        "end": datetime(2026, 1, 15),
        "milestone": True,
        "dependencies": [],
        "resource": "Zarząd / Właściciel",
        "cost_area": "Szkolenia i konsultacje",
        "progress": 0,
    },
    {
        "id": "E1.2",
        "name": "Inwentaryzacja obecnych narzędzi",
        "phase": "E1 - Start i przygotowanie",
        "start": datetime(2026, 1, 16),
        "end": datetime(2026, 2, 28),
        "milestone": False,
        "dependencies": ["E1.1"],
        "resource": "PM + IT",
        "cost_area": "Szkolenia i konsultacje",
        "progress": 0,
    },
    {
        "id": "E1.3",
        "name": "Określenie budżetu IT na 2026-2027",
        "phase": "E1 - Start i przygotowanie",
        "start": datetime(2026, 2, 1),
        "end": datetime(2026, 2, 28),
        "milestone": False,
        "dependencies": ["E1.2"],
        "resource": "Zarząd + PM",
        "cost_area": "Szkolenia i konsultacje",
        "progress": 0,
    },
    {
        "id": "E1.4",
        "name": "Wybór dostawcy PMS/booking engine i wstępny brief nowej strony www",
        "phase": "E1 - Start i przygotowanie",
        "start": datetime(2026, 2, 15),
        "end": datetime(2026, 3, 31),
        "milestone": False,
        "dependencies": ["E1.2"],
        "resource": "PM + IT + Marketing",
        "cost_area": "PMS + booking engine + channel manager",
        "progress": 0,
    },
    # --- E2 - Strona www + identyfikacja (Q2-Q3 2026) ---
    {
        "id": "E2.1",
        "name": "Projekt nowej strony www",
        "phase": "E2 - Strona www + identyfikacja",
        "start": datetime(2026, 4, 1),
        "end": datetime(2026, 5, 31),
        "milestone": False,
        "dependencies": ["E1.4"],
        "resource": "PM + Marketing + Dostawca WWW",
        "cost_area": "Nowa strona www + identyfikacja",
        "progress": 0,
    },
    {
        "id": "E2.2",
        "name": "Przygotowanie logo i szablonów graficznych",
        "phase": "E2 - Strona www + identyfikacja",
        "start": datetime(2026, 4, 1),
        "end": datetime(2026, 5, 15),
        "milestone": False,
        "dependencies": ["E1.4"],
        "resource": "Marketing + Dostawca WWW",
        "cost_area": "Nowa strona www + identyfikacja",
        "progress": 0,
    },
    {
        "id": "E2.3",
        "name": "Wdrożenie nowej strony www",
        "phase": "E2 - Strona www + identyfikacja",
        "start": datetime(2026, 6, 1),
        "end": datetime(2026, 8, 31),
        "milestone": False,
        "dependencies": ["E2.1", "E2.2"],
        "resource": "Dostawca WWW + PM",
        "cost_area": "Nowa strona www + identyfikacja",
        "progress": 0,
    },
    {
        "id": "E2.4",
        "name": "Aktualizacja treści i zdjęć + podstawowe SEO",
        "phase": "E2 - Strona www + identyfikacja",
        "start": datetime(2026, 7, 1),
        "end": datetime(2026, 9, 30),
        "milestone": False,
        "dependencies": ["E2.1"],
        "resource": "Marketing",
        "cost_area": "Nowa strona www + identyfikacja",
        "progress": 0,
    },
    {
        "id": "E2.5",
        "name": "Finalizacja strony www i identyfikacji",
        "phase": "E2 - Strona www + identyfikacja",
        "start": datetime(2026, 9, 1),
        "end": datetime(2026, 9, 30),
        "milestone": True,
        "dependencies": ["E2.3", "E2.4"],
        "resource": "PM + Marketing",
        "cost_area": "Nowa strona www + identyfikacja",
        "progress": 0,
    },
    # --- E3 - System rezerwacji i płatności (Q3-Q4 2026) ---
    {
        "id": "E3.1",
        "name": "Uruchomienie booking engine",
        "phase": "E3 - System rezerwacji i płatności",
        "start": datetime(2026, 10, 1),
        "end": datetime(2026, 10, 31),
        "milestone": False,
        "dependencies": ["E1.4", "E2.5"],
        "resource": "Dostawca PMS + PM",
        "cost_area": "PMS + booking engine + channel manager",
        "progress": 0,
    },
    {
        "id": "E3.2",
        "name": "Uruchomienie płatności online",
        "phase": "E3 - System rezerwacji i płatności",
        "start": datetime(2026, 11, 1),
        "end": datetime(2026, 11, 30),
        "milestone": False,
        "dependencies": ["E3.1"],
        "resource": "Dostawca PMS + operator płatności",
        "cost_area": "PMS + booking engine + channel manager",
        "progress": 0,
    },
    {
        "id": "E3.3",
        "name": "Integracja z OTA (channel manager)",
        "phase": "E3 - System rezerwacji i płatności",
        "start": datetime(2026, 11, 1),
        "end": datetime(2026, 12, 15),
        "milestone": False,
        "dependencies": ["E3.1"],
        "resource": "Dostawca PMS",
        "cost_area": "PMS + booking engine + channel manager",
        "progress": 0,
    },
    {
        "id": "E3.4",
        "name": "Testy procesu rezerwacji",
        "phase": "E3 - System rezerwacji i płatności",
        "start": datetime(2026, 12, 1),
        "end": datetime(2026, 12, 31),
        "milestone": False,
        "dependencies": ["E3.2", "E3.3"],
        "resource": "Recepcja + PM",
        "cost_area": "PMS + booking engine + channel manager",
        "progress": 0,
    },
    {
        "id": "E3.5",
        "name": "Start produkcyjny systemu rezerwacji",
        "phase": "E3 - System rezerwacji i płatności",
        "start": datetime(2027, 1, 1),
        "end": datetime(2027, 1, 15),
        "milestone": True,
        "dependencies": ["E3.4"],
        "resource": "PM + Recepcja",
        "cost_area": "PMS + booking engine + channel manager",
        "progress": 0,
    },
    # --- E4 - CRM i lojalność (Q1-Q2 2027) ---
    {
        "id": "E4.1",
        "name": "Wdrożenie CRM",
        "phase": "E4 - CRM i lojalność",
        "start": datetime(2027, 1, 16),
        "end": datetime(2027, 3, 15),
        "milestone": False,
        "dependencies": ["E2.5"],
        "resource": "PM + Marketing",
        "cost_area": "CRM + narzędzie e-mail marketingu",
        "progress": 0,
    },
    {
        "id": "E4.2",
        "name": "Import dotychczasowych kontaktów",
        "phase": "E4 - CRM i lojalność",
        "start": datetime(2027, 3, 16),
        "end": datetime(2027, 4, 15),
        "milestone": False,
        "dependencies": ["E4.1"],
        "resource": "Marketing",
        "cost_area": "CRM + narzędzie e-mail marketingu",
        "progress": 0,
    },
    {
        "id": "E4.3",
        "name": "Uruchomienie programu lojalnościowego (kody rabatowe)",
        "phase": "E4 - CRM i lojalność",
        "start": datetime(2027, 4, 16),
        "end": datetime(2027, 5, 15),
        "milestone": False,
        "dependencies": ["E4.2"],
        "resource": "Marketing + PM",
        "cost_area": "CRM + narzędzie e-mail marketingu",
        "progress": 0,
    },
    {
        "id": "E4.4",
        "name": "Automatyczne e-maile przed/po pobycie",
        "phase": "E4 - CRM i lojalność",
        "start": datetime(2027, 5, 16),
        "end": datetime(2027, 6, 15),
        "milestone": True,
        "dependencies": ["E4.1", "E4.3"],
        "resource": "Marketing",
        "cost_area": "CRM + narzędzie e-mail marketingu",
        "progress": 0,
    },
    # --- E5 - Analityka i dynamic pricing (Q2-Q3 2027) ---
    {
        "id": "E5.1",
        "name": "Konfiguracja raportów (obłożenie, kanały, RevPAR)",
        "phase": "E5 - Analityka i dynamic pricing",
        "start": datetime(2027, 6, 16),
        "end": datetime(2027, 8, 15),
        "milestone": False,
        "dependencies": ["E3.5"],
        "resource": "PM + Zarząd",
        "cost_area": "Szkolenia i konsultacje",
        "progress": 0,
    },
    {
        "id": "E5.2",
        "name": "Wdrożenie zasad dynamicznego ustalania cen",
        "phase": "E5 - Analityka i dynamic pricing",
        "start": datetime(2027, 8, 16),
        "end": datetime(2027, 10, 15),
        "milestone": False,
        "dependencies": ["E5.1"],
        "resource": "PM + Revenue Manager",
        "cost_area": "PMS + booking engine + channel manager",
        "progress": 0,
    },
    {
        "id": "E5.3",
        "name": "Szkolenia z analityki i pracy na danych",
        "phase": "E5 - Analityka i dynamic pricing",
        "start": datetime(2027, 10, 16),
        "end": datetime(2027, 11, 15),
        "milestone": True,
        "dependencies": ["E5.2"],
        "resource": "Szkoleniowiec zewnętrzny + PM",
        "cost_area": "Szkolenia i konsultacje",
        "progress": 0,
    },
    # --- E6 - Optymalizacja i rozwój (Q3-Q4 2027) ---
    {
        "id": "E6.1",
        "name": "Przegląd KPI z IT BSC",
        "phase": "E6 - Optymalizacja i rozwój",
        "start": datetime(2027, 11, 16),
        "end": datetime(2027, 12, 15),
        "milestone": False,
        "dependencies": ["E5.1"],
        "resource": "PM + Zarząd",
        "cost_area": "Szkolenia i konsultacje",
        "progress": 0,
    },
    {
        "id": "E6.2",
        "name": "Korekta procesów",
        "phase": "E6 - Optymalizacja i rozwój",
        "start": datetime(2027, 12, 16),
        "end": datetime(2028, 1, 15),
        "milestone": False,
        "dependencies": ["E6.1"],
        "resource": "PM + Właściciel procesów",
        "cost_area": "Szkolenia i konsultacje",
        "progress": 0,
    },
    {
        "id": "E6.3",
        "name": "Decyzja o dalszych inwestycjach (chatbot, kolejne integracje)",
        "phase": "E6 - Optymalizacja i rozwój",
        "start": datetime(2028, 1, 16),
        "end": datetime(2028, 2, 15),
        "milestone": True,
        "dependencies": ["E6.2"],
        "resource": "Zarząd + PM",
        "cost_area": "Sprzęt / Rozwiązania SaaS (wg potrzeb)",
        "progress": 0,
    },
]

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def generate_markdown_structure(tasks):
    """
    Generuje strukturę projektu w formacie markdown
    """
    df = pd.DataFrame(tasks)
    
    # Sortowanie według faz i dat
    phase_order = {
        "E1 - Start i przygotowanie": 1,
        "E2 - Strona www + identyfikacja": 2, 
        "E3 - System rezerwacji i płatności": 3,
        "E4 - CRM i lojalność": 4,
        "E5 - Analityka i dynamic pricing": 5,
        "E6 - Optymalizacja i rozwój": 6
    }
    df["phase_order"] = df["phase"].map(phase_order)
    df = df.sort_values(["phase_order", "start"])
    
    markdown = "# Program Digitalizacji - Struktura Projektu\n\n"
    markdown += f"**Okres realizacji:** {df['start'].min().strftime('%Y-%m-%d')} - {df['end'].max().strftime('%Y-%m-%d')}\n\n"
    markdown += "---\n\n"
    
    # Grupowanie według faz
    for phase in df['phase'].unique():
        phase_tasks = df[df['phase'] == phase]
        phase_start = phase_tasks['start'].min()
        phase_end = phase_tasks['end'].max()
        
        # Nagłówek fazy
        markdown += f"## {phase}\n\n"
        markdown += f"**Okres:** {phase_start.strftime('%Y-%m-%d')} - {phase_end.strftime('%Y-%m-%d')}\n\n"
        
        # Tabela zadań
        markdown += "| ID | Zadanie | Data rozpoczęcia | Data zakończenia | Kamień milowy | Zasoby | Obszar kosztów |\n"
        markdown += "|---|---|---|---|---|---|---|\n"
        
        for _, task in phase_tasks.iterrows():
            milestone_icon = "🎯" if task['milestone'] else "📋"
            markdown += f"| {task['id']} | {milestone_icon} {task['name']} | {task['start'].strftime('%Y-%m-%d')} | {task['end'].strftime('%Y-%m-%d')} | {'✅' if task['milestone'] else '❌'} | {task['resource']} | {task['cost_area']} |\n"
        
        # Zależności
        phase_dependencies = []
        for _, task in phase_tasks.iterrows():
            if task['dependencies']:
                deps = ", ".join(task['dependencies'])
                phase_dependencies.append(f"- **{task['id']}** zależy od: {deps}")
        
        if phase_dependencies:
            markdown += "\n**Zależności:**\n"
            markdown += "\n".join(phase_dependencies)
        
        markdown += "\n\n---\n\n"
    
    # Podsumowanie kamieni milowych
    milestones = df[df['milestone'] == True].sort_values('end')
    if not milestones.empty:
        markdown += "## 🎯 Kamienie Milowe\n\n"
        markdown += "| Data | Etap | Kamień milowy |\n"
        markdown += "|---|---|---|\n"
        for _, milestone in milestones.iterrows():
            markdown += f"| {milestone['end'].strftime('%Y-%m-%d')} | {milestone['phase'].split(' - ')[0]} | {milestone['name']} |\n"
        markdown += "\n---\n\n"
    
    # Podsumowanie zasobów
    markdown += "## 👥 Zasoby\n\n"
    resources = set()
    for task in tasks:
        if task['resource']:
            # Rozdzielenie zasobów po '+'
            task_resources = [r.strip() for r in task['resource'].split('+')]
            resources.update(task_resources)
    
    for resource in sorted(resources):
        resource_tasks = []
        for _, task in df.iterrows():
            if resource in task['resource']:
                resource_tasks.append(f"{task['id']} ({task['start'].strftime('%Y-%m')} - {task['end'].strftime('%Y-%m')})")
        markdown += f"**{resource}:**\n"
        markdown += "- " + "\n- ".join(resource_tasks) + "\n\n"
    
    # Podsumowanie obszarów kosztów
    markdown += "## 💰 Obszary Kosztów\n\n"
    cost_areas = df.groupby('cost_area').agg({
        'id': lambda x: ', '.join(x),
        'start': 'min',
        'end': 'max'
    }).reset_index()
    
    for _, area in cost_areas.iterrows():
        markdown += f"**{area['cost_area']}**\n"
        markdown += f"- Zadania: {area['id']}\n"
        markdown += f"- Okres: {area['start'].strftime('%Y-%m-%d')} - {area['end'].strftime('%Y-%m-%d')}\n\n"
    
    return markdown

def generate_phase_gantt(tasks, filename_prefix="phases"):
    """
    Generuje uproszczony wykres Gantta tylko z etapami (bez poszczególnych zadań)
    """
    df = pd.DataFrame(tasks)
    
    # Sortowanie według faz
    phase_order = {
        "E1 - Start i przygotowanie": 1,
        "E2 - Strona www + identyfikacja": 2, 
        "E3 - System rezerwacji i płatności": 3,
        "E4 - CRM i lojalność": 4,
        "E5 - Analityka i dynamic pricing": 5,
        "E6 - Optymalizacja i rozwój": 6
    }
    
    # Agregacja danych według faz
    phase_data = []
    for phase in df['phase'].unique():
        phase_tasks = df[df['phase'] == phase]
        phase_start = phase_tasks['start'].min()
        phase_end = phase_tasks['end'].max()
        
        # Sprawdzenie czy faza ma kamienie milowe
        has_milestones = phase_tasks['milestone'].any()
        
        # Główne zasoby w fazie
        all_resources = []
        for resource_str in phase_tasks['resource'].dropna():
            all_resources.extend([r.strip() for r in resource_str.split('+')])
        main_resources = ', '.join(list(set(all_resources))[:3])  # Top 3 zasoby
        
        phase_data.append({
            'phase': phase,
            'start': phase_start,
            'end': phase_end,
            'has_milestones': has_milestones,
            'resources': main_resources,
            'order': phase_order.get(phase, 999)
        })
    
    phase_df = pd.DataFrame(phase_data).sort_values('order')
    
    # Kolory dla etapów (takie same jak w głównym wykresie)
    phase_colors = {
        "E1 - Start i przygotowanie": "#FF6B6B",
        "E2 - Strona www + identyfikacja": "#4ECDC4",
        "E3 - System rezerwacji i płatności": "#45B7D1",
        "E4 - CRM i lojalność": "#96CEB4",
        "E5 - Analityka i dynamic pricing": "#FECA57",
        "E6 - Optymalizacja i rozwój": "#DDA0DD"
    }
    
    # Tworzenie wykresu
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Pozycje na osi Y
    y_positions = range(len(phase_df))
    
    for i, row in phase_df.iterrows():
        start_num = mdates.date2num(row["start"])
        end_num = mdates.date2num(row["end"])
        duration_num = end_num - start_num
        
        # Kolor dla danego etapu
        color = phase_colors.get(row["phase"], "#CCCCCC")
        
        # Pasek etapu
        ax.barh(
            y=i,
            width=duration_num,
            left=start_num,
            height=0.6,
            align="center",
            alpha=0.8,
            color=color,
            edgecolor="black",
            linewidth=1,
        )
        
        # Dodatkowa obwódka dla etapów z kamieniami milowymi
        if row["has_milestones"]:
            ax.barh(
                y=i,
                width=duration_num,
                left=start_num,
                height=0.6,
                align="center",
                alpha=0,
                edgecolor="black",
                linewidth=3,
                zorder=3,
            )
        
        # Etykieta z datami na pasku
        mid_point = start_num + duration_num / 2
        ax.text(mid_point, i, f"{row['start'].strftime('%m/%y')} - {row['end'].strftime('%m/%y')}", 
                ha='center', va='center', fontweight='bold', fontsize=9, color='white',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='black', alpha=0.7))
    
    # Oś Y – nazwy etapów
    ax.set_yticks(list(y_positions))
    phase_labels = []
    for _, row in phase_df.iterrows():
        phase_num = row['phase'].split(' - ')[0]
        phase_name = row['phase'].split(' - ')[1]
        duration_days = (row['end'] - row['start']).days
        phase_labels.append(f"{phase_num}\n{phase_name}\n({duration_days} dni)")
    
    ax.set_yticklabels(phase_labels, fontsize=10)
    
    # Formatowanie osi X (daty)
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    
    plt.xticks(rotation=45, fontsize=10)
    ax.tick_params(axis='y', labelsize=10)
    
    ax.set_xlabel("Czas", fontsize=12, fontweight='bold')
    ax.set_title("Harmonogram - Etapy", fontsize=16, fontweight='bold', pad=20)
    
    # Legenda
    legend_elements = []
    for phase, color in phase_colors.items():
        short_name = phase.split(' - ')[1]
        legend_elements.append(plt.Rectangle((0,0),1,1, facecolor=color, alpha=0.8, label=short_name))
    
    ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9, 
              title="Etapy projektu", title_fontsize=10)
    
    # Siatka
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.grid(axis="y", linestyle=":", alpha=0.2)
    
    plt.tight_layout()
    
    # Zapisanie do plików
    plt.savefig(f"{filename_prefix}_gantt.png", dpi=300, bbox_inches="tight")
    plt.savefig(f"{filename_prefix}_gantt.pdf", bbox_inches="tight")
    
    return fig, ax

def generate_roadmap(tasks, filename_prefix="roadmap"):
    """
    Generuje roadmapę rozwoju infrastruktury cyfrowej w formie wizualnego diagramu
    """
    # Definicja poziomów roadmapy zgodnie z tabelą
    roadmap_levels = [
        {
            'level': 0,
            'title': 'Stan wyjściowy',
            'horizon': 'do końca 2025',
            'description': 'Brak PMS/CRM, tylko OTA + Excel, brak integracji, brak formalnych polityk bezpieczeństwa i backupu.',
            'actions': 'Inwentaryzacja istniejących narzędzi, ocena łącza internetowego i sprzętu, identyfikacja głównych luk infrastrukturalnych (przygotowanie do startu programu od Q1 2026).',
            'color': '#E0E0E0',
            'tasks': [],
            'start_date': datetime(2025, 10, 1),
            'end_date': datetime(2025, 12, 31)
        },
        {
            'level': 1,
            'title': 'Podstawowa infrastruktura rezerwacyjna',
            'horizon': 'Q1–Q4 2026',
            'description': 'Nowa strona www, podstawowy PMS z kalendarzem i channel managerem, zintegrowany z OTA; pełny proces rezerwacji online z płatnościami (jeszcze bez CRM i zaawansowanej analityki).',
            'actions': 'E1.1–E1.4, E2.1–E2.5, E3.1–E3.5: • formalne uruchomienie programu i budżetu IT • wybór i wdrożenie PMS/booking engine • projekt i wdrożenie nowej strony www + identyfikacja • uruchomienie płatności online i integracji z OTA • testy i start produkcyjny systemu rezerwacji.',
            'color': '#FF6B6B',
            'tasks': ['E1', 'E2', 'E3'],
            'start_date': datetime(2026, 1, 1),
            'end_date': datetime(2027, 1, 15)
        },
        {
            'level': 2,
            'title': 'Infrastruktura relacyjna',
            'horizon': 'Q1–Q2 2027',
            'description': 'PMS zintegrowany z booking engine i CRM; uruchomione płatności online, działający program lojalnościowy oraz podstawowe raporty operacyjne (obłożenie, kanały sprzedaży, przychody).',
            'actions': 'E4.1–E4.4: • wdrożenie CRM • import dotychczasowych kontaktów • uruchomienie programu lojalnościowego (kody rabatowe) • konfiguracja automatycznych e-maili przed/po pobycie oraz podstawowych raportów operacyjnych.',
            'color': '#96CEB4',
            'tasks': ['E4'],
            'start_date': datetime(2027, 1, 16),
            'end_date': datetime(2027, 6, 15)
        },
        {
            'level': 3,
            'title': 'Infrastruktura analityczna i rozwojowa',
            'horizon': 'Q2–Q4 2027',
            'description': 'Dashboardy zarządcze (KPI), dynamic pricing, częściowa automatyzacja marketingu (segmentacja, kampanie), ugruntowane procedury bezpieczeństwa i backupu.',
            'actions': 'E5.1–E5.3, E6.1–E6.3: • konfiguracja zaawansowanych raportów i dashboardów (m.in. obłożenie, ADR, RevPAR, udział kanałów) • wdrożenie zasad dynamicznego ustalania cen • szkolenia z analityki i pracy na danych • przegląd KPI z IT BSC, korekta procesów • decyzje o dalszych inwestycjach (chatbot, kolejne integracje, dodatkowe SaaS).',
            'color': '#FECA57',
            'tasks': ['E5', 'E6'],
            'start_date': datetime(2027, 6, 16),
            'end_date': datetime(2028, 2, 15)
        }
    ]
    
    # Tworzenie wykresu roadmapy
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Pozycje na osi Y dla poziomów (poziom 0 na górze, poziom 3 na dole)
    y_positions = list(range(len(roadmap_levels)))
    # Odwracamy pozycje - najwyższy indeks (poziom 3) ma najmniejszą pozycję Y
    y_positions.reverse()
    level_height = 0.8
    
    # Kolory dla strumieni zadań
    stream_colors = {
        'E1': '#FF6B6B',
        'E2': '#4ECDC4', 
        'E3': '#45B7D1',
        'E4': '#96CEB4',
        'E5': '#FECA57',
        'E6': '#DDA0DD'
    }
    
    for i, level in enumerate(roadmap_levels):
        y_pos = y_positions[i]
        
        # Konwersja dat na numery
        start_num = mdates.date2num(level['start_date'])
        end_num = mdates.date2num(level['end_date'])
        duration_num = end_num - start_num
        
        # Główny pasek poziomu
        ax.barh(
            y=y_pos,
            width=duration_num,
            left=start_num,
            height=level_height,
            align="center",
            alpha=0.3,
            color=level['color'],
            edgecolor="black",
            linewidth=2,
        )
        
        # Dodanie strumieni zadań na pasku
        if level['tasks']:
            stream_width = duration_num / len(level['tasks'])
            for j, task_phase in enumerate(level['tasks']):
                stream_start = start_num + j * stream_width
                ax.barh(
                    y=y_pos,
                    width=stream_width * 0.8,  # Lekko węższe dla lepszej wizualizacji
                    left=stream_start + stream_width * 0.1,
                    height=level_height * 0.4,
                    align="center",
                    alpha=0.8,
                    color=stream_colors.get(task_phase, '#CCCCCC'),
                    edgecolor="black",
                    linewidth=1,
                )
                
                # Etykieta zadania
                ax.text(stream_start + stream_width/2, y_pos, task_phase, 
                       ha='center', va='center', fontweight='bold', fontsize=10, color='white',
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='black', alpha=0.7))
        
        # Tytuł poziomu po lewej stronie
        ax.text(start_num - 30, y_pos, f"Poziom {level['level']}\n{level['title']}", 
               ha='right', va='center', fontweight='bold', fontsize=11,
               bbox=dict(boxstyle='round,pad=0.5', facecolor=level['color'], alpha=0.8))
        
        # Horyzont czasowy na pasku
        mid_point = start_num + duration_num / 2
        ax.text(mid_point, y_pos + level_height/3, level['horizon'], 
               ha='center', va='center', fontweight='bold', fontsize=10,
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9))
    
    # Strzałki pokazujące przepływ między poziomami
    for i in range(len(roadmap_levels) - 1):
        current_level = roadmap_levels[i]
        next_level = roadmap_levels[i + 1]
        
        current_y = y_positions[i]
        next_y = y_positions[i + 1]
        
        current_end = mdates.date2num(current_level['end_date'])
        next_start = mdates.date2num(next_level['start_date'])
        
        # Strzałka między poziomami
        ax.annotate('', xy=(next_start, next_y), xytext=(current_end, current_y),
                   arrowprops=dict(arrowstyle='->', lw=3, color='darkblue', alpha=0.7))
    
    # Ustawienia osi Y
    ax.set_yticks(y_positions)
    ax.set_yticklabels([f"Poziom {level['level']}" for level in roadmap_levels], fontsize=12)
    
    # Formatowanie osi X (daty)
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
    
    plt.xticks(rotation=45, fontsize=10)
    ax.tick_params(axis='y', labelsize=10)
    
    ax.set_xlabel("Czas", fontsize=12, fontweight='bold')
    ax.set_title("Roadmapa Rozwoju Infrastruktury Cyfrowej", fontsize=16, fontweight='bold', pad=20)
    
    # Legenda dla strumieni zadań
    legend_elements = []
    for task_phase, color in stream_colors.items():
        legend_elements.append(plt.Rectangle((0,0),1,1, facecolor=color, alpha=0.8, label=f"Etap {task_phase}"))
    
    ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9, 
              title="Strumienie zadań", title_fontsize=10)
    
    # Siatka
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.grid(axis="y", linestyle=":", alpha=0.2)
    
    # Ustawienie limitów osi
    ax.set_xlim(mdates.date2num(datetime(2025, 9, 1)), mdates.date2num(datetime(2028, 3, 31)))
    
    plt.tight_layout()
    
    # Zapisanie do plików
    plt.savefig(f"{filename_prefix}_diagram.png", dpi=300, bbox_inches="tight")
    plt.savefig(f"{filename_prefix}_diagram.pdf", bbox_inches="tight")
    
    return fig, ax, roadmap_levels

def generate_roadmap_markdown(roadmap_levels, filename="roadmap_struktura.md"):
    """
    Generuje szczegółową dokumentację roadmapy w formacie markdown
    """
    markdown = "# Roadmapa Rozwoju Infrastruktury Cyfrowej\n\n"
    markdown += "## Przegląd strategii digitalizacji 2025-2028\n\n"
    markdown += "Roadmapa przedstawia czterostopniowy rozwój infrastruktury cyfrowej hotelu, "
    markdown += "od stanu początkowego do pełnej automatyzacji procesów biznesowych.\n\n"
    markdown += "---\n\n"
    
    # Tabela główna roadmapy
    markdown += "## Tabela 9. Roadmapa rozwoju infrastruktury cyfrowej\n\n"
    markdown += "| Poziom | Horyzont | Opis infrastruktury | Kluczowe działania |\n"
    markdown += "|--------|----------|---------------------|--------------------|\n"
    
    for level in roadmap_levels:
        level_title = f"**{level['level']} – {level['title']}**"
        horizon = f"**{level['horizon']}**"
        description = level['description']
        actions = level['actions']
        
        markdown += f"| {level_title} | {horizon} | {description} | {actions} |\n"
    
    markdown += "\n---\n\n"
    
    # Szczegółowy opis każdego poziomu
    markdown += "## Szczegółowy opis poziomów roadmapy\n\n"
    
    for level in roadmap_levels:
        markdown += f"### Poziom {level['level']}: {level['title']}\n\n"
        markdown += f"**Horyzont czasowy:** {level['horizon']}\n\n"
        markdown += f"**Daty realizacji:** {level['start_date'].strftime('%Y-%m-%d')} - {level['end_date'].strftime('%Y-%m-%d')}\n\n"
        
        markdown += "**Opis infrastruktury:**\n"
        markdown += f"{level['description']}\n\n"
        
        markdown += "**Kluczowe działania:**\n"
        markdown += f"{level['actions']}\n\n"
        
        if level['tasks']:
            markdown += "**Powiązane etapy:**\n"
            for task in level['tasks']:
                markdown += f"- Etap {task}\n"
            markdown += "\n"
        
        markdown += "---\n\n"
    
    # Podsumowanie korzyści i wskaźników sukcesu
    markdown += "## Korzyści i wskaźniki sukcesu\n\n"
    
    success_metrics = [
        {
            'level': 0,
            'metrics': ['Kompletna inwentaryzacja obecnych systemów', 'Zidentyfikowane luki w infrastrukturze', 'Przygotowany budżet IT na 2026-2027']
        },
        {
            'level': 1, 
            'metrics': ['100% rezerwacji online', 'Integracja z wszystkimi głównymi OTA', 'Redukcja czasu obsługi rezerwacji o 50%', 'Zwiększenie konwersji na stronie o 25%']
        },
        {
            'level': 2,
            'metrics': ['Automatyzacja 80% komunikacji z gośćmi', 'Wzrost powtarzalnych rezerwacji o 30%', 'Redukcja kosztów marketingu o 20%', 'Centralizacja wszystkich danych gości']
        },
        {
            'level': 3,
            'metrics': ['Optymalizacja cen w czasie rzeczywistym', 'Wzrost RevPAR o 15-20%', 'Automatyzacja raportowania dla zarządu', 'Pełna kontrola nad procesami biznesowymi']
        }
    ]
    
    for metric_set in success_metrics:
        level_info = next(l for l in roadmap_levels if l['level'] == metric_set['level'])
        markdown += f"### Poziom {metric_set['level']}: {level_info['title']}\n\n"
        
        for metric in metric_set['metrics']:
            markdown += f"- ✅ {metric}\n"
        markdown += "\n"
    
    markdown += "---\n\n"
    
    # Analiza ryzyk i mitygacji
    markdown += "## Analiza ryzyk i działania mitygujące\n\n"
    
    risks = [
        {
            'risk': 'Opóźnienia w dostawie systemów PMS',
            'probability': 'Średnie',
            'impact': 'Wysokie',
            'mitigation': 'Wybór sprawdzonego dostawcy, buffer czasowy 2-4 tygodnie, plan B z alternatywnym dostawcą'
        },
        {
            'risk': 'Problemy z integracją systemów',
            'probability': 'Średnie', 
            'impact': 'Średnie',
            'mitigation': 'Testy integracyjne na środowisku testowym, wsparcie techniczne dostawców, dokumentacja API'
        },
        {
            'risk': 'Opór zespołu wobec nowych technologii',
            'probability': 'Niskie',
            'impact': 'Średnie', 
            'mitigation': 'Program szkoleń, zaangażowanie team leaderów, stopniowe wdrażanie funkcjonalności'
        },
        {
            'risk': 'Przekroczenie budżetu IT',
            'probability': 'Niskie',
            'impact': 'Wysokie',
            'mitigation': 'Szczegółowe planowanie budżetowe, monitoring kosztów miesięcznych, elastyczne podejście do zakresu'
        }
    ]
    
    markdown += "| Ryzyko | Prawdopodobieństwo | Wpływ | Działania mitygujące |\n"
    markdown += "|--------|-------------------|-------|---------------------|\n"
    
    for risk in risks:
        markdown += f"| {risk['risk']} | {risk['probability']} | {risk['impact']} | {risk['mitigation']} |\n"
    
    markdown += "\n---\n\n"
    
    # Budżet i zasoby
    markdown += "## Szacunkowy budżet i zasoby\n\n"
    
    budget_items = [
        {'category': 'PMS + booking engine + channel manager', 'annual_cost': '15,000 - 25,000 PLN', 'level': '1-3'},
        {'category': 'CRM + narzędzie e-mail marketingu', 'annual_cost': '8,000 - 15,000 PLN', 'level': '2-3'},
        {'category': 'Nowa strona www + identyfikacja', 'annual_cost': '20,000 - 40,000 PLN', 'level': '1'},
        {'category': 'Szkolenia i konsultacje', 'annual_cost': '10,000 - 20,000 PLN', 'level': '1-3'},
        {'category': 'Sprzęt / Rozwiązania SaaS (wg potrzeb)', 'annual_cost': '5,000 - 15,000 PLN', 'level': '3'}
    ]
    
    markdown += "| Kategoria | Szacunkowy koszt roczny | Poziomy roadmapy |\n"
    markdown += "|-----------|-------------------------|------------------|\n"
    
    total_min = 0
    total_max = 0
    
    for item in budget_items:
        markdown += f"| {item['category']} | {item['annual_cost']} | {item['level']} |\n"
        # Prosta kalkulacja sumy (zakładając format "X,XXX - Y,YYY PLN")
        costs = item['annual_cost'].replace(' PLN', '').replace(',', '').split(' - ')
        if len(costs) == 2:
            total_min += int(costs[0])
            total_max += int(costs[1])
    
    markdown += f"| **RAZEM** | **{total_min:,} - {total_max:,} PLN** | **Wszystkie** |\n"
    markdown += "\n"
    
    markdown += "**Uwagi dotyczące budżetu:**\n"
    markdown += "- Koszty przedstawiono jako szacunki roczne w pełni operacyjnych systemów\n"
    markdown += "- Koszty wdrożenia (jednorazowe) mogą wynieść dodatkowo 20-50% kosztów rocznych\n"
    markdown += "- Ostateczne koszty zależą od wybranego dostawcy i zakresu funkcjonalności\n"
    markdown += "- Zaleca się utworzenie rezerwy budżetowej na poziomie 15-20% całkowitych kosztów\n\n"
    
    # Zapisanie do pliku
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)
    
    return markdown

def generate_detailed_schedule(tasks, filename_prefix="detailed_schedule"):
    """
    Generuje bardzo szczegółowy harmonogram z pełnym podziałem na zadania
    """
    df = pd.DataFrame(tasks)
    
    # Sortowanie według faz i dat
    phase_order = {
        "E1 - Start i przygotowanie": 1,
        "E2 - Strona www + identyfikacja": 2, 
        "E3 - System rezerwacji i płatności": 3,
        "E4 - CRM i lojalność": 4,
        "E5 - Analityka i dynamic pricing": 5,
        "E6 - Optymalizacja i rozwój": 6
    }
    df["phase_order"] = df["phase"].map(phase_order)
    df = df.sort_values(["phase_order", "start"]).reset_index(drop=True)
    
    # Obliczenie dodatkowych metryk
    df["duration_days"] = (df["end"] - df["start"]).dt.days + 1
    df["start_week"] = df["start"].dt.isocalendar().week
    df["end_week"] = df["end"].dt.isocalendar().week
    df["quarter"] = df["start"].dt.quarter
    df["year"] = df["start"].dt.year
    
    # Kolory dla etapów
    phase_colors = {
        "E1 - Start i przygotowanie": "#FF6B6B",
        "E2 - Strona www + identyfikacja": "#4ECDC4",
        "E3 - System rezerwacji i płatności": "#45B7D1",
        "E4 - CRM i lojalność": "#96CEB4",
        "E5 - Analityka i dynamic pricing": "#FECA57",
        "E6 - Optymalizacja i rozwój": "#DDA0DD"
    }
    
    # Tworzenie bardzo szczegółowego wykresu
    fig = plt.figure(figsize=(20, 16))
    
    # Główny wykres Gantta (zajmuje większą część)
    ax1 = plt.subplot2grid((4, 3), (0, 0), colspan=2, rowspan=3)
    
    # Pozycje na osi Y
    y_positions = range(len(df))
    
    for i, row in df.iterrows():
        start_num = mdates.date2num(row["start"])
        end_num = mdates.date2num(row["end"])
        duration_num = end_num - start_num
        
        # Kolor dla danego etapu
        color = phase_colors.get(row["phase"], "#CCCCCC")
        
        # Główny pasek zadania
        ax1.barh(
            y=i,
            width=duration_num,
            left=start_num,
            height=0.6,
            align="center",
            alpha=0.7,
            color=color,
            edgecolor="black",
            linewidth=1,
        )
        
        # Pasek progresu
        if row["progress"] > 0:
            progress_width = duration_num * (row["progress"] / 100.0)
            ax1.barh(
                y=i,
                width=progress_width,
                left=start_num,
                height=0.3,
                align="center",
                color="darkgreen",
                alpha=0.8,
                zorder=3,
            )
        
        # Oznaczenie kamieni milowych
        if row["milestone"]:
            ax1.barh(
                y=i,
                width=duration_num,
                left=start_num,
                height=0.6,
                align="center",
                alpha=0,
                edgecolor="red",
                linewidth=4,
                zorder=4,
            )
            # Dodanie ikony kamienia milowego
            ax1.scatter(end_num, i, s=200, c='red', marker='D', zorder=5, edgecolor='black')
        
        # Etykieta z czasem trwania na pasku
        mid_point = start_num + duration_num / 2
        if duration_num > 20:  # Tylko dla dłuższych zadań
            ax1.text(mid_point, i, f"{row['duration_days']}d", 
                    ha='center', va='center', fontweight='bold', fontsize=8, color='white',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='black', alpha=0.7))
    
    # Linie podziału między etapami
    current_phase = None
    for i, row in df.iterrows():
        if current_phase != row['phase']:
            if i > 0:  # Nie rysuj linii przed pierwszym etapem
                ax1.axhline(y=i - 0.5, color='red', linestyle='--', linewidth=2, alpha=0.8)
            current_phase = row['phase']
    
    # Pionowe linie dla granic etapów z etykietami
    for phase in df['phase'].unique():
        phase_tasks = df[df['phase'] == phase]
        phase_start = phase_tasks['start'].min()
        phase_end = phase_tasks['end'].max()
        
        phase_start_num = mdates.date2num(phase_start)
        phase_end_num = mdates.date2num(phase_end)
        
        ax1.axvline(x=phase_start_num, color='gray', linestyle='--', linewidth=1, alpha=0.5)
        ax1.axvline(x=phase_end_num, color='gray', linestyle='--', linewidth=1, alpha=0.5)
        
        # Etykieta etapu na górze
        phase_label = phase.split(' - ')[0]
        ax1.text(phase_start_num + (phase_end_num - phase_start_num) / 2, 
                len(df) - 0.5, phase_label, 
                fontsize=12, fontweight='bold', ha='center', va='bottom',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.8))
    
    # Ustawienia głównego wykresu
    ax1.set_yticks(list(y_positions))
    task_labels = []
    for _, task in df.iterrows():
        milestone_marker = "🎯" if task['milestone'] else ""
        progress_marker = f"({task['progress']}%)" if task['progress'] > 0 else ""
        task_labels.append(f"{task['id']} {milestone_marker}\n{task['name'][:40]}{'...' if len(task['name']) > 40 else ''}\n{progress_marker}")
    
    ax1.set_yticklabels(task_labels, fontsize=8)
    ax1.xaxis_date()
    ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    ax1.xaxis.set_minor_locator(mdates.WeekdayLocator())
    
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, fontsize=9)
    ax1.tick_params(axis='y', labelsize=8)
    ax1.set_xlabel("Czas", fontsize=12, fontweight='bold')
    ax1.set_title("Szczegółowy Harmonogram Projektu", fontsize=16, fontweight='bold', pad=20)
    ax1.grid(axis="x", linestyle="--", alpha=0.3)
    ax1.grid(axis="y", linestyle=":", alpha=0.2)
    
    # Panel informacyjny po prawej (ax2)
    ax2 = plt.subplot2grid((4, 3), (0, 2), rowspan=2)
    ax2.axis('off')
    
    # Statystyki projektu
    stats_text = "📊 STATYSTYKI PROJEKTU\n\n"
    stats_text += f"Całkowity czas: {(df['end'].max() - df['start'].min()).days} dni\n"
    stats_text += f"Liczba zadań: {len(df)}\n"
    stats_text += f"Kamienie milowe: {df['milestone'].sum()}\n"
    stats_text += f"Liczba etapów: {df['phase'].nunique()}\n\n"
    
    # Statystyki według etapów
    stats_text += "📈 WEDŁUG ETAPÓW:\n"
    for phase in df['phase'].unique():
        phase_tasks = df[df['phase'] == phase]
        phase_duration = (phase_tasks['end'].max() - phase_tasks['start'].min()).days
        stats_text += f"• {phase.split(' - ')[0]}: {len(phase_tasks)} zadań, {phase_duration} dni\n"
    
    stats_text += "\n🎯 KAMIENIE MILOWE:\n"
    milestones = df[df['milestone'] == True].sort_values('end')
    for _, milestone in milestones.iterrows():
        stats_text += f"• {milestone['end'].strftime('%Y-%m-%d')}: {milestone['id']}\n"
    
    ax2.text(0.05, 0.95, stats_text, transform=ax2.transAxes, fontsize=9,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', alpha=0.8))
    
    # Panel zasobów (ax3)
    ax3 = plt.subplot2grid((4, 3), (2, 2), rowspan=2)
    ax3.axis('off')
    
    # Analiza zasobów
    # resources_text = "👥 ZASOBY I ODPOWIEDZIALNOŚCI\n\n"
    # all_resources = set()
    # for task in tasks:
    #     if task['resource']:
    #         task_resources = [r.strip() for r in task['resource'].split('+')]
    #         all_resources.update(task_resources)
    
    # for resource in sorted(all_resources):
    #     resource_tasks = df[df['resource'].str.contains(resource, na=False)]
    #     resources_text += f"• {resource}:\n"
    #     resources_text += f"  {len(resource_tasks)} zadań\n"
    #     if len(resource_tasks) > 0:
    #         total_days = resource_tasks['duration_days'].sum()
    #         resources_text += f"  {total_days} dni roboczych\n"
    #     resources_text += "\n"
    
    # ax3.text(0.05, 0.95, resources_text, transform=ax3.transAxes, fontsize=8,
    #         verticalalignment='top', fontfamily='monospace',
    #         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.8))
    
    # Timeline z kamieniami milowymi (ax4)
    ax4 = plt.subplot2grid((4, 3), (3, 0), colspan=3)
    
    # Tworzenie osi czasowej
    project_start = df['start'].min()
    project_end = df['end'].max()
    
    # Linia czasowa
    ax4.plot([mdates.date2num(project_start), mdates.date2num(project_end)], [0, 0], 
            'k-', linewidth=3, alpha=0.7)
    
    # Kamienie milowe na linii czasowej
    milestones = df[df['milestone'] == True].sort_values('end')
    for i, (_, milestone) in enumerate(milestones.iterrows()):
        date_num = mdates.date2num(milestone['end'])
        ax4.scatter(date_num, 0, s=300, c='red', marker='D', zorder=5, edgecolor='black')
        
        # Etykieta kamienia milowego
        y_offset = 0.3 if i % 2 == 0 else -0.3
        ax4.annotate(f"{milestone['id']}\n{milestone['end'].strftime('%Y-%m-%d')}", 
                    xy=(date_num, 0), xytext=(date_num, y_offset),
                    ha='center', va='center' if y_offset > 0 else 'center',
                    fontsize=8, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.8),
                    arrowprops=dict(arrowstyle='->', lw=1))
    
    # Oznaczenia etapów na timeline
    for phase in df['phase'].unique():
        phase_tasks = df[df['phase'] == phase]
        phase_start = mdates.date2num(phase_tasks['start'].min())
        phase_end = mdates.date2num(phase_tasks['end'].max())
        
        color = phase_colors.get(phase, "#CCCCCC")
        ax4.axvspan(phase_start, phase_end, alpha=0.2, color=color, zorder=1)
        
        # Etykieta etapu
        phase_mid = phase_start + (phase_end - phase_start) / 2
        ax4.text(phase_mid, -0.8, phase.split(' - ')[0], 
                ha='center', va='center', fontsize=10, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor=color, alpha=0.8))
    
    ax4.set_xlim(mdates.date2num(project_start) - 10, mdates.date2num(project_end) + 10)
    ax4.set_ylim(-1, 1)
    ax4.xaxis_date()
    ax4.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax4.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, fontsize=9)
    ax4.set_ylabel("")
    ax4.set_title("Timeline kamieni milowych", fontsize=12, fontweight='bold')
    ax4.grid(axis="x", linestyle="--", alpha=0.3)
    ax4.set_yticks([])
    
    # Legenda na głównym wykresie
    legend_elements = []
    for phase, color in phase_colors.items():
        short_name = phase.split(' - ')[1]
        legend_elements.append(plt.Rectangle((0,0),1,1, facecolor=color, alpha=0.7, label=short_name))
    
    # Dodanie elementów legendy dla specjalnych oznaczeń
    legend_elements.append(plt.Rectangle((0,0),1,1, facecolor='red', alpha=0.7, label='Kamień milowy'))
    legend_elements.append(plt.Rectangle((0,0),1,1, facecolor='darkgreen', alpha=0.8, label='Postęp'))
    
    ax1.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1), fontsize=9, 
              title="Legenda", title_fontsize=10)
    
    plt.tight_layout()
    
    # Zapisanie do plików
    plt.savefig(f"{filename_prefix}.png", dpi=300, bbox_inches="tight")
    plt.savefig(f"{filename_prefix}.pdf", bbox_inches="tight")
    
    return fig, (ax1, ax2, ax3, ax4)

def generate_detailed_schedule_report(tasks, filename="detailed_schedule_report.md"):
    """
    Generuje wyczerpujący raport szczegółowego harmonogramu
    """
    df = pd.DataFrame(tasks)
    
    # Sortowanie i obliczenia
    phase_order = {
        "E1 - Start i przygotowanie": 1,
        "E2 - Strona www + identyfikacja": 2, 
        "E3 - System rezerwacji i płatności": 3,
        "E4 - CRM i lojalność": 4,
        "E5 - Analityka i dynamic pricing": 5,
        "E6 - Optymalizacja i rozwój": 6
    }
    df["phase_order"] = df["phase"].map(phase_order)
    df = df.sort_values(["phase_order", "start"]).reset_index(drop=True)
    df["duration_days"] = (df["end"] - df["start"]).dt.days + 1
    df["quarter"] = df["start"].dt.quarter
    df["year"] = df["start"].dt.year
    df["start_weekday"] = df["start"].dt.day_name()
    df["end_weekday"] = df["end"].dt.day_name()
    
    markdown = "# Szczegółowy Harmonogram Projektu - Raport Wyczerpujący\n\n"
    markdown += f"**Data wygenerowania:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    markdown += f"**Okres realizacji:** {df['start'].min().strftime('%Y-%m-%d')} - {df['end'].max().strftime('%Y-%m-%d')}\n"
    markdown += f"**Całkowity czas projektu:** {(df['end'].max() - df['start'].min()).days} dni\n"
    markdown += f"**Liczba zadań:** {len(df)}\n"
    markdown += f"**Liczba etapów:** {df['phase'].nunique()}\n"
    markdown += f"**Kamienie milowe:** {df['milestone'].sum()}\n\n"
    markdown += "---\n\n"
    
    # 1. Szczegółowa analiza według etapów
    markdown += "## 1. Szczegółowa Analiza Według Etapów\n\n"
    
    for phase in df['phase'].unique():
        phase_tasks = df[df['phase'] == phase].copy()
        phase_start = phase_tasks['start'].min()
        phase_end = phase_tasks['end'].max()
        phase_duration = (phase_end - phase_start).days + 1
        
        markdown += f"### {phase}\n\n"
        markdown += f"**📅 Okres:** {phase_start.strftime('%Y-%m-%d')} - {phase_end.strftime('%Y-%m-%d')} ({phase_duration} dni)\n"
        markdown += f"**📊 Liczba zadań:** {len(phase_tasks)}\n"
        markdown += f"**🎯 Kamienie milowe:** {phase_tasks['milestone'].sum()}\n"
        markdown += f"**⏱️ Łączny czas zadań:** {phase_tasks['duration_days'].sum()} dni\n\n"
        
        # Zasoby w etapie
        all_resources = set()
        for resource_str in phase_tasks['resource'].dropna():
            all_resources.update([r.strip() for r in resource_str.split('+')])
        markdown += f"**👥 Zaangażowane zasoby:** {', '.join(sorted(all_resources))}\n\n"
        
        # Obszary kosztów
        cost_areas = phase_tasks['cost_area'].unique()
        markdown += f"**💰 Obszary kosztów:** {', '.join(cost_areas)}\n\n"
        
        # Szczegółowa tabela zadań
        markdown += "#### Szczegółowa lista zadań:\n\n"
        markdown += "| ID | Zadanie | Start | Koniec | Dni | Dzień tyg. start | Dzień tyg. koniec | Kamień milowy | Postęp | Zasoby | Obszar kosztów | Zależności |\n"
        markdown += "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
        
        for _, task in phase_tasks.iterrows():
            milestone_icon = "🎯" if task['milestone'] else "📋"
            dependencies = ", ".join(task['dependencies']) if task['dependencies'] else "Brak"
            
            markdown += f"| {task['id']} | {milestone_icon} {task['name']} | {task['start'].strftime('%Y-%m-%d')} | {task['end'].strftime('%Y-%m-%d')} | {task['duration_days']} | {task['start_weekday']} | {task['end_weekday']} | {'✅' if task['milestone'] else '❌'} | {task['progress']}% | {task['resource']} | {task['cost_area']} | {dependencies} |\n"
        
        markdown += "\n"
        
        # Analiza krytyczna dla etapu
        critical_tasks = phase_tasks[phase_tasks['milestone'] == True]
        if not critical_tasks.empty:
            markdown += "#### 🔥 Zadania krytyczne (kamienie milowe):\n\n"
            for _, task in critical_tasks.iterrows():
                markdown += f"- **{task['id']}** ({task['end'].strftime('%Y-%m-%d')}): {task['name']}\n"
            markdown += "\n"
        
        markdown += "---\n\n"
    
    # 2. Analiza zależności
    markdown += "## 2. Szczegółowa Analiza Zależności\n\n"
    
    # Mapowanie wszystkich zależności
    dependency_map = {}
    for _, task in df.iterrows():
        if task['dependencies']:
            dependency_map[task['id']] = task['dependencies']
    
    if dependency_map:
        markdown += "### Mapa zależności zadań:\n\n"
        markdown += "| Zadanie | Zależy od | Opis zależności |\n"
        markdown += "|---------|-----------|------------------|\n"
        
        for task_id, deps in dependency_map.items():
            task_info = df[df['id'] == task_id].iloc[0]
            deps_details = []
            
            for dep_id in deps:
                dep_task = df[df['id'] == dep_id]
                if not dep_task.empty:
                    dep_info = dep_task.iloc[0]
                    deps_details.append(f"{dep_id} (koniec: {dep_info['end'].strftime('%Y-%m-%d')})")
            
            markdown += f"| {task_id} - {task_info['name'][:50]} | {', '.join(deps)} | {'; '.join(deps_details)} |\n"
        
        markdown += "\n"
        
        # Analiza ścieżki krytycznej (uproszczona)
        markdown += "### Analiza ścieżki krytycznej:\n\n"
        milestones = df[df['milestone'] == True].sort_values('end')
        markdown += "Kluczowe punkty kontrolne projektu:\n\n"
        
        for _, milestone in milestones.iterrows():
            markdown += f"- **{milestone['end'].strftime('%Y-%m-%d')}**: {milestone['id']} - {milestone['name']}\n"
        
        markdown += "\n---\n\n"
    
    # 3. Analiza zasobów i obciążenia
    markdown += "## 3. Szczegółowa Analiza Zasobów i Obciążenia\n\n"
    
    # Zebranie wszystkich zasobów
    all_resources = set()
    for task in tasks:
        if task['resource']:
            task_resources = [r.strip() for r in task['resource'].split('+')]
            all_resources.update(task_resources)
    
    for resource in sorted(all_resources):
        resource_tasks = df[df['resource'].str.contains(resource, na=False, regex=False)]
        
        if not resource_tasks.empty:
            markdown += f"### 👤 {resource}\n\n"
            markdown += f"**Liczba zadań:** {len(resource_tasks)}\n"
            markdown += f"**Łączny czas zaangażowania:** {resource_tasks['duration_days'].sum()} dni\n"
            markdown += f"**Okres aktywności:** {resource_tasks['start'].min().strftime('%Y-%m-%d')} - {resource_tasks['end'].max().strftime('%Y-%m-%d')}\n\n"
            
            # Timeline dla zasobu
            markdown += "**Timeline zaangażowania:**\n\n"
            markdown += "| Zadanie | Start | Koniec | Dni | Etap | Typ |\n"
            markdown += "|---------|-------|--------|-----|------|-----|\n"
            
            for _, task in resource_tasks.sort_values('start').iterrows():
                task_type = "🎯 Kamień milowy" if task['milestone'] else "📋 Standardowe"
                etap = task['phase'].split(' - ')[0]
                markdown += f"| {task['id']} - {task['name'][:40]} | {task['start'].strftime('%Y-%m-%d')} | {task['end'].strftime('%Y-%m-%d')} | {task['duration_days']} | {etap} | {task_type} |\n"
            
            markdown += "\n"
            
            # Analiza obciążenia w czasie
            markdown += "**Analiza obciążenia:**\n"
            
            # Grupowanie według miesięcy
            resource_tasks_copy = resource_tasks.copy()
            resource_tasks_copy['month_year'] = resource_tasks_copy['start'].dt.to_period('M')
            monthly_workload = resource_tasks_copy.groupby('month_year').agg({
                'duration_days': 'sum',
                'id': 'count'
            }).reset_index()
            
            if not monthly_workload.empty:
                markdown += "\n| Miesiąc | Liczba zadań | Łączne dni |\n"
                markdown += "|---------|--------------|------------|\n"
                
                for _, month_data in monthly_workload.iterrows():
                    markdown += f"| {month_data['month_year']} | {month_data['id']} | {month_data['duration_days']} |\n"
            
            markdown += "\n---\n\n"
    
    # 4. Analiza obszarów kosztów
    markdown += "## 4. Szczegółowa Analiza Obszarów Kosztów\n\n"
    
    cost_areas = df.groupby('cost_area').agg({
        'id': 'count',
        'duration_days': 'sum',
        'start': 'min',
        'end': 'max',
        'milestone': 'sum'
    }).reset_index()
    
    cost_areas.columns = ['Obszar kosztów', 'Liczba zadań', 'Łączne dni', 'Pierwszy start', 'Ostatni koniec', 'Kamienie milowe']
    
    markdown += "### Podsumowanie według obszarów kosztów:\n\n"
    markdown += "| Obszar kosztów | Liczba zadań | Łączne dni | Pierwszy start | Ostatni koniec | Kamienie milowe |\n"
    markdown += "|----------------|--------------|------------|----------------|----------------|-----------------|\n"
    
    for _, area in cost_areas.iterrows():
        markdown += f"| {area['Obszar kosztów']} | {area['Liczba zadań']} | {area['Łączne dni']} | {area['Pierwszy start'].strftime('%Y-%m-%d')} | {area['Ostatni koniec'].strftime('%Y-%m-%d')} | {area['Kamienie milowe']} |\n"
    
    markdown += "\n"
    
    # Szczegółowa analiza każdego obszaru kosztów
    for _, area in cost_areas.iterrows():
        area_name = area['Obszar kosztów']
        area_tasks = df[df['cost_area'] == area_name]
        
        markdown += f"### 💰 {area_name}\n\n"
        
        # Zadania w obszarze kosztów
        markdown += "**Zadania w tym obszarze:**\n\n"
        for _, task in area_tasks.iterrows():
            milestone_marker = " 🎯" if task['milestone'] else ""
            markdown += f"- **{task['id']}**{milestone_marker}: {task['name']} ({task['start'].strftime('%Y-%m-%d')} - {task['end'].strftime('%Y-%m-%d')}, {task['duration_days']} dni)\n"
        
        markdown += "\n"
    
    markdown += "---\n\n"
    
    # 5. Kalendarz kamieni milowych
    markdown += "## 5. Kalendarz Kamieni Milowych\n\n"
    
    milestones = df[df['milestone'] == True].sort_values('end')
    
    markdown += "### Chronologiczna lista kamieni milowych:\n\n"
    markdown += "| Data | Zadanie | Etap | Opis | Zależności |\n"
    markdown += "|------|---------|------|------|------------|\n"
    
    for _, milestone in milestones.iterrows():
        etap = milestone['phase'].split(' - ')[0]
        dependencies = ", ".join(milestone['dependencies']) if milestone['dependencies'] else "Brak"
        
        markdown += f"| {milestone['end'].strftime('%Y-%m-%d')} | {milestone['id']} | {etap} | {milestone['name']} | {dependencies} |\n"
    
    markdown += "\n"
    
    # Analiza odstępów między kamieniami milowymi
    markdown += "### Analiza odstępów między kamieniami milowymi:\n\n"
    if len(milestones) > 1:
        for i in range(len(milestones) - 1):
            current = milestones.iloc[i]
            next_milestone = milestones.iloc[i + 1]
            days_between = (next_milestone['end'] - current['end']).days
            
            markdown += f"- **{current['id']}** → **{next_milestone['id']}**: {days_between} dni\n"
    
    markdown += "\n---\n\n"
    
    # 6. Podsumowanie i rekomendacje
    markdown += "## 6. Podsumowanie i Rekomendacje\n\n"
    
    markdown += "### Kluczowe statystyki:\n\n"
    markdown += f"- **Najdłuższe zadanie:** {df.loc[df['duration_days'].idxmax(), 'name']} ({df['duration_days'].max()} dni)\n"
    markdown += f"- **Najkrótsze zadanie:** {df.loc[df['duration_days'].idxmin(), 'name']} ({df['duration_days'].min()} dni)\n"
    markdown += f"- **Średni czas zadania:** {df['duration_days'].mean():.1f} dni\n"
    markdown += f"- **Najwięcej zadań w etapie:** {df.groupby('phase').size().max()} zadań\n"
    markdown += f"- **Najdłuższy etap:** {df.groupby('phase').apply(lambda x: (x['end'].max() - x['start'].min()).days).max()} dni\n\n"
    
    # Identyfikacja potencjalnych ryzyk
    markdown += "### Identyfikacja potencjalnych ryzyk:\n\n"
    
    # Zadania z wieloma zależnościami
    complex_dependencies = df[df['dependencies'].apply(lambda x: len(x) if x else 0) >= 2]
    if not complex_dependencies.empty:
        markdown += "**⚠️ Zadania z wieloma zależnościami (wysokie ryzyko opóźnień):**\n"
        for _, task in complex_dependencies.iterrows():
            markdown += f"- {task['id']}: {task['name']} (zależy od: {', '.join(task['dependencies'])})\n"
        markdown += "\n"
    
    # Długie zadania (potencjalnie problematyczne)
    long_tasks = df[df['duration_days'] > 60]  # Zadania dłuższe niż 2 miesiące
    if not long_tasks.empty:
        markdown += "**📅 Długie zadania (zalecane dzielenie na mniejsze części):**\n"
        for _, task in long_tasks.iterrows():
            markdown += f"- {task['id']}: {task['name']} ({task['duration_days']} dni)\n"
        markdown += "\n"
    
    # Rekomendacje
    markdown += "### Rekomendacje:\n\n"
    markdown += "1. **Monitoring kamieni milowych**: Szczególną uwagę należy zwrócić na terminowość realizacji kamieni milowych, gdyż opóźnienia wpływają na cały projekt.\n\n"
    markdown += "2. **Zarządzanie zasobami**: Należy monitorować obciążenie kluczowych zasobów, szczególnie PM i zespołów IT.\n\n"
    markdown += "3. **Bufory czasowe**: Zaleca się dodanie buforów czasowych (10-15%) dla zadań krytycznych i tych z wieloma zależnościami.\n\n"
    markdown += "4. **Regularne przeglądy**: Cotygodniowe przeglądy postępu z aktualizacją harmonogramu według rzeczywistego postępu.\n\n"
    markdown += "5. **Plan awaryjny**: Przygotowanie alternatywnych scenariuszy dla zadań o wysokim ryzyku.\n\n"
    
    # Zapisanie do pliku
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)
    
    return markdown

# Załóżmy, że lista 'tasks' jest zaimportowana z poprzedniego fragmentu

# 1. Przekształcenie na DataFrame
df = pd.DataFrame(tasks)

# 2. Filtrowanie – np. tylko zadania (bez rozróżniania faz, bo fazy tu nie są osobnymi rekordami)
# Jeśli chcesz odfiltrować tylko konkretne fazy, możesz użyć df[df["phase"].str.contains("E2")], itd.

# 3. Obliczenie długości zadania w dniach
df["duration"] = df["end"] - df["start"]

# 4. Dodanie kolumny pomocniczej do sortowania według etapów (zachowujemy kolejność E1->E6)
phase_order = {
    "E1 - Start i przygotowanie": 1,
    "E2 - Strona www + identyfikacja": 2, 
    "E3 - System rezerwacji i płatności": 3,
    "E4 - CRM i lojalność": 4,
    "E5 - Analityka i dynamic pricing": 5,
    "E6 - Optymalizacja i rozwój": 6
}
df["phase_order"] = df["phase"].map(phase_order)

# 5. Sortowanie najpierw po etapach, potem po dacie startu w ramach etapu
df = df.sort_values(["phase_order", "start"]).reset_index(drop=True)

# 6. Definicja kolorów dla etapów
phase_colors = {
    "E1 - Start i przygotowanie": "#FF6B6B",
    "E2 - Strona www + identyfikacja": "#4ECDC4",
    "E3 - System rezerwacji i płatności": "#45B7D1",
    "E4 - CRM i lojalność": "#96CEB4",
    "E5 - Analityka i dynamic pricing": "#FECA57",
    "E6 - Optymalizacja i rozwój": "#DDA0DD"
}

# 7. Wyznaczenie granic etapów dla linii podziału (po sortowaniu według etapów)
print("Analiza struktury etapów po sortowaniu według etapów:")
phase_boundaries = []
current_phase = None
phase_start_idx = 0

for i, row in df.iterrows():
    if current_phase != row['phase']:
        # Jeśli to nie pierwszy etap, zamknij poprzedni
        if current_phase is not None:
            phase_boundaries.append((current_phase, phase_start_idx, i-1))
            print(f"Etap: {current_phase}, indeksy: {phase_start_idx}-{i-1}")
        
        # Rozpocznij nowy etap
        current_phase = row['phase']
        phase_start_idx = i

# Dodaj ostatni etap
if current_phase is not None:
    phase_boundaries.append((current_phase, phase_start_idx, len(df)-1))
    print(f"Etap: {current_phase}, indeksy: {phase_start_idx}-{len(df)-1}")

print(f"Znalezione granice etapów: {len(phase_boundaries)} etapów")

# 7. Rysowanie wykresu Gantta
fig, ax = plt.subplots(figsize=(14, 10))

# Pozycje na osi Y
y_positions = range(len(df))

for i, row in df.iterrows():
    start_num = mdates.date2num(row["start"])
    end_num = mdates.date2num(row["end"])
    duration_num = end_num - start_num
    
    # Kolor dla danego etapu
    color = phase_colors.get(row["phase"], "#CCCCCC")
    
    # Pasek zadania (całkowity planowany czas)
    ax.barh(
        y=i,
        width=duration_num,
        left=start_num,
        height=0.4,
        align="center",
        alpha=0.7,
        color=color,
        edgecolor="black",
    )
    
    # Pasek progresu (np. węższy, na środku)
    if row["progress"] > 0 and not row["milestone"]:
        progress_width = duration_num * (row["progress"] / 100.0)
        ax.barh(
            y=i,
            width=progress_width,
            left=start_num,
            height=0.2,
            align="center",
        )
    
    # Kamienie milowe – pogrubiona czarna obwódka paska
    if row["milestone"]:
        # Dodatkowa czarna obwódka dla kamieni milowych
        ax.barh(
            y=i,
            width=duration_num,
            left=start_num,
            height=0.4,
            align="center",
            alpha=0,
            edgecolor="black",
            linewidth=3,
            zorder=3,
        )

# 8. Dodanie linii podziału między etapami
for i, (phase, min_idx, max_idx) in enumerate(phase_boundaries[:-1]):
    # Linia podziału po ostatnim zadaniu danego etapu
    ax.axhline(y=max_idx + 0.5, color='red', linestyle='--', linewidth=2, alpha=0.8)

# 8a. Dodanie pionowych linii dla granic etapów
for phase, min_idx, max_idx in phase_boundaries:
    phase_tasks = df[df['phase'] == phase]
    phase_start = phase_tasks['start'].min()
    phase_end = phase_tasks['end'].max()
    
    phase_start_num = mdates.date2num(phase_start)
    phase_end_num = mdates.date2num(phase_end)
    
    # Pionowa linia na początku etapu - szara przerywana
    ax.axvline(x=phase_start_num, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    
    # Pionowa linia na końcu etapu - szara przerywana
    ax.axvline(x=phase_end_num, color='gray', linestyle='--', linewidth=1, alpha=0.5)
    
    # Etykieta z numerem etapu na górze
    phase_label = phase.split(' - ')[0]
    ax.text(phase_start_num + (phase_end_num - phase_start_num) / 2, 
            len(df) - 0.5, phase_label, 
            fontsize=12, fontweight='bold', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.8))

# 9. Etykiety etapów są teraz na górze jako część pionowych linii

# 10. Oś Y – nazwy zadań
ax.set_yticks(list(y_positions))
ax.set_yticklabels(df["id"] + " " + df["name"], fontsize=9)

# 11. Formatowanie osi X (daty)
ax.xaxis_date()
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Co 3 miesiące zamiast 2
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.xaxis.set_minor_locator(mdates.MonthLocator())

plt.xticks(rotation=45, fontsize=10)
ax.tick_params(axis='y', labelsize=9)

ax.set_xlabel("Czas", fontsize=12, fontweight='bold')
ax.set_title("Harmonogram", fontsize=16, fontweight='bold', pad=20)

# 12. Dodanie legendy z kolorami etapów
legend_elements = []
for phase, color in phase_colors.items():
    short_name = phase.split(' - ')[1]  # Tylko opis bez numeru
    legend_elements.append(plt.Rectangle((0,0),1,1, facecolor=color, alpha=0.7, label=short_name))

ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9, 
          title="Etapy projektu", title_fontsize=10)

# Siatka pionowa i pozioma dla lepszej czytelności
ax.grid(axis="x", linestyle="--", alpha=0.3)
ax.grid(axis="y", linestyle=":", alpha=0.2)

plt.tight_layout()

# Zapisanie wykresu do pliku
plt.savefig("gantt_chart_digitalizacja.png", dpi=300, bbox_inches="tight")
plt.savefig("gantt_chart_digitalizacja.pdf", bbox_inches="tight")

# Generowanie struktury markdown
markdown_content = generate_markdown_structure(tasks)

# Zapisanie do pliku markdown
with open("struktura_projektu.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

# Generowanie uproszczonego wykresu z etapami
print("\nGenerowanie uproszczonego harmonogramu z etapami...")
fig_phases, ax_phases = generate_phase_gantt(tasks, "harmonogram_etapy")

# Generowanie roadmapy
print("\nGenerowanie roadmapy rozwoju infrastruktury...")
fig_roadmap, ax_roadmap, roadmap_levels = generate_roadmap(tasks, "roadmap_infrastruktura")

# Generowanie dokumentacji roadmapy
print("Generowanie dokumentacji roadmapy...")
roadmap_markdown = generate_roadmap_markdown(roadmap_levels, "roadmap_struktura.md")

# Generowanie szczegółowego harmonogramu
print("\nGenerowanie bardzo szczegółowego harmonogramu...")
fig_detailed, ax_detailed = generate_detailed_schedule(tasks, "harmonogram_szczegolowy")

def generate_clean_roadmap_table(tasks, filename_prefix="roadmap_clean_table"):
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
    
    # Mapowanie zadań według okresów i poziomów
    tasks_by_period = {
        0: [],  # Przygotowania - brak zadań projektowych
        1: [    # 2026-01-01 do 2026-09-30 - E1, E2
            "E1.1: Formalne uruchomienie programu (2026-01-01 do 2026-01-15)",
            "E1.2: Inwentaryzacja obecnych narzędzi (2026-01-16 do 2026-02-28)",
            "E1.3: Określenie budżetu IT na 2026-2027 (2026-02-01 do 2026-02-28)",
            "E1.4: Wybór dostawcy PMS/booking engine (2026-02-15 do 2026-03-31)",
            "E2.1: Projekt nowej strony www (2026-04-01 do 2026-05-31)",
            "E2.2: Przygotowanie logo i szablonów graficznych (2026-04-01 do 2026-05-15)",
            "E2.3: Wdrożenie nowej strony www (2026-06-01 do 2026-08-31)",
            "E2.4: Aktualizacja treści i zdjęć + podstawowe SEO (2026-07-01 do 2026-09-30)",
            "E2.5: Finalizacja strony www i identyfikacji (2026-09-01 do 2026-09-30)"
        ],
        2: [    # 2026-10-01 do 2027-01-15 - E3
            "E3.1: Uruchomienie booking engine (2026-10-01 do 2026-10-31)",
            "E3.2: Uruchomienie płatności online (2026-11-01 do 2026-11-30)",
            "E3.3: Integracja z OTA (channel manager) (2026-11-01 do 2026-12-15)",
            "E3.4: Testy procesu rezerwacji (2026-12-01 do 2026-12-31)",
            "E3.5: Start produkcyjny systemu rezerwacji (2027-01-01 do 2027-01-15)"
        ],
        3: [    # 2027-01-16 do 2027-06-15 - E4
            "E4.1: Wdrożenie CRM (2027-01-16 do 2027-03-15)",
            "E4.2: Import dotychczasowych kontaktów (2027-03-16 do 2027-04-15)",
            "E4.3: Uruchomienie programu lojalnościowego (2027-04-16 do 2027-05-15)",
            "E4.4: Automatyczne e-maile przed/po pobycie (2027-05-16 do 2027-06-15)"
        ],
        4: [    # 2027-06-16 do 2028-02-15 - E5, E6
            "E5.1: Konfiguracja raportów (obłożenie, kanały, RevPAR) (2027-06-16 do 2027-08-15)",
            "E5.2: Wdrożenie zasad dynamicznego ustalania cen (2027-08-16 do 2027-10-15)",
            "E5.3: Szkolenia z analityki i pracy na danych (2027-10-16 do 2027-11-15)",
            "E6.1: Przegląd KPI z IT BSC (2027-11-16 do 2027-12-15)",
            "E6.2: Korekta procesów (2027-12-16 do 2028-01-15)",
            "E6.3: Decyzja o dalszych inwestycjach (2028-01-16 do 2028-02-15)"
        ]
    }
    
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
    
    return fig, ax

# Generowanie wyczerpującego raportu
print("Generowanie wyczerpującego raportu harmonogramu...")
detailed_report = generate_detailed_schedule_report(tasks, "harmonogram_raport_szczegolowy.md")

# Generowanie czytelnej roadmapy tabelarycznej
print("\nGenerowanie czytelnej roadmapy tabelarycznej...")
fig_clean, ax_clean = generate_clean_roadmap_table(tasks, "roadmap_clean_table")

print("Wykres Gantta został zapisany do plików:")
print("- gantt_chart_digitalizacja.png (obraz PNG - szczegółowy)")
print("- gantt_chart_digitalizacja.pdf (plik PDF - szczegółowy)")
print("- harmonogram_etapy_gantt.png (obraz PNG - tylko etapy)")
print("- harmonogram_etapy_gantt.pdf (plik PDF - tylko etapy)")
print("- roadmap_infrastruktura_diagram.png (obraz PNG - roadmapa)")
print("- roadmap_infrastruktura_diagram.pdf (plik PDF - roadmapa)")
print("- harmonogram_szczegolowy.png (obraz PNG - bardzo szczegółowy)")
print("- harmonogram_szczegolowy.pdf (plik PDF - bardzo szczegółowy)")
print("- roadmap_clean_table.png (obraz PNG - czytelna roadmapa tabelaryczna)")
print("- roadmap_clean_table.pdf (plik PDF - czytelna roadmapa tabelaryczna)")
print("- struktura_projektu.md (struktura w markdown)")
print("- roadmap_struktura.md (szczegółowa dokumentacja roadmapy)")
print("- harmonogram_raport_szczegolowy.md (wyczerpujący raport harmonogramu)")

def generate_comprehensive_stream_roadmap(tasks, filename_prefix="roadmap_streams_comprehensive"):
    """
    Generuje wyczerpującą roadmapę z podziałem na 3 strumienie (Systemy, Dane i analityka, Bezpieczeństwo i zarządzanie)
    z 4 poziomami dojrzałości (0-3) na precyzyjnej osi czasowej Q4 2025-2027.
    Wszystkie zadania mają się mieścić na wykresie z maksymalną szczegółowością.
    """
    
    # === DEFINICJA STRUMIENI ===
    stream_definitions = {
        "Systemy": {
            "description": "PMS, booking engine, CRM, płatności, narzędzia marketingowe",
            "color_base": "#E74C3C",  # Czerwony
            "tasks_mapping": {
                0: {  # Poziom 0 - Stan wyjściowy
                    "description": "Brak PMS/CRM, tylko OTA + Excel",
                    "tasks": [],
                    "period": "Q4 2025"
                },
                1: {  # Poziom 1 - Podstawowa infrastruktura
                    "description": "Podstawowy PMS, booking engine, strona www",
                    "tasks": [
                        "E1.4: Wybór dostawcy PMS/booking engine (2026-02-15 do 2026-03-31)",
                        "E2.1: Projekt nowej strony www (2026-04-01 do 2026-05-31)",
                        "E2.2: Przygotowanie logo i szablonów graficznych (2026-04-01 do 2026-05-15)",
                        "E2.3: Wdrożenie nowej strony www (2026-06-01 do 2026-08-31)",
                        "E3.1: Uruchomienie booking engine (2026-10-01 do 2026-10-31)"
                    ],
                    "period": "Q1-Q4 2026"
                },
                2: {  # Poziom 2 - Systemy zintegrowane
                    "description": "PMS + płatności + CRM + channel manager",
                    "tasks": [
                        "E3.2: Uruchomienie płatności online (2026-11-01 do 2026-11-30)",
                        "E3.3: Integracja z OTA (channel manager) (2026-11-01 do 2026-12-15)",
                        "E4.1: Wdrożenie CRM (2027-01-16 do 2027-03-15)",
                        "E4.3: Uruchomienie programu lojalnościowego (2027-04-16 do 2027-05-15)"
                    ],
                    "period": "Q4 2026-Q2 2027"
                },
                3: {  # Poziom 3 - Zaawansowane systemy
                    "description": "Zautomatyzowane systemy marketingowe",
                    "tasks": [
                        "E4.4: Automatyczne e-maile przed/po pobycie (2027-05-16 do 2027-06-15)",
                        "E6.3: Decyzja o dalszych inwestycjach - chatbot, integracje (2028-01-16 do 2028-02-15)"
                    ],
                    "period": "Q2 2027-Q1 2028"
                }
            }
        },
        "Dane i analityka": {
            "description": "Od prostych raportów do zaawansowanych dashboardów",
            "color_base": "#3498DB",  # Niebieski
            "tasks_mapping": {
                0: {  # Poziom 0 - Stan wyjściowy
                    "description": "Brak raportowania, tylko Excel",
                    "tasks": [],
                    "period": "Q4 2025"
                },
                1: {  # Poziom 1 - Podstawowe raporty
                    "description": "Pierwsze raporty z systemu rezerwacji",
                    "tasks": [
                        "E2.4: Aktualizacja treści i zdjęć + podstawowe SEO (2026-07-01 do 2026-09-30)",
                        "E3.4: Testy procesu rezerwacji (2026-12-01 do 2026-12-31)",
                        "E4.2: Import dotychczasowych kontaktów (2027-03-16 do 2027-04-15)"
                    ],
                    "period": "Q3 2026-Q1 2027"
                },
                2: {  # Poziom 2 - Operacyjna analityka
                    "description": "Raporty operacyjne - obłożenie, kanały, RevPAR",
                    "tasks": [
                        "E5.1: Konfiguracja raportów (obłożenie, kanały, RevPAR) (2027-06-16 do 2027-08-15)",
                        "E5.3: Szkolenia z analityki i pracy na danych (2027-10-16 do 2027-11-15)"
                    ],
                    "period": "Q2-Q4 2027"
                },
                3: {  # Poziom 3 - Zaawansowana analityka
                    "description": "Dynamic pricing, dashboardy zarządcze, predykcje",
                    "tasks": [
                        "E5.2: Wdrożenie zasad dynamicznego ustalania cen (2027-08-16 do 2027-10-15)",
                        "E6.1: Przegląd KPI z IT BSC (2027-11-16 do 2027-12-15)"
                    ],
                    "period": "Q3 2027-Q1 2028"
                }
            }
        },
        "Bezpieczeństwo i zarządzanie": {
            "description": "Od braku polityk do formalnych zasad i procedur",
            "color_base": "#27AE60",  # Zielony
            "tasks_mapping": {
                0: {  # Poziom 0 - Stan wyjściowy
                    "description": "Brak formalnych polityk bezpieczeństwa",
                    "tasks": [],
                    "period": "Q4 2025"
                },
                1: {  # Poziom 1 - Podstawowe zarządzanie
                    "description": "Formalne rozpoczęcie, inwentaryzacja, budżet",
                    "tasks": [
                        "E1.1: Formalne uruchomienie programu (2026-01-01 do 2026-01-15)",
                        "E1.2: Inwentaryzacja obecnych narzędzi (2026-01-16 do 2026-02-28)",
                        "E1.3: Określenie budżetu IT na 2026-2027 (2026-02-01 do 2026-02-28)"
                    ],
                    "period": "Q1 2026"
                },
                2: {  # Poziom 2 - Procedury operacyjne
                    "description": "Ustalone procedury, backup, monitoring",
                    "tasks": [
                        "E2.5: Finalizacja strony www i identyfikacji (2026-09-01 do 2026-09-30)",
                        "E3.5: Start produkcyjny systemu rezerwacji (2027-01-01 do 2027-01-15)"
                    ],
                    "period": "Q3 2026-Q1 2027"
                },
                3: {  # Poziom 3 - Zaawansowane zarządzanie
                    "description": "Kompleksowe polityki, monitoring KPI, governance",
                    "tasks": [
                        "E6.2: Korekta procesów (2027-12-16 do 2028-01-15)"
                    ],
                    "period": "Q4 2027-Q1 2028"
                }
            }
        }
    }
    
    # === KONFIGURACJA WYKRESU ===
    fig, ax = plt.subplots(figsize=(24, 16))
    
    # Definicja okresów czasowych z precyzyjnymi datami
    time_periods = [
        {"label": "Q4 2025\n(Przygotowania)", "start": datetime(2025, 10, 1), "end": datetime(2025, 12, 31)},
        {"label": "Q1 2026\n(Start)", "start": datetime(2026, 1, 1), "end": datetime(2026, 3, 31)},
        {"label": "Q2 2026\n(Fundament)", "start": datetime(2026, 4, 1), "end": datetime(2026, 6, 30)},
        {"label": "Q3 2026\n(Budowa)", "start": datetime(2026, 7, 1), "end": datetime(2026, 9, 30)},
        {"label": "Q4 2026\n(Integracja)", "start": datetime(2026, 10, 1), "end": datetime(2026, 12, 31)},
        {"label": "Q1 2027\n(Produkcja)", "start": datetime(2027, 1, 1), "end": datetime(2027, 3, 31)},
        {"label": "Q2 2027\n(Rozwój)", "start": datetime(2027, 4, 1), "end": datetime(2027, 6, 30)},
        {"label": "Q3 2027\n(Analityka)", "start": datetime(2027, 7, 1), "end": datetime(2027, 9, 30)},
        {"label": "Q4 2027\n(Optymalizacja)", "start": datetime(2027, 10, 1), "end": datetime(2027, 12, 31)},
        {"label": "Q1 2028\n(Finalizacja)", "start": datetime(2028, 1, 1), "end": datetime(2028, 3, 31)}
    ]
    
    # === RYSOWANIE STRUKTURY ===
    # Pozycje Y dla strumieni
    y_stream_positions = {
        "Systemy": 12,
        "Dane i analityka": 8, 
        "Bezpieczeństwo i zarządzanie": 4
    }
    
    level_height = 0.8
    stream_spacing = 4
    
    # Ustawienia osi X (okresy czasowe)
    period_width = 2.0  # Szerokość każdego okresu
    x_positions = [i * period_width for i in range(len(time_periods))]
    
    ax.set_xlim(-0.5, len(time_periods) * period_width - 0.5)
    ax.set_ylim(0, 16)
    
    # === RYSOWANIE NAGŁÓWKÓW OKRESÓW ===
    for i, period in enumerate(time_periods):
        x_pos = x_positions[i]
        # Nagłówek okresu
        ax.add_patch(plt.Rectangle((x_pos - period_width/2 + 0.1, 15), period_width - 0.2, 0.8,
                                 facecolor='#2C3E50', alpha=0.9, edgecolor='white', linewidth=2))
        ax.text(x_pos, 15.4, period["label"], ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white')
        
        # Data szczegółowa
        date_text = f"{period['start'].strftime('%Y-%m-%d')}\ndo\n{period['end'].strftime('%Y-%m-%d')}"
        ax.text(x_pos, 14.2, date_text, ha='center', va='center', fontsize=8, color='#34495E')
    
    # === RYSOWANIE STRUMIENI ===
    for stream_name, stream_data in stream_definitions.items():
        y_base = y_stream_positions[stream_name]
        color_base = stream_data["color_base"]
        
        # Nagłówek strumienia
        ax.text(-1, y_base + 1.5, f"🔧 {stream_name}", ha='right', va='center', 
               fontsize=14, fontweight='bold', color=color_base)
        ax.text(-1, y_base + 1.0, stream_data["description"], ha='right', va='center', 
               fontsize=10, color='#7F8C8D', style='italic')
        
        # Rysowanie poziomów dojrzałości dla każdego strumienia
        for level in range(4):  # Poziomy 0-3
            y_pos = y_base - level * level_height
            level_data = stream_data["tasks_mapping"][level]
            
            # Nagłówek poziomu
            ax.text(-0.3, y_pos, f"Poziom {level}", ha='right', va='center', 
                   fontsize=11, fontweight='bold', color=color_base)
            ax.text(-0.3, y_pos - 0.3, level_data["description"], ha='right', va='center', 
                   fontsize=9, color='#7F8C8D', style='italic')
            
            # Zadania w odpowiednich okresach
            if level_data["tasks"]:
                for task_text in level_data["tasks"]:
                    # Wyodrębnienie dat z tekstu zadania
                    if "(202" in task_text and " do " in task_text:
                        try:
                            date_part = task_text.split("(")[1].split(")")[0]
                            if " do " in date_part:
                                start_date_str = date_part.split(" do ")[0]
                                end_date_str = date_part.split(" do ")[1]
                                
                                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
                                end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
                                
                                # Znajdowanie odpowiednich okresów dla zadania
                                for i, period in enumerate(time_periods):
                                    if (start_date >= period["start"] and start_date <= period["end"]) or \
                                       (end_date >= period["start"] and end_date <= period["end"]) or \
                                       (start_date <= period["start"] and end_date >= period["end"]):
                                        
                                        x_pos = x_positions[i]
                                        
                                        # Rysowanie zadania jako kolorowego prostokąta
                                        from matplotlib.patches import FancyBboxPatch
                                        task_rect = FancyBboxPatch(
                                            (x_pos - period_width/2 + 0.05, y_pos - 0.3), 
                                            period_width - 0.1, 0.6,
                                            boxstyle="round,pad=0.02",
                                            facecolor=color_base,
                                            alpha=0.8,
                                            edgecolor='white',
                                            linewidth=1
                                        )
                                        ax.add_patch(task_rect)
                                        
                                        # Tekst zadania
                                        task_id = task_text.split(":")[0]
                                        task_name = task_text.split(": ")[1].split(" (")[0]
                                        
                                        ax.text(x_pos, y_pos + 0.1, task_id, ha='center', va='center', 
                                               fontsize=9, fontweight='bold', color='white')
                                        ax.text(x_pos, y_pos - 0.1, task_name[:25] + ("..." if len(task_name) > 25 else ""), 
                                               ha='center', va='center', fontsize=7, color='white')
                                        break  # Tylko jeden prostokąt na zadanie
                        except (IndexError, ValueError) as e:
                            print(f"Błąd parsowania daty dla zadania: {task_text} - {e}")
                            continue
            else:
                # Poziom 0 - stan wyjściowy (pustka)
                for i in range(1):  # Tylko pierwszy okres
                    x_pos = x_positions[i]
                    ax.add_patch(plt.Rectangle((x_pos - period_width/2 + 0.05, y_pos - 0.3), 
                                             period_width - 0.1, 0.6,
                                             facecolor='#BDC3C7', alpha=0.5, 
                                             edgecolor='#95A5A6', linewidth=1))
                    ax.text(x_pos, y_pos, "BRAK", ha='center', va='center', 
                           fontsize=10, fontweight='bold', color='#7F8C8D')
    
    # === FINALIZACJA WYKRESU ===
    # Usunięcie osi
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Tytuł główny
    ax.text(len(time_periods) * period_width / 2, 17.5, 
           "WYCZERPUJĄCA ROADMAPA DIGITALIZACJI HOTELU", 
           ha='center', va='center', fontsize=20, fontweight='bold', color='#2C3E50')
    
    # Podtytuł
    ax.text(len(time_periods) * period_width / 2, 17, 
           "Podział na 3 strumienie × 4 poziomy dojrzałości × precyzyjne przedziały czasowe", 
           ha='center', va='center', fontsize=14, color='#34495E')
    
    # Informacja o zakresie
    ax.text(len(time_periods) * period_width / 2, 16.5, 
           "📅 Q4 2025 - Q1 2028 | 📋 24 zadania | 🎯 6 etapów | 🔄 3 strumienie transformacji", 
           ha='center', va='center', fontsize=12, color='#7F8C8D')
    
    # Legenda strumieni
    legend_y = 0.5
    for stream_name, stream_data in stream_definitions.items():
        legend_x = list(stream_definitions.keys()).index(stream_name) * 6 + 2
        ax.add_patch(plt.Rectangle((legend_x, legend_y), 1, 0.5,
                                 facecolor=stream_data["color_base"], alpha=0.8))
        ax.text(legend_x + 1.2, legend_y + 0.25, stream_name, 
               ha='left', va='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    
    # Zapisanie do plików
    plt.savefig(f"{filename_prefix}.png", dpi=300, bbox_inches="tight", 
               facecolor='white', edgecolor='none')
    plt.savefig(f"{filename_prefix}.pdf", bbox_inches="tight", 
               facecolor='white', edgecolor='none')
    
    print(f"Zapisano wyczerpującą roadmapę strumieni do pliku: {filename_prefix}.png")
    print(f"Zapisano wyczerpującą roadmapę strumieni do pliku: {filename_prefix}.pdf")
    
    return fig, ax, stream_definitions

# Generowanie wyczerpującej roadmapy strumieni
print("\n🎯 Generowanie wyczerpującej roadmapy z podziałem na 3 strumienie...")
fig_streams, ax_streams, streams_data = generate_comprehensive_stream_roadmap(tasks, "roadmap_streams_comprehensive")

def generate_streams_documentation(streams_data, tasks, filename="roadmap_streams_dokumentacja.md"):
    """
    Generuje wyczerpującą dokumentację roadmapy z 3 strumieniami
    """
    df = pd.DataFrame(tasks)
    
    markdown = "# 🚀 WYCZERPUJĄCA ROADMAPA TRANSFORMACJI CYFROWEJ\n\n"
    markdown += "## 📋 Podział na 3 strumienie × 4 poziomy dojrzałości × precyzyjne przedziały czasowe\n\n"
    markdown += f"**Okres realizacji:** Q4 2025 - Q1 2028\n"
    markdown += f"**Łączna liczba zadań:** {len(df)} zadań\n"
    markdown += f"**Liczba etapów:** {df['phase'].nunique()} etapów\n"
    markdown += f"**Liczba strumieni:** 3 strumienie transformacji\n\n"
    
    markdown += "---\n\n"
    
    # Szczegółowy opis każdego strumienia
    for stream_name, stream_data in streams_data.items():
        markdown += f"## 🎯 STRUMIEŃ: {stream_name.upper()}\n\n"
        markdown += f"**Opis:** {stream_data['description']}\n\n"
        
        # Analiza zadań według poziomów
        for level in range(4):
            level_data = stream_data["tasks_mapping"][level]
            markdown += f"### 📊 Poziom {level} - {level_data['description']}\n\n"
            markdown += f"**Okres realizacji:** {level_data['period']}\n\n"
            
            if level_data["tasks"]:
                markdown += f"**Liczba zadań:** {len(level_data['tasks'])}\n\n"
                markdown += "**Szczegółowa lista zadań:**\n\n"
                
                for i, task_text in enumerate(level_data["tasks"], 1):
                    # Parsowanie zadania
                    task_id = task_text.split(":")[0]
                    task_name = task_text.split(": ")[1].split(" (")[0]
                    
                    if "(202" in task_text and " do " in task_text:
                        date_part = task_text.split("(")[1].split(")")[0]
                        if " do " in date_part:
                            start_date_str = date_part.split(" do ")[0]
                            end_date_str = date_part.split(" do ")[1]
                            duration_days = (datetime.strptime(end_date_str, "%Y-%m-%d") - 
                                           datetime.strptime(start_date_str, "%Y-%m-%d")).days + 1
                            
                            markdown += f"{i}. **{task_id}:** {task_name}\n"
                            markdown += f"   - 📅 **Okres:** {start_date_str} do {end_date_str}\n"
                            markdown += f"   - ⏱️ **Czas trwania:** {duration_days} dni\n"
                            
                            # Dodatkowe informacje z głównego harmonogramu
                            task_df = df[df['id'] == task_id]
                            if not task_df.empty:
                                task_info = task_df.iloc[0]
                                markdown += f"   - 👥 **Zasoby:** {task_info['resource']}\n"
                                markdown += f"   - 💰 **Obszar kosztów:** {task_info['cost_area']}\n"
                                if task_info['milestone']:
                                    markdown += f"   - 🎯 **Kamień milowy:** TAK\n"
                                if task_info['dependencies']:
                                    markdown += f"   - 🔗 **Zależności:** {', '.join(task_info['dependencies'])}\n"
                            markdown += "\n"
            else:
                markdown += f"**Stan:** Brak zadań projektowych - stan wyjściowy\n\n"
            
            markdown += "---\n\n"
        
        markdown += "\n"
    
    # Analiza czasowa
    markdown += "## 📅 ANALIZA CZASOWA\n\n"
    
    # Statystyki według kwartałów
    df['quarter'] = df['start'].dt.quarter
    df['year'] = df['start'].dt.year
    df['quarter_year'] = df['year'].astype(str) + ' Q' + df['quarter'].astype(str)
    
    markdown += "### Rozkład zadań według kwartałów:\n\n"
    markdown += "| Kwartał | Liczba zadań | Główne strumienie |\n"
    markdown += "|---------|--------------|-------------------|\n"
    
    for quarter in sorted(df['quarter_year'].unique()):
        quarter_tasks = df[df['quarter_year'] == quarter]
        task_count = len(quarter_tasks)
        
        # Analiza głównych strumieni w kwartale
        streams_in_quarter = []
        for _, task in quarter_tasks.iterrows():
            task_id = task['id']
            for stream_name, stream_data in streams_data.items():
                for level in range(4):
                    for task_text in stream_data["tasks_mapping"][level]["tasks"]:
                        if task_id in task_text:
                            streams_in_quarter.append(stream_name)
                            break
        
        main_streams = ", ".join(list(set(streams_in_quarter)))
        markdown += f"| {quarter} | {task_count} | {main_streams} |\n"
    
    markdown += "\n"
    
    # Kamienie milowe według strumieni
    milestones = df[df['milestone'] == True]
    if not milestones.empty:
        markdown += "### 🎯 Kamienie milowe według strumieni:\n\n"
        
        for stream_name, stream_data in streams_data.items():
            markdown += f"#### {stream_name}:\n\n"
            stream_milestones = []
            
            for _, milestone in milestones.iterrows():
                task_id = milestone['id']
                for level in range(4):
                    for task_text in stream_data["tasks_mapping"][level]["tasks"]:
                        if task_id in task_text:
                            stream_milestones.append({
                                'id': task_id,
                                'name': milestone['name'],
                                'date': milestone['end'],
                                'level': level
                            })
                            break
            
            if stream_milestones:
                for milestone in sorted(stream_milestones, key=lambda x: x['date']):
                    markdown += f"- **{milestone['date'].strftime('%Y-%m-%d')}:** {milestone['id']} - {milestone['name']} (Poziom {milestone['level']})\n"
            else:
                markdown += "- Brak kamieni milowych\n"
            markdown += "\n"
    
    # Zależności między strumieniami
    markdown += "### 🔗 Analiza zależności między strumieniami:\n\n"
    
    all_dependencies = []
    for _, task in df.iterrows():
        if task['dependencies']:
            for dep in task['dependencies']:
                # Znajdź strumień zadania źródłowego i docelowego
                source_stream = None
                target_stream = None
                
                # Znajdź strumień dla zależności
                for stream_name, stream_data in streams_data.items():
                    for level in range(4):
                        for task_text in stream_data["tasks_mapping"][level]["tasks"]:
                            if dep in task_text:
                                source_stream = stream_name
                            if task['id'] in task_text:
                                target_stream = stream_name
                
                if source_stream and target_stream and source_stream != target_stream:
                    all_dependencies.append(f"{dep} ({source_stream}) → {task['id']} ({target_stream})")
    
    if all_dependencies:
        for dependency in all_dependencies:
            markdown += f"- {dependency}\n"
    else:
        markdown += "- Większość zależności występuje w ramach tego samego strumienia\n"
    
    markdown += "\n"
    
    # Rekomendacje
    markdown += "## 💡 REKOMENDACJE I WNIOSKI\n\n"
    markdown += "### Kluczowe obserwacje:\n\n"
    markdown += "1. **Strumień 'Systemy'** stanowi fundament transformacji - większość zadań w poziomach 1-2\n"
    markdown += "2. **Strumień 'Dane i analityka'** rozwija się stopniowo od Q3 2026, osiąga dojrzałość w Q3-Q4 2027\n"
    markdown += "3. **Strumień 'Bezpieczeństwo i zarządzanie'** zapewnia governance przez cały projekt\n\n"
    
    markdown += "### Rekomendowane podejście:\n\n"
    markdown += "- **Fazowe podejście:** Każdy strumień ma swój rytm rozwoju dostosowany do potrzeb biznesowych\n"
    markdown += "- **Synchronizacja strumieni:** Kluczowe kamienie milowe są skoordynowane między strumieniami\n"
    markdown += "- **Minimalne ryzyko:** Bezpieczeństwo i zarządzanie rozwijane równolegle z systemami\n\n"
    
    # Zapisanie do pliku
    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)
    
    print(f"Zapisano wyczerpującą dokumentację strumieni do pliku: {filename}")
    return markdown

# Generowanie dokumentacji strumieni
print("\n📚 Generowanie wyczerpującej dokumentacji strumieni...")
streams_documentation = generate_streams_documentation(streams_data, tasks, "roadmap_streams_dokumentacja.md")

# Podsumowanie wszystkich wygenerowanych plików
print("\n" + "="*80)
print("🎉 WSZYSTKIE PLIKI ROADMAPY ZOSTAŁY WYGENEROWANE POMYŚLNIE!")
print("="*80)
print("\n📊 PLIKI WIZUALNE:")
print("- gantt_chart_digitalizacja.png/pdf (szczegółowy wykres Gantta)")
print("- harmonogram_etapy_gantt.png/pdf (uproszczony wykres z etapami)")
print("- roadmap_infrastruktura_diagram.png/pdf (podstawowa roadmapa poziomów)")
print("- harmonogram_szczegolowy.png/pdf (bardzo szczegółowy harmonogram)")
print("- roadmap_clean_table.png/pdf (czytelna roadmapa tabelaryczna)")
print("- roadmap_streams_comprehensive.png/pdf (🆕 WYCZERPUJĄCA ROADMAPA 3 STRUMIENI)")
print("\n📋 PLIKI DOKUMENTACYJNE:")
print("- struktura_projektu.md (podstawowa struktura)")
print("- roadmap_struktura.md (dokumentacja poziomów roadmapy)")
print("- harmonogram_raport_szczegolowy.md (szczegółowy raport harmonogramu)")
print("- roadmap_streams_dokumentacja.md (🆕 WYCZERPUJĄCA DOKUMENTACJA STRUMIENI)")
print("\n💾 DANE EKSPORTOWE:")
print("- [Pliki CSV i inne formaty dostępne w poprzednich funkcjach]")
print("\n🎯 NOWA ROADMAPA 3 STRUMIENI zawiera:")
print("✅ Wszystkie 24 zadania zmapowane do odpowiednich strumieni")
print("✅ 4 poziomy dojrzałości (0-3) dla każdego strumienia")
print("✅ Precyzyjne przedziały czasowe Q4 2025 - Q1 2028")
print("✅ Kolorowe kodowanie i szczegółowe etykiety zadań")
print("✅ Kompletną dokumentację z analizą zależności i rekomendacjami")

# plt.show()