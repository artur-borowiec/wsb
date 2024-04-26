import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definicja zakresów dla zmiennych wejściowych i wyjściowej w systemie rozmytym
wind_speed = ctrl.Antecedent(np.arange(0, 101, 1), 'wind_speed')  # Prędkość wiatru (0-100 km/h)
rain_chance = ctrl.Antecedent(np.arange(0, 101, 1), 'rain_chance')  # Szansa na deszcz (0-100%)
sailing = ctrl.Consequent(np.arange(0, 101, 1), 'sailing')  # Szanse na żeglowanie jako wyjście (0-100%)

# Definicja funkcji przynależności dla każdej ze zmiennych
# Funkcje przynależności dla prędkości wiatru
wind_speed['low'] = fuzz.trimf(wind_speed.universe, [0, 0, 20])  # Niska prędkość: 0-20 km/h
wind_speed['medium'] = fuzz.trimf(wind_speed.universe, [10, 30, 50])  # Średnia prędkość: 10-50 km/h
wind_speed['high'] = fuzz.trimf(wind_speed.universe, [40, 60, 100])  # Wysoka prędkość: 40-100 km/h

# Funkcje przynależności dla szansy na deszcz
rain_chance['low'] = fuzz.trimf(rain_chance.universe, [0, 0, 30])  # Niska szansa na deszcz: 0-30%
rain_chance['medium'] = fuzz.trimf(rain_chance.universe, [20, 50, 80])  # Średnia szansa na deszcz: 20-80%
rain_chance['high'] = fuzz.trimf(rain_chance.universe, [70, 100, 100])  # Wysoka szansa na deszcz: 70-100%

# Funkcje przynależności dla możliwości żeglowania
sailing['poor'] = fuzz.trimf(sailing.universe, [0, 0, 40])  # Słabe warunki do żeglowania: 0-40%
sailing['good'] = fuzz.trimf(sailing.universe, [30, 60, 100])  # Dobre warunki do żeglowania: 30-100%

# Tworzenie reguł rozmytych opisujących zależności między warunkami a żeglowaniem
rule1 = ctrl.Rule(wind_speed['high'] & rain_chance['low'], sailing['good'])
rule2 = ctrl.Rule(wind_speed['medium'] & rain_chance['low'], sailing['good'])
rule3 = ctrl.Rule(wind_speed['low'] | rain_chance['high'], sailing['poor'])

# Inicjalizacja systemu sterowania opartego na zdefiniowanych regułach
sailing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
sailing_simulation = ctrl.ControlSystemSimulation(sailing_ctrl)

# Ustawienie danych wejściowych dla symulacji
sailing_simulation.input['wind_speed'] = 20  # Prędkość wiatru wynosi 20 km/h
sailing_simulation.input['rain_chance'] = 80  # Szansa na deszcz wynosi 80%

# Wykonywanie obliczeń systemu rozmytego
sailing_simulation.compute()

# Wyświetlenie wyniku: procentowa ocena możliwości żeglowania
print(f"Możliwość żeglowania: {sailing_simulation.output['sailing']}%")
