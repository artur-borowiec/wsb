def knapsack_with_limits(items, max_weight):
    n = len(items)
    # Tworzymy tablicę dp, gdzie dp[i][w] to maksymalna wartość, jaką można osiągnąć dla wagi w używając pierwsze i
    # przedmiotów
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    # Tablica, która pomoże śledzić, które przedmioty zostały wybrane
    item_count = [[(0, [])] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, price, weight, quantity = items[i - 1]
        for w in range(max_weight + 1):
            dp[i][w] = dp[i - 1][w]
            item_count[i][w] = item_count[i - 1][w]
            # Próbujemy dodać przedmioty od 1 do quantity, jeśli waga na to pozwala
            for q in range(1, min(quantity, w // weight) + 1):
                current_value = dp[i - 1][w - q * weight] + q * price
                if current_value > dp[i][w]:
                    dp[i][w] = current_value
                    item_count[i][w] = (q, item_count[i - 1][w - q * weight][1] + [(name, q)])

    # Znajdujemy rozwiązanie
    max_value = dp[n][max_weight]
    result = item_count[n][max_weight][1]

    # Wypisujemy wyniki
    print("Max Value:", max_value)
    print("Items to buy:")
    for item in result:
        print(f"{item[0]}: {item[1]}")


# Przykładowe dane
num_offers = 4
max_weight = 50
items = [
    ("Laptop", 1000, 3, 2),
    ("Telefon", 500, 1, 3),
    ("Książka", 200, 2, 10),
    ("Zegarek", 300, 1, 4)
]

knapsack_with_limits(items, max_weight)
