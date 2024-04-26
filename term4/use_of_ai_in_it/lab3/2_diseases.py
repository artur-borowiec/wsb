def suggest_diseases(temperature, crp_level, leukocyte_count, glucose_level, blood_pressure, pain_presence):
    diseases = []

    # Sprawdzenie możliwości grypy
    if temperature > 38 and crp_level < 10 and 4 <= leukocyte_count <= 11 and not pain_presence:
        diseases.append("Grypa")

    # Sprawdzenie możliwości zakażenia bakteryjnego
    if temperature > 38 and crp_level > 20 and leukocyte_count > 11 and not pain_presence:
        diseases.append("Zakażenie bakteryjne")

    # Sprawdzenie możliwości anemii
    if temperature <= 37 and leukocyte_count < 4:
        diseases.append("Anemia")

    # Sprawdzenie możliwości cukrzycy
    if glucose_level > 126:
        diseases.append("Cukrzyca")

    # Sprawdzenie możliwości nadciśnienia
    systolic, diastolic = map(int, blood_pressure.split('/'))
    if systolic > 140 or diastolic > 90:
        diseases.append("Nadciśnienie")

    # Sprawdzenie możliwości zapalenia płuc
    if temperature > 38 and crp_level > 20 and pain_presence:
        diseases.append("Zapalenie płuc")

    return diseases if diseases else ["Brak sugerowanych chorób na podstawie podanych wyników."]


# Zbieranie danych wejściowych od użytkownika
temperature = float(input("Podaj temperaturę pacjenta (°C): "))
crp_level = float(input("Podaj poziom białka CRP (mg/L): "))
leukocyte_count = float(input("Podaj liczbę leukocytów (w tys./µl): "))
glucose_level = float(input("Podaj poziom glukozy (mg/dL): "))
blood_pressure = input("Podaj ciśnienie krwi (mmHg, format systolic/diastolic): ")
pain_presence = input("Czy pacjent odczuwa ból? (tak/nie): ") == "tak"

# Sugerowanie możliwych chorób
suggested_diseases = suggest_diseases(temperature, crp_level, leukocyte_count, glucose_level, blood_pressure,
                                      pain_presence)
print("Sugerowane choroby: ", ", ".join(suggested_diseases))
