# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

ksiazki = []
czytacze = []
historia = []

status_wypozyczona = 'Nie w bibliotece'
status_dostepna = 'W bibliotece'

naglowek_biblioteka = "ID, Tytul, Autor, Rok wydania, Status"
naglowek_historia = "ID, Numer czytacza, Czy udana, Data wypozyczenia, Data oddania"
naglowek_czytacze = "Numer czytacza, Imie, Nazwisko, Ilosc ksiazek"

class Ksiazka:
    def __init__(self, id, tytul, autor, rok_wydania, status=status_dostepna):
        self.id = id
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.status = status
    
    def __str__(self):
        return f"{self.id},{self.tytul},{self.autor},{self.rok_wydania},{self.status}"
        
    def wprowadz(self):
        self.id = len(ksiazki)
        self.tytul = wprowadz_wartosc("Podaj tytul ksiazki: ")
        self.autor = wprowadz_wartosc("Podaj autora ksiazki: ")
        self.rok_wydania = input("Podaj rok wydania książki: ")
        self.status = status_dostepna

class Czytacz:
    def __init__(self, id, imie, nazwisko, ilosc_ksiazek=0):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.ilosc_ksiazek = ilosc_ksiazek
    
    def __str__(self):
        return f"{self.id},{self.imie},{self.nazwisko},{self.ilosc_ksiazek}"
        
class Wypozyczenie:
    def __init__(self, id, numer_czytacza, czy_udane, data_wyp, data_odd):
        self.id = id
        self.numer_czytacza = numer_czytacza
        self.czy_udane = czy_udane
        self.data_wyp = data_wyp
        self.data_odd = data_odd

    def __str__(self):
        return f"{self.id},{self.numer_czytacza},{self.czy_udane},{self.data_wyp},{self.data_odd}"
      
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
        print("4. historia ksiazki\n5. zakoncz\n")
        
    def obsluz_opcje(self):
        opcja = input("Wybrana opcja: ")
        while True:
            match opcja:
                case '1':
                    self.dodaj_ksiazke()
                case '2':
                    self.wypozycz_ksiazke()
                case '3':
                    self.oddaj_ksiazke()
                case '4':
                    self.historia_ksiazki()
                case '5':
                    self.zapisz_dane()
                    return
                case _:
                    print(f"\n==== Opcja {opcja} niedostepna! ====\n")
            opcja = input("Wybrana opcja: ")
            
    def zacznij_prace(self):
        self.asystent_plikow.sprawdz_pliki()
        self.wypisz_poczatkowe_info()
        self.obsluz_opcje()
        
    def dodaj_ksiazke(self):
        nowa_ksiazka = Ksiazka("", "", "", "", "")
        nowa_ksiazka.wprowadz()
        ksiazki.append(nowa_ksiazka)
        print(f"\n==== Wprowadzono ksiazke {nowa_ksiazka}! ====")
        wyswietl_kolekcje(ksiazki, 'Ksiazki')
    
    def wypozycz_ksiazke(self):
        numer = int(input("Podaj nr ksiazki: "))
        nr_czytacza = int(input("Podaj nr czytacza: "))
        imie = input("Podaj imie czytacza: ")
        nazwisko = input("Podaj nazwisko czytacza: ")

        for k in ksiazki:
            if k.id == numer:
                if k.status != status_wypozyczona:
                    k.status = status_wypozyczona
                    dodaj_ksiazke_czytacza(nr_czytacza, imie, nazwisko)
                else:
                    print('Wypozyczenie niemozliwe, ksiazka jest juz wypozyczona!')
        wyswietl_kolekcje(ksiazki, 'Ksiazki')
        wyswietl_kolekcje(czytacze, 'Czytacze')

    def oddaj_ksiazke(self):
        numer = int(input("Podaj nr ksiazki: "))
        print(len([k for k in ksiazki if k.id==numer]))
    
    def historia_ksiazki(self):
        print(f"\n==== Historia ksiazki jeszcze nie jest zaimplementowana ====")
        
    def zapisz_dane(self):
        print(f"\n==== Zapisywanie jeszcze nie jest zaimplementowana ====")

def wyswietl_kolekcje(kolekcja, nazwa):
    print(f"==== {nazwa} ====")
    for element in kolekcja:
        print(element)
    print("===========\n")
        
def zmien_ksiazki_czytacza(numer, zmiana):
    for cz in czytacze:
        if cz.id == numer:
            cz.ilosc_ksiazek += zmiana
            return
        
def dodaj_ksiazke_czytacza(numer_czytacza, imie, nazwisko):
    istnieje_z_id = any(cz.id == numer_czytacza for cz in czytacze)
    if istnieje_z_id:
        zmien_ksiazki_czytacza(numer_czytacza, 1)
    else:
        czytacze.append(Czytacz(numer_czytacza, imie, nazwisko, 1))

def wyswietl_wszystkie_kolekcje():
    wyswietl_kolekcje(ksiazki, 'Ksiazki')
    wyswietl_kolekcje(czytacze, 'Czytacze')
    wyswietl_kolekcje(historia, 'Wypozyczenia')
    
def wprowadz_wartosc(komunikat):
    while True:
        wartosc = input(komunikat)
        if not sprawdz_polskie_znaki(wartosc):
            return wartosc
        else:
            print("Wprowadzono tekst z polskimi znakami, ktore nie sa dozwolone. Prosze sprobowac ponownie.")

def sprawdz_polskie_znaki(tekst):
    polskie_znaki = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
    for znak in polskie_znaki:
        if znak in tekst:
            return True
    return False

wyswietl_kolekcje(ksiazki, 'Ksiazki')
ksiazki.append(Ksiazka(0, "T1", "A1", 2021))
wyswietl_kolekcje(ksiazki, 'Ksiazki')
czytacze.append(Czytacz(0, "I1", "N1"))
czytacze.append(Czytacz(1, "I2", "N1"))
zmien_ksiazki_czytacza(1, -1)
wyswietl_kolekcje(czytacze, 'Czytacze')
historia.append(Wypozyczenie(1, 1, "tak", 21-2-2002, 22-2-2002))
wyswietl_kolekcje(historia, 'Historia')

wyswietl_wszystkie_kolekcje()

asystent = AsystentPlikow()
biblioteka = Biblioteka(asystent)
biblioteka.zacznij_prace()
