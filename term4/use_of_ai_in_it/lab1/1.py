import heapq
import math

def tsp_a_star(start, end, graph, coordinates):
    """Rozwiązuje problem komiwojażera używając algorytmu A*.

    Args:
        start: Miasto początkowe.
        end: Miasto końcowe.
        graph: Graf reprezentujący miasta i połączenia (słownik list sąsiedztwa).
        coordinates: Słownik współrzędnych dla każdego miasta.

    Returns:
        Listę miast reprezentującą odwiedzoną ścieżkę.
    """
    open_set = []  # Kolejka priorytetowa przechowująca stany do przetworzenia.
    # Wstawienie stanu początkowego: (koszt początkowy, miasto startowe, odwiedzone miasta, ścieżka).
    heapq.heappush(open_set, (0, start, frozenset([start]), [start]))

    while open_set:
        # Pobranie stanu o najniższym przewidywanym koszcie z kolejki.
        current_cost, current_city, visited, path = heapq.heappop(open_set)

        # Sprawdzenie, czy to stan końcowy (wszystkie miasta odwiedzone i znajdujemy się w mieście końcowym).
        if len(visited) == len(graph) and current_city == end:
            return path

        # Rozwijanie stanu przez przeglądanie wszystkich sąsiednich miast.
        for next_city, travel_cost in graph[current_city]:
            # Sprawdzamy, czy miasto zostało już odwiedzone, lub czy jest to ostatni krok do miasta końcowego.
            if next_city not in visited or (len(visited) == len(graph) - 1 and next_city == end):
                new_visited = visited | {next_city}  # Dodanie miasta do zbioru odwiedzonych.
                new_cost = current_cost + travel_cost  # Zaktualizowanie kosztu trasy.
                new_path = path + [next_city]  # Dodanie miasta do ścieżki.
                # Wstawienie nowego stanu do kolejki.
                heapq.heappush(open_set, (new_cost, next_city, new_visited, new_path))

    return "No complete tour found"

# Przykład danych
cities_coordinates = {
    'Wrocław': (51.107883, 17.038538),
    'Poznań': (52.406374, 16.925168),
    'Łódź': (51.759248, 19.455983),
    'Warszawa': (52.229676, 21.012229),
    'Gdańsk': (54.352025, 18.646638)
}

graph = {
    'Wrocław': [('Poznań', 180), ('Łódź', 220)],
    'Poznań': [('Gdańsk', 300), ('Warszawa', 310)],
    'Łódź': [('Warszawa', 140), ('Wrocław', 220)],
    'Warszawa': [('Gdańsk', 280), ('Poznań', 310)],
    'Gdańsk': [('Wrocław', 450), ('Poznań', 300)]
}

start_city = 'Wrocław'
end_city = 'Gdańsk'

# Wywołanie funkcji
path = tsp_a_star(start_city, end_city, graph, cities_coordinates)
print("Ścieżka TSP:", path)
