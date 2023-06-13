import random

biblioteka = []
historia = []
czytacze = []

def wypisz_poczatkowe_info():
    print("Witaj w bibliotece miejskiej w Sosnowcu!\n")
    print("Wybierz opcje:\n1. dodaj ksiazke")
    print("2. wypozycz ksiazke\n3. oddaj ksiazke")
    print("4. historia ksiazki\n5. zakoncz")

def dodaj_ksiazke():
    #TODO: zmienic na najmniejszy dostepny
    numer = random.randint(0,9999)
    tytul = input("Tytul ksiazki: ")
    autor = input("Autor ksiazki: ")
    rok_wydania = input("Rok wydania: ")
    
    ksiazka = (numer, tytul, autor, rok_wydania, 'w bibliotece')
    biblioteka.append(ksiazka)
    print(f"Dodano ksiazke {ksiazka}")
    print(f"Stan biblioteki: {biblioteka}")

def dodaj_czytacza(czytacz):
    czytacze.append(czytacz)
    print(f"Czytacze: {czytacze}")

def zwieksz_ksiazki_czytacza(numer):
    numery = [czytacz[0] for czytacz in czytacze]
    index = numery.index(numer)
    czytacz = czytacze[index]
    czytacze[index] = (czytacz[0], czytacz[1], czytacz[2], 1+czytacz[3])
    print(f"Czytacze: {czytacze}")
    
def wypozycz_ksiazke():
    tytul_lub_numer = input("Tytuł lub numer indeksu ksiazki: ")
    numer_czytacza = input("Numer czytacza: ")
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    #data = input("Data: ")
    czy_ksiazka_dostepna(tytul_lub_numer)
    czy_istnieje = czy_czytacz_istnieje(numer_czytacza, imie, nazwisko)
    
    if not czy_istnieje:
        dodaj_czytacza((numer_czytacza, imie, nazwisko, 1))
    else:
        zwieksz_ksiazki_czytacza(numer_czytacza)

def czy_ksiazka_dostepna(tytul_lub_numer):
    try:
        numer = int(tytul_lub_numer)
        numery = [ksiazka[0] for ksiazka in biblioteka]
        print(f"Numer istnieje? {numer in numery}")
    except ValueError:
        tytuly = [ksiazka[1] for ksiazka in biblioteka]
        print(f"Tytul istnieje? {tytul_lub_numer in tytuly}")

def czy_czytacz_istnieje(numer, imie, nazwisko):
    numery = [czytacz[0] for czytacz in czytacze]
    imiona_nazwiska = [(czytacz[1], czytacz[2]) for czytacz in czytacze]
    print(f"Czytacz z numerem istnieje? {numer in numery}")
    print(f"Czytacz z imieniem/nazwiskiem istnieje? {(imie, nazwisko) in imiona_nazwiska}")
    return (numer in numery) or ((imie, nazwisko) in imiona_nazwiska)
    
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
