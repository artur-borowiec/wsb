biblioteka = []

def wypisz_poczatkowe_info():
    print("Witaj w bibliotece miejskiej w Sosnowcu!\n")
    print("Wybierz opcje:\n1. dodaj ksiazke")
    print("2. wypozycz ksiazke\n3. oddaj ksiazke")
    print("4. historia ksiazki\n5. zakoncz")

def dodaj_ksiazke():
    tytul = input("Tytul ksiazki: ")
    autor = input("Autor ksiazki: ")
    rok_wydania = input("Rok wydania: ")
    ksiazka = (tytul, autor, rok_wydania, 'w bibliotece')
    biblioteka.append(ksiazka)
    print(f"Dodano ksiazke {ksiazka}")
    print(f"Stan biblioteki: {biblioteka}")

def wypozycz_ksiazke():
    print('')
    
def zacznij_prace_bibliotekarki():
    opcja = input("Wybrana opcja: ")
    while opcja != '5':
        match opcja:
            case '1':
                dodaj_ksiazke()
            case '2':
                wypozycz_ksiazke()
        opcja = input("Wybrana opcja: ")

wypisz_poczatkowe_info()
zacznij_prace_bibliotekarki()
