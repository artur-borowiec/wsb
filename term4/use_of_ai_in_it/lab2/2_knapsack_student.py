def knapsack(max_capacity, weights, values, n):
    # Tablica K o rozmiarach (n+1) x (max_capacity+1) jest inicjalizowana zerami. K[i][w] będzie przechowywać
    # maksymalną wartość, którą można osiągnąć używając pierwszych i przedmiotów i nie przekraczając wagi w.
    K = [[0 for x in range(max_capacity + 1)] for x in range(n + 1)]

    # Budowanie tablicy:
    # Iterujemy przez każdy przedmiot (i od 1 do n) i każdą możliwą wagę plecaka.

    # Jeżeli przedmiot mieści się w plecaku (weights[i-1] <= w), możemy nie wziąć przedmiotu: wtedy wartość jest taka
    # sama jak bez tego przedmiotu (K[i-1][w]) lub wziąć przedmiot, wtedy wartość to suma wartości tego przedmiotu
    # (values[i-1]) i najlepszej wartości dla pozostałej pojemności plecaka po wzięciu tego przedmiotu.
    # Wybieramy większą wartość z tych dwóch opcji.
    # Jeśli przedmiot się nie mieści, to jedyną opcją jest nie wzięcie przedmiotu.
    for i in range(n + 1):
        for w in range(max_capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Po zakończeniu wszystkich iteracji, K[n][max_capacity] zawiera maksymalną wartość, jaką można uzyskać dla danych
    # przedmiotów przy danej pojemności plecaka.
    return K[n][max_capacity]


# Przykładowe dane
values = [60, 100, 120]  # wartości przedmiotów
weights = [10, 20, 30]  # wagi przedmiotów
max_capacity = 50  # maksymalna pojemność plecaka
n = len(values)  # liczba dostępnych przedmiotów

# Wywołanie funkcji
result = knapsack(max_capacity, weights, values, n)
print("Maksymalna wartość, którą można wynieść to:", result)
