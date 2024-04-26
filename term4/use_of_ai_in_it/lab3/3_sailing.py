def can_we_sail(wind_speed, is_raining):
    if wind_speed > 15 and not is_raining:
        return "Tak, możemy popłynąć żaglówką."
    elif wind_speed <= 15:
        return "Nie, wiatr jest za słaby do żeglowania."
    elif is_raining:
        return "Nie, nie możemy popłynąć, ponieważ pada deszcz."


# Zbieranie danych wejściowych
wind_speed = float(input("Podaj prędkość wiatru (w km/h): "))
is_raining = input("Czy pada deszcz? (tak/nie): ").lower() == 'tak'

# Podjęcie decyzji na podstawie danych wejściowych
decision = can_we_sail(wind_speed, is_raining)
print("Decyzja:", decision)
