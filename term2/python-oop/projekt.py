# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Witaj w bibliotece miejskiej w Sosnowcu!\n")
print("Wybierz opcje:\n1. dodaj ksiazke")
print("2. wypozycz ksiazke\n3. oddaj ksiazke")
print("4. historia ksiazki\n5. zakoncz")

ksiazki = []

def dodaj_ksiazke():
    tytul = input("Tytul ksiazki: ")
    autor = input("Autor ksiazki: ")
    rok_wydania = input("Rok wydania: ")
    ksiazki.append((tytul, autor, rok_wydania))
    print(ksiazki)

opcja = input("Wybrana opcja: ")

while opcja != '5':
    match opcja:
        case '1':
            dodaj_ksiazke()
    opcja = input("Wybrana opcja: ")
