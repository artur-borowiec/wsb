def nearest_neighbor(start, end, graph):
    # Inicjalizacja zbioru odwiedzonych miast i ścieżki podróży
    visited = set()
    path = [start]
    current = start
    visited.add(current)

    # Główna pętla działa dopóki wszystkie miasta w grafie nie zostaną odwiedzone
    while len(visited) < len(graph):
        neighbors = graph[current]
        next_node = None
        min_distance = float('inf')

        # Wyszukuje sąsiada z najkrótszą dostępną odległością, który nie został jeszcze odwiedzony
        for neighbor, distance in neighbors:
            if neighbor not in visited and distance < min_distance:
                min_distance = distance
                next_node = neighbor

        # Sprawdza czy jest możliwe znalezienie kolejnego miasta do odwiedzenia
        if next_node is None:
            return "Route not possible or graph disconnected"

        # Aktualizuje ścieżkę i zbiór odwiedzonych miast
        path.append(next_node)
        visited.add(next_node)
        current = next_node

    # Dodaje przejście do miasta końcowego, jeśli nie jest to ostatnie odwiedzone miasto
    if current != end:
        if end in [city for city, _ in graph[current]]:
            path.append(end)
        else:
            return "No direct route to final city from the last city"

    return path


# Przykład grafu miast gdzie klucze to miasta a wartości to listy sąsiadów i odległości do nich
graph = {
    'Wrocław': [('Poznań', 180), ('Łódź', 220)],
    'Poznań': [('Gdańsk', 300), ('Łódź', 200)],
    'Łódź': [('Warszawa', 140)],
    'Warszawa': [('Gdańsk', 300)],
    'Gdańsk': []
}

start_city = 'Wrocław'
end_city = 'Gdańsk'

# Wywołanie funkcji algorytmu najbliższego sąsiada
path = nearest_neighbor(start_city, end_city, graph)
print("Ścieżka:", path)
