def car_purchase_decision(budget, brand, max_age, max_mileage, fuel_type):
    # Przykładowe dane o minimalnych cenach rynkowych dla różnych marek
    minimum_prices = {'Toyota': 20000, 'BMW': 30000, 'Ford': 15000}
    # Przykładowe maksymalne wiek i przebieg dla samochodu
    car_data = {'Toyota': (10, 150000), 'BMW': (8, 120000), 'Ford': (12, 200000)}

    # Sprawdzenie, czy budżet wystarcza na zakup samochodu danej marki
    if budget < minimum_prices[brand]:
        return "NIE - Budżet za niski."

    # Sprawdzenie, czy samochód mieści się w dopuszczalnym wieku i przebiegu
    allowable_age, allowable_mileage = car_data[brand]
    if max_age > allowable_age or max_mileage > allowable_mileage:
        return "NIE - Samochód zbyt stary lub zbyt wysoki przebieg."

    # Dodatkowe preferencje dotyczące typu paliwa
    if fuel_type not in ['benzyna', 'diesel', 'elektryk', 'hybryda']:
        return "NIE - Nieobsługiwany typ paliwa."

    return "TAK - Możesz kupić samochód."


# Zbieranie danych wejściowych od użytkownika
budget = float(input("Podaj swój budżet na samochód (zł): "))
brand = input("Jakiej marki samochód chcesz kupić? (Toyota/BMW/Ford): ")
max_age = int(input("Jaki jest maksymalny akceptowalny wiek samochodu (w latach)?: "))
max_mileage = int(input("Jaki jest maksymalny akceptowalny przebieg samochodu (w km)?: "))
fuel_type = input("Jaki typ paliwa preferujesz? (benzyna/diesel/elektryk/hybryda): ")

# Podjęcie decyzji na podstawie danych wejściowych
decision = car_purchase_decision(budget, brand, max_age, max_mileage, fuel_type)
print("Decyzja:", decision)
