# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

ksiazki = []
czytacze = []
historia = []

class Ksiazka:
    def __init__(self, id, tytul, autor, rok_wydania, status='W bibliotece'):
        self.id = id
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.status = status
    
    def __str__(self):
        return f"{self.id},{self.tytul},{self.autor},{self.rok_wydania},{self.status}"

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
        print("4. historia ksiazki\n5. zakoncz")
        
    def zacznij_prace(self):
        self.asystent_plikow.sprawdz_pliki()
        self.wypisz_poczatkowe_info()
        
def wyswietl_kolekcje(kolekcja, nazwa):
    print(f"==== {nazwa} ====")
    for element in kolekcja:
        print(element)
        
def zmien_ksiazki_czytacza(numer, zmiana):
    for cz in czytacze:
        if cz.id == numer:
            cz.ilosc_ksiazek += zmiana

def wyswietl_wszystkie_kolekcje():
    wyswietl_kolekcje(ksiazki, 'Ksiazki')
    wyswietl_kolekcje(czytacze, 'Czytacze')
    wyswietl_kolekcje(historia, 'Wypozyczenia')

wyswietl_kolekcje(ksiazki, 'Ksiazki')
ksiazki.append(Ksiazka(1, "T1", "A1", 2021))
wyswietl_kolekcje(ksiazki, 'Ksiazki')
czytacze.append(Czytacz(1, "I1", "N1"))
czytacze.append(Czytacz(2, "I2", "N1"))
zmien_ksiazki_czytacza(2, -1)
wyswietl_kolekcje(czytacze, 'Czytacze')
historia.append(Wypozyczenie(1, 1, "tak", 21-2-2002, 22-2-2002))
wyswietl_kolekcje(historia, 'Historia')

wyswietl_wszystkie_kolekcje()

asystent = AsystentPlikow()
biblioteka = Biblioteka(asystent)
biblioteka.zacznij_prace()
