biblioteka = []
historia = []
czytacze = []

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
    tytul_lub_numer = input("Tytuł lub numer indeksu ksiazki: ")
    numer_czytacza = input("Numer czytacza: ")
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    data = input("Data: ")
    # dodaj czytacza
    czytacz = (numer_czytacza, imie, nazwisko, 1)
    # lub inkrementuj liczbe jego ksiazek
    
def szukaj_ksiazki(tytul):
    znalezione = [ksiazka for ksiazka in biblioteka if ksiazka[0] == tytul]
    print(f"Ksiazka znaleziona: {znalezione}")
    
def zacznij_prace_bibliotekarki():
    opcja = input("Wybrana opcja: ")
    while opcja != '5':
        match opcja:
            case '1':
                dodaj_ksiazke()
            case '2':
                wypozycz_ksiazke()
            case '13':
                szukaj_ksiazki(input("Szukaj tytulu: "))
        opcja = input("Wybrana opcja: ")

wypisz_poczatkowe_info()
zacznij_prace_bibliotekarki()
