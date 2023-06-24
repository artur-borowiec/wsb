# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from datetime import datetime

KSIAZKI = []
KSIAZKI_NAZWA_PLIKU = 'biblioteka'
CZYTACZE = []
CZYTACZE_NAZWA_PLIKU = 'czytacze'
HISTORIA = []
HISTORIA_NAZWA_PLIKU = 'historia'

STATUS_WYPOZYCZONA = 'Nie w bibliotece'
STATUS_DOSTEPNA = 'W bibliotece'

NAGLOWEK_BIBLIOTEKA = "ID, Tytul, Autor, Rok wydania, Status\n"
NAGLOWEK_HISTORIA = "ID, Numer czytacza, Czy udana, Typ Akcji, Data\n"
NAGLOWEK_CZYTACZE = "Numer czytacza, Imie, Nazwisko, Ilosc ksiazek\n"

UDANE = 'Tak'
NIE_UDANE = 'Nie'
WYPOZYCZENIE_AKCJA = 'Wypozyczenie'
ODDANIE_AKCJA = 'Oddanie'
HISTORIA_AKCJA = 'Historia'


class Ksiazka:
    def __init__(self, id, tytul, autor, rok_wydania, status=STATUS_DOSTEPNA):
        self.id = id
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.status = status

    def __str__(self):
        return f"{self.id},{self.tytul},{self.autor},{self.rok_wydania},{self.status}"

    def wprowadz(self):
        self.id = len(KSIAZKI)
        self.tytul = wprowadz_wartosc("Podaj tytul KSIAZKI: ")
        self.autor = wprowadz_wartosc("Podaj autora KSIAZKI: ")
        self.rok_wydania = input("Podaj rok wydania książki: ")
        self.status = STATUS_DOSTEPNA


class Czytacz:
    def __init__(self, id, imie, nazwisko, ilosc_ksiazek=0):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.ilosc_ksiazek = int(ilosc_ksiazek)

    def __str__(self):
        return f"{self.id},{self.imie},{self.nazwisko},{self.ilosc_ksiazek}"


class Wypozyczenie:
    def __init__(self, id_ksiazki, numer_czytacza, czy_udane, typ_akcji, data=None):
        self.id = id_ksiazki
        self.numer_czytacza = numer_czytacza
        self.czy_udane = czy_udane
        self.data = data
        self.typ_akcji = typ_akcji

    def __str__(self):
        return f"{self.id},{self.numer_czytacza},{self.czy_udane},{self.typ_akcji},{self.data}"

    def ustaw_czas_na_teraz(self):
        self.data = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")


class AsystentPlikow:
    def __init__(self):
        pass

    def _wczytaj(self, nazwa_pliku, zbior_danych, typ, typ_str):
        with open(f'{nazwa_pliku}.csv', 'r') as plik:
            lines = plik.readlines()
            if (len(lines) > 1):
                lines.pop(0)
                for line in lines:
                    zbior_danych.append(typ(*line.strip().split(',')))
                print(f"\nWczytano {len(lines)} {typ_str}!")
            else:
                print(f"\nBrak {typ_str} do wczytania!")

    def wczytaj_ksiazki(self):
        self._wczytaj(KSIAZKI_NAZWA_PLIKU, KSIAZKI, Ksiazka, 'ksiazek')

    def wczytaj_czytaczy(self):
        self._wczytaj(CZYTACZE_NAZWA_PLIKU, CZYTACZE, Czytacz, 'czytaczy')

    def wczytaj_historia(self):
        self._wczytaj(HISTORIA_NAZWA_PLIKU, HISTORIA, Wypozyczenie, 'wypozyczen')

    def __utworz_plik__(self, nazwa, f_wczytaj):
        try:
            open(f"{nazwa}", "x")
            print(f"\nUtworzono plik {nazwa}")
        except:
            print(f"\n{nazwa} juz istnieje, pomijam tworzenie")
            f_wczytaj()

    def sprawdz_pliki(self):
        self.__utworz_plik__(f"{KSIAZKI_NAZWA_PLIKU}.csv", self.wczytaj_ksiazki)
        self.__utworz_plik__(f"{HISTORIA_NAZWA_PLIKU}.csv", self.wczytaj_historia)
        self.__utworz_plik__(f"{CZYTACZE_NAZWA_PLIKU}.csv", self.wczytaj_czytaczy)

    def _zapisz(self, nazwa_pliku, naglowek, zbior_danych):
        with open(f'{nazwa_pliku}.csv', 'w') as plik:
            plik.write(naglowek)
            for dane in zbior_danych:
                plik.write(f"{dane}\n")

    def _zapisz_czytacze(self):
        self._zapisz(CZYTACZE_NAZWA_PLIKU, NAGLOWEK_CZYTACZE, CZYTACZE)

    def _zapisz_historia(self):
        self._zapisz(HISTORIA_NAZWA_PLIKU, NAGLOWEK_HISTORIA, HISTORIA)

    def _zapisz_biblioteka(self):
        self._zapisz(KSIAZKI_NAZWA_PLIKU, NAGLOWEK_BIBLIOTEKA, KSIAZKI)

    def zapisz_dane(self):
        self._zapisz_czytacze()
        self._zapisz_historia()
        self._zapisz_biblioteka()


class Biblioteka:
    def __init__(self, asystent_plikow):
        self.asystent_plikow = asystent_plikow
        self._powitalne_info = "\nWitaj w bibliotece miejskiej w Sosnowcu!\n"
        self._opcja1 = "1. dodaj ksiazke"
        self._opcja2 = "2. wypozycz ksiazke"
        self._opcja3 = "3. oddaj ksiazke"
        self._opcja4 = "4. historia ksiazki"
        self._opcja5 = "5. zakoncz"

    def wypisz_poczatkowe_info(self):
        print(self._powitalne_info)
        self.wypisz_dostepne_opcje()

    def wypisz_dostepne_opcje(self):
        print("\nWybierz opcje:")

        opcje = [self._opcja1,
                 self._opcja2,
                 self._opcja3,
                 self._opcja4,
                 self._opcja5]

        print("\n".join(opcje))

    def obsluz_opcje(self):
        opcja = input("\nWybrana opcja: ")

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
                    self.asystent_plikow.zapisz_dane()
                    return
                case _:
                    print(f"\n==== Opcja {opcja} niedostepna! ====\n")

            self.wypisz_dostepne_opcje()
            opcja = input("\nWybrana opcja: ")

    def zacznij_prace(self):
        self.asystent_plikow.sprawdz_pliki()
        self.wypisz_poczatkowe_info()
        try:
            self.obsluz_opcje()
        except Exception as e:
            print(e)
            print("=" * 20)
            print(
                "\n[BLAD]  Podaj poprawne dane dla opcji, jeżeli opcja wymaga numeru podaj liczbę a nie litery / slowa\n\n")
            print("=" * 20)

    def dodaj_ksiazke(self):
        nowa_ksiazka = Ksiazka("", "", "", "", "")
        nowa_ksiazka.wprowadz()
        KSIAZKI.append(nowa_ksiazka)
        print(f"\n==== Wprowadzono ksiazke {nowa_ksiazka}! ====")
        wyswietl_kolekcje(KSIAZKI, 'Ksiazki', NAGLOWEK_BIBLIOTEKA)

    def _czy_ksiazka_istnieje(self, id_ksiazki):
        return any(int(k.id) == id_ksiazki for k in KSIAZKI)

    def _znajdz_ksiazke(self, id_ksiazki):
        for k in KSIAZKI:
            # ToDo: dodać `or` żeby szukało np po tytule
            if int(k.id) == id_ksiazki:
                return k
        return None

    def _znajdz_ksiazke_o_statusie(self, id_ksiazki, status):
        ksiazka = self._znajdz_ksiazke(id_ksiazki)

        if ksiazka and ksiazka.status == status:
            return ksiazka

        return None

    def _znajdz_wolna_ksiazke(self, id_ksiazki):
        return self._znajdz_ksiazke_o_statusie(id_ksiazki, STATUS_DOSTEPNA)

    def _znajdz_wynajeta_ksiazke(self, id_ksiazki):
        return self._znajdz_ksiazke_o_statusie(id_ksiazki, STATUS_WYPOZYCZONA)

    def wypozycz_ksiazke(self):
        wyswietl_kolekcje(KSIAZKI, 'Ksiazki', NAGLOWEK_BIBLIOTEKA)
        numer = int(input("Podaj nr KSIAZKI: "))

        if not self._czy_ksiazka_istnieje(numer):
            dodaj_historie(numer, '', NIE_UDANE, WYPOZYCZENIE_AKCJA)
            return print("\nNie znaleziono ksiazki !!!!")

        wyswietl_kolekcje(CZYTACZE, 'Czytacze', NAGLOWEK_CZYTACZE)

        ksiazka = self._znajdz_wolna_ksiazke(numer)

        if ksiazka:
            ksiazka.status = STATUS_WYPOZYCZONA
        else:
            dodaj_historie(numer, '', NIE_UDANE, WYPOZYCZENIE_AKCJA)
            return print("\n[BLAD] Ksiazka wypożyczona")

        nr_czytacza = int(input("Podaj nr czytacza: "))
        imie = input("Podaj imie czytacza: ")
        nazwisko = input("Podaj nazwisko czytacza: ")

        dodaj_ksiazke_czytacza(nr_czytacza, imie, nazwisko)
        dodaj_historie(numer, nr_czytacza, UDANE, WYPOZYCZENIE_AKCJA)

        print("=" * 20)
        print("Akcja wypozyczenia ksiązki się powiodła")
        print("=" * 20)
        print("\n Zakutalizowana biblioteka")
        wyswietl_kolekcje(KSIAZKI, 'Ksiazki', NAGLOWEK_BIBLIOTEKA)
        print("\n Zakutalizowani Czytacze")
        wyswietl_kolekcje(CZYTACZE, 'Czytacze', NAGLOWEK_CZYTACZE)

    def oddaj_ksiazke(self):
        wyswietl_kolekcje(KSIAZKI, 'Ksiazki', NAGLOWEK_BIBLIOTEKA)
        numer = int(input("Podaj nr KSIAZKI: "))

        if not self._czy_ksiazka_istnieje(numer):
            dodaj_historie(numer, '', NIE_UDANE, ODDANIE_AKCJA)
            return print("\nNie znaleziono ksiazki !!!!")

        ksiazka = self._znajdz_wynajeta_ksiazke(numer)

        wyswietl_kolekcje(CZYTACZE, 'Czytacze', NAGLOWEK_CZYTACZE)
        nr_czytacza = int(input("Podaj nr czytacza: "))

        if not any(int(cz.id) == nr_czytacza for cz in CZYTACZE):
            dodaj_historie(numer, nr_czytacza, NIE_UDANE, ODDANIE_AKCJA)
            return print("\nNie znaleziono czytacza")

        if ksiazka:
            ksiazka.status = STATUS_DOSTEPNA
        else:
            dodaj_historie(numer, nr_czytacza, NIE_UDANE, ODDANIE_AKCJA)
            return print("\n[BLAD] Ksiazka już oddana")

        odejmij_ksiazke_czytacza(nr_czytacza)
        dodaj_historie(numer, nr_czytacza, UDANE, ODDANIE_AKCJA)

        print("=" * 20)
        print("Akcja oddania ksiązki się powiodła")
        print("=" * 20)
        print("\n Zakutalizowana biblioteka")
        wyswietl_kolekcje(KSIAZKI, 'Ksiazki', NAGLOWEK_BIBLIOTEKA)
        print("\n Zakutalizowani Czytacze")
        wyswietl_kolekcje(CZYTACZE, 'Czytacze', NAGLOWEK_CZYTACZE)

    def historia_ksiazki(self):
        wyswietl_kolekcje(KSIAZKI, 'Ksiazki', NAGLOWEK_BIBLIOTEKA)
        numer = int(input("Podaj nr KSIAZKI: "))

        if not self._czy_ksiazka_istnieje(numer):
            dodaj_historie(numer, '', NIE_UDANE, HISTORIA)
            return print("\nNie znaleziono ksiazki !!!!")

        for h in HISTORIA:
            if int(int(h.id_ksiazki)) == numer:
                print(f"\n{str(h)}")


def wyswietl_kolekcje(kolekcja, nazwa, kolumny):
    print(f"==== {nazwa} ====")
    print(kolumny)
    for element in kolekcja:
        print(element)
    print("===========\n")


def zmien_ksiazki_czytacza(numer, zmiana, dodaj=True):
    for cz in CZYTACZE:
        if int(cz.id) == int(numer):
            if dodaj:
                cz.ilosc_ksiazek += zmiana
            elif int(cz.ilosc_ksiazek) > 0:
                cz.ilosc_ksiazek -= zmiana

            print(f"\n Liczba {cz.ilosc_ksiazek} ksiązek Czytacza {cz.imie} po zmiane.")
            return


def dodaj_ksiazke_czytacza(numer_czytacza, imie, nazwisko):
    istnieje_z_id = any(int(cz.id) == numer_czytacza for cz in CZYTACZE)
    if istnieje_z_id:
        zmien_ksiazki_czytacza(numer_czytacza, 1)
        print(f"\n Dodano kolejna ksiazke dla czytacza z ID {numer_czytacza}")
    else:
        czytacz = Czytacz(numer_czytacza, imie, nazwisko, 1)
        CZYTACZE.append(czytacz)
        print(f"\n Dodano 1 ksiazke dla czytacza {czytacz.imie} {czytacz.nazwisko}")


def odejmij_ksiazke_czytacza(numer_czytacza):
    istnieje_z_id = any(int(cz.id) == numer_czytacza for cz in CZYTACZE)
    if istnieje_z_id:
        zmien_ksiazki_czytacza(numer_czytacza, 1, False)
        print(f"\n Odjeto kolejna ksiazke dla czytacza z ID {numer_czytacza}")


def dodaj_historie(id_ksiazki, numer_czytacza, czy_udane, typ_akcji):
    try:
        id_ksiazki = int(id_ksiazki)
    except:
        return

    wypozyczenie = Wypozyczenie(id_ksiazki, numer_czytacza, czy_udane, typ_akcji)
    wypozyczenie.ustaw_czas_na_teraz()
    HISTORIA.append(wypozyczenie)


def wyswietl_wszystkie_kolekcje():
    wyswietl_kolekcje(KSIAZKI, 'Ksiazki', NAGLOWEK_BIBLIOTEKA)
    wyswietl_kolekcje(CZYTACZE, 'Czytacze', NAGLOWEK_CZYTACZE)
    wyswietl_kolekcje(HISTORIA, 'Wypozyczenia', NAGLOWEK_HISTORIA)


def wprowadz_wartosc(komunikat):
    while True:
        wartosc = input(komunikat)
        if not sprawdz_polskie_znaki(wartosc):
            return wartosc
        else:
            print("[BLAD] Wprowadzono tekst z polskimi znakami, ktore nie sa dozwolone. Prosze sprobowac ponownie.")


def sprawdz_polskie_znaki(tekst):
    polskie_znaki = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
    return any(znak in tekst for znak in polskie_znaki)


asystent = AsystentPlikow()
biblioteka = Biblioteka(asystent)
biblioteka.zacznij_prace()
wyswietl_wszystkie_kolekcje()
