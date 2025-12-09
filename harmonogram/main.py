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

print("Wykres Gantta został zapisany do plików:")
print("- gantt_chart_digitalizacja.png (obraz PNG - szczegółowy)")
print("- gantt_chart_digitalizacja.pdf (plik PDF - szczegółowy)")
print("- harmonogram_etapy_gantt.png (obraz PNG - tylko etapy)")
print("- harmonogram_etapy_gantt.pdf (plik PDF - tylko etapy)")
print("- struktura_projektu.md (struktura w markdown)")

# plt.show()