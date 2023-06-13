import random

biblioteka = []
historia = []
czytacze = []

def dodaj_ksiazke():
    numer = len(biblioteka)
    tytul = input("Tytul ksiazki: ")
    autor = input("Autor ksiazki: ")
    rok_wydania = input("Rok wydania: ")
    
    ksiazka = (numer, tytul, autor, rok_wydania, 'W bibliotece')
    biblioteka.append(ksiazka)
    print(f"Dodano ksiazke {ksiazka}")
    bstr = str(biblioteka).replace('), (', '),\n(').replace('[', '[\n').replace(']', '\n]')
    print(f"Stan biblioteki: {bstr}")

def dodaj_czytacza(czytacz):
    czytacze.append(czytacz)
    print(f"Czytacze: {czytacze}")
    
def wypozycz_ksiazke():
    tytul_lub_numer = input("Tytuł lub numer indeksu ksiazki: ")
    numer_czytacza = input("Numer czytacza: ")
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    #data = input("Data: ")
    pozycja = pozycja_ksiazki(tytul_lub_numer)
    if pozycja == -1:
        obsluz_bledne_wypozyczenie(None)
        return
    
    ksiazka = biblioteka[pozycja]
    if (ksiazka[4] == 'Nie w bibliotece'):
        obsluz_bledne_wypozyczenie(ksiazka)
        return
        
    biblioteka[pozycja] = (ksiazka[0], ksiazka[1], ksiazka[2], ksiazka[3], 'Nie w bibliotece')
    czy_istnieje = czy_czytacz_istnieje(numer_czytacza, imie, nazwisko)
    
    if not czy_istnieje:
        dodaj_czytacza((numer_czytacza, imie, nazwisko, 1))
    else:
        zwieksz_ksiazki_czytacza(numer_czytacza)

def obsluz_bledne_wypozyczenie(ksiazka):
    if ksiazka == None:
        print("Brak ksiazki")
    else:
        print("Ksiazka juz wypozyczona")

def pozycja_ksiazki(tytul_lub_numer):
    try:
        numer = int(tytul_lub_numer)
        numery = [ksiazka[0] for ksiazka in biblioteka]
        return numery.index(numer) if numer in numery else -1
    except ValueError:
        tytul = tytul_lub_numer
        tytuly = [ksiazka[1] for ksiazka in biblioteka]
        return tytuly.index(tytul_lub_numer) if tytul in tytuly else -1
        
def zwieksz_ksiazki_czytacza(numer):
    numery = [czytacz[0] for czytacz in czytacze]
    index = numery.index(numer)
    czytacz = czytacze[index]
    czytacze[index] = (czytacz[0], czytacz[1], czytacz[2], 1+czytacz[3])
    print(f"Czytacze: {czytacze}")

def czy_czytacz_istnieje(numer, imie, nazwisko):
    numery = [czytacz[0] for czytacz in czytacze]
    imiona_nazwiska = [(czytacz[1], czytacz[2]) for czytacz in czytacze]
    print(f"Czytacz z numerem istnieje? {numer in numery}")
    print(f"Czytacz z imieniem/nazwiskiem istnieje? {(imie, nazwisko) in imiona_nazwiska}")
    return (numer in numery) or ((imie, nazwisko) in imiona_nazwiska)

class AsystentPlikow:
    def __init__(self):
        pass
        
    def __utworz_plik__(self, nazwa):
        try:
            open(f"{nazwa}", "x")
            print(f"Utworzono plik {nazwa}")
        except:
            print(f"{nazwa} juz istnieje, pomijam tworzenie")
    
    def sprawdz_pliki(self):
        self.__utworz_plik__("biblioteka.csv")
        self.__utworz_plik__("historia.csv")
        self.__utworz_plik__("czytacze.csv")
        
class Biblioteka:
    def __init__(self, asystent_plikow):
        self.asystent_plikow = asystent_plikow
    
    def wypisz_poczatkowe_info(self):
        print("Witaj w bibliotece miejskiej w Sosnowcu!\n")
        print("Wybierz opcje:\n1. dodaj ksiazke")
        print("2. wypozycz ksiazke\n3. oddaj ksiazke")
        print("4. historia ksiazki\n5. zakoncz")
        
    def zacznij_prace(self):
        self.asystent_plikow.sprawdz_pliki()
        self.wypisz_poczatkowe_info()
        opcja = input("Wybrana opcja: ")
        while opcja != '5':
            match opcja:
                case '1':
                    dodaj_ksiazke()
                case '2':
                    wypozycz_ksiazke()
            opcja = input("Wybrana opcja: ")

asystent = AsystentPlikow()
Biblioteka(asystent).zacznij_prace()
