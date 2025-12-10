import matplotlib.pyplot as plt
import matplotlib.patches as patches

def tq(year, quarter, base_year=2025):
    # year – rok (np. 2026)
    # quarter – kwartał 1..4
    # base_year – rok, od którego liczymy (tu 2025)
    # wynik: liczba zmiennoprzecinkowa, gdzie 0 = Q1 base_year
    return (year - base_year) + (quarter - 1) / 4.0

# Definicja strumieni
streams = {
    "systems": {"name": "Systemy", "color": "#FFB6C1", "y_offset": 0},
    "data": {"name": "Dane i analityka", "color": "#87CEEB", "y_offset": 1},
    "security": {"name": "Bezpieczeństwo i zarządzanie", "color": "#98FB98", "y_offset": 2}
}

# Nowa struktura poziomów z podziałem na strumienie
levels = [
    {
        "name": "Poziom 0 – Stan wyjściowy",
        "level": 0,
        "start": (2025, 4),
        "end": (2025, 4),
        "streams": {
            "systems": [
                "Brak PMS/CRM",
                "Panel OTA",
                "Arkusze Excel"
            ],
            "data": [
                "Brak raportów",
                "Brak systematycznej analizy",
                "Ręczne prowadzenie ewidencji"
            ],
            "security": [
                "Brak formalnych polityk bezpieczeństwa",
                "Brak procedur backupu",
                "Niekontrolowany dostęp do danych"
            ]
        }
    },
    {
        "name": "Poziom 1 – Podstawowa infrastruktura rezerwacyjna",
        "level": 1,
        "start": (2026, 1),
        "end": (2026, 4),
        "streams": {
            "systems": [
                "Nowa strona www",
                "PMS + booking engine",
                "Channel manager",
                "Płatności online"
            ],
            "data": [
                "Podstawowe raporty z PMS",
                "Statystyki rezerwacji",
                "Analiza obłożenia"
            ],
            "security": [
                "Wstępne porządkowanie dostępu",
                "Podstawowe kopie danych",
                "Procedury logowania"
            ]
        }
    },
    {
        "name": "Poziom 2 – Infrastruktura relacyjna",
        "level": 2,
        "start": (2027, 1),
        "end": (2027, 2),
        "streams": {
            "systems": [
                "PMS zintegrowany z CRM",
                "Program lojalnościowy",
                "Automatyczne e-maile",
                "Integracja z booking engine"
            ],
            "data": [
                "Raporty operacyjne",
                "Analiza kanałów sprzedaży",
                "Tracking przychodów",
                "Segmentacja klientów"
            ],
            "security": [
                "Procedury backupu",
                "Ochrona danych klientów",
                "Kontrola dostępu",
                "Polityki prywatności"
            ]
        }
    },
    {
        "name": "Poziom 3 – Infrastruktura analityczna i rozwojowa",
        "level": 3,
        "start": (2027, 2),
        "end": (2027, 4),
        "streams": {
            "systems": [
                "Marketing automation",
                "Rozszerzone konfiguracje PMS/CRM",
                "Narzędzia segmentacji",
                "Chatbot (opcjonalnie)"
            ],
            "data": [
                "Dashboardy KPI",
                "Metryki RevPAR, ADR",
                "Analiza udziału kanałów",
                "Dynamic pricing",
                "Predykcyjne modele obłożenia"
            ],
            "security": [
                "Formalne procedury bezpieczeństwa",
                "Regularne backupy",
                "Przeglądy KPI",
                "Audyty bezpieczeństwa",
                "Zarządzanie zgodnością"
            ]
        }
    }
]

# Tworzenie wykresu
fig, ax = plt.subplots(figsize=(18, 14))

# Parametry układu
stream_height = 1.0  # wysokość jednego strumienia
level_spacing = 0.3  # odstęp między poziomami
stream_spacing = 0.1  # odstęp między strumieniami
item_height = 0.15   # wysokość pojedynczego elementu

# Funkcja do rysowania elementów w strumieniu
def draw_stream_items(ax, level, stream_key, start_x, width, base_y):
    stream_info = streams[stream_key]
    items = level["streams"][stream_key]
    color = stream_info["color"]
    
    # Rysowanie tła strumienia
    # ax.barh(base_y, width, left=start_x, height=stream_height,
    #         color=color, alpha=0.3, edgecolor='black', linewidth=0.5)
    
    # Dodanie etykiety strumienia po lewej stronie
    ax.text(-1.0, base_y + stream_height/2, stream_info["name"],
            va="center", ha="right", fontsize=11, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
    
    # Rysowanie poszczególnych elementów
    item_y_start = base_y + 0.1
    for i, item in enumerate(items):
        item_y = item_y_start + i * (item_height + 0.05)
        if item_y + item_height <= base_y + stream_height - 0.1:
            # Rysowanie prostokąta dla elementu
            rect = plt.Rectangle((start_x + 0.05, item_y), width - 0.1, item_height,
                               facecolor=color, alpha=0.7, edgecolor='darkgray', linewidth=0.5)
            ax.add_patch(rect)
            
            # Dodanie tekstu elementu
            ax.text(start_x + width/2, item_y + item_height/2, item,
                   va="center", ha="center", fontsize=8, wrap=True)

# Funkcja do rysowania poziomych linii oddzielających strumienie
def draw_stream_separators(ax, y_positions):
    for y in y_positions:
        ax.axhline(y, color='gray', linestyle='--', alpha=0.7, linewidth=1)

# Rysowanie poziomów i strumieni
y_current = 0.8  # Start z offsetem dla pierwszego tytułu
separator_lines = []

for level in levels:
    # Obliczanie pozycji czasowej (ze skalowaniem 3x)
    if level['start'] == level['end']:
        start_x = tq(level['start'][0], level['start'][1]) * 3
        width = 0.75 * 3  # Zwiększona szerokość dla lepszej czytelności
    else:
        start_x = tq(level['start'][0], level['start'][1]) * 3
        end_x = tq(level['end'][0], level['end'][1] + 1) * 3
        width = end_x - start_x
    
    # Dodanie tytułu poziomu NA POCZĄTKU sekcji
    title_y = y_current - 0.4  # Tytuł powyżej strumieni
    ax.text(start_x + width/2, title_y, level["name"],
           va="center", ha="center", fontsize=12, fontweight="bold",
           bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))
    
    # Rysowanie strumieni dla tego poziomu - zaczynamy od y_current
    stream_keys = ["systems", "data", "security"]
    for i, stream_key in enumerate(stream_keys):
        # Pozycja strumienia liczona od y_current
        stream_y = y_current + i * (stream_height + stream_spacing)
        draw_stream_items(ax, level, stream_key, start_x, width, stream_y)
        
        # Dodanie linii oddzielającej strumienie (oprócz ostatniego)
        if i < len(stream_keys) - 1:
            separator_y = stream_y + stream_height + stream_spacing/2
            separator_lines.append(separator_y)
    
    # Przesunięcie do następnego poziomu - uwzględniamy strumienie i odstęp
    y_current += 3 * stream_height + 2 * stream_spacing + level_spacing + 0.4

# Rysowanie linii oddzielających strumienie
draw_stream_separators(ax, separator_lines)

# Konfiguracja osi X
x_ticks = []
x_labels = []
for year in range(2025, 2028):
    for quarter in range(1, 5):
        if year == 2025 and quarter < 4:
            continue
        x_pos = tq(year, quarter) * 3  # Skalowanie 3x
        x_ticks.append(x_pos)
        x_labels.append(f"Q{quarter} {year}")

ax.set_xticks(x_ticks)
ax.set_xticklabels(x_labels, rotation=45, ha='right')

# Ukrycie osi Y (poziomy będą opisane tytułami)
ax.set_yticks([])

# Dodanie tytułu wykresu
ax.set_title("Roadmapa rozwoju infrastruktury cyfrowej pensjonatu (2025–2027)\nPodział na strumienie rozwoju", 
             fontsize=14, fontweight='bold', pad=30)
ax.set_xlabel("Czas (kwartały)", fontsize=12)

# Ustawienia zakresu osi
ax.set_xlim((tq(2025, 4) - 0.2) * 3, (tq(2027, 4) + 0.4) * 3)
ax.set_ylim(-0.5, y_current + 0.5)

# Dodanie siatki pionowej
ax.grid(True, axis='x', alpha=0.3, linestyle='-')

# Dodanie legendy strumieni
legend_elements = []
for stream_key, stream_info in streams.items():
    legend_elements.append(plt.Rectangle((0, 0), 1, 1, facecolor=stream_info["color"], 
                                       alpha=0.7, label=stream_info["name"]))

ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.15, 1))

# Dostosowanie układu
plt.tight_layout()

# Zapisanie wykresu do pliku
plt.savefig('roadmap_infrastruktury.png', dpi=300, bbox_inches='tight')
print("Wykres został zapisany jako roadmap_infrastruktury.png")

# Wyświetlenie wykresu (opcjonalnie)
# plt.show()