import datetime
from abc import abstractmethod

class Animal:
    def __init__(self, name, birth_year, is_alive, weight):
        self.name = name
        self.birth_year = birth_year
        self.is_alive = is_alive
        self.weight = weight
    
    def rename(self, new_name):
        self.name = new_name
        
    def print_age(self):
        today = datetime.date.today()
        print(f"{self.name}'s age: {today.year-self.birth_year}")
        
    @abstractmethod
    def print_data(self):
        pass
    
    @abstractmethod
    def change_weight(self, weight):
        pass
        
class Human(Animal):
    def __init__(self, name, surname, birth_year, profession, is_alive, weight, height):
        super(Human, self).__init__(name, birth_year, is_alive, weight)
        self.surname = surname
        self.profession = profession
        self.height = height

    def print_full_name(self):
        print(f"{self.name} {self.surname}")
        
    def print_data(self):
        print(f"{self.name} {self.surname} was born in {self.birth_year}. ")
        print(f"He/she works as {self.profession}") if self.is_alive else print("R.I.P.")
        
    def change_job(self, new_job):
        self.profession = new_job
        
    def print_bmi(self):
        print(self.__calculate_bmi())
    
    def __calculate_bmi(self):
        bmi = self.weight / (self.height/100)**2
        if bmi <= 18.4:
            return "Niedowaga"
        elif bmi <= 24.9:
            return "Waga prawidlowa"
        else:
            return "Nadwaga"
    
    def change_weight(self, weight):
        if (weight > 300):
            print ("Nieprawidlowa waga")
        else:
            self.weight = weight
    
h1 = Human("John", "Blake", 1997, "accountant", True, 70, 180)
h1.print_full_name()
h1.print_data()
h1.print_age()
h1.change_job("programmer")
h1.print_data()
h1.print_bmi()

class Cat(Animal):
    def __init__(self, name, breed, birth_year, is_alive, weight):
        super(Cat, self).__init__(name, birth_year, is_alive, weight)
        self.breed = breed

    def print_name(self):
        print(f"{self.name}, meow!" if self.is_alive else "<silence>")
        
    def print_data(self):
        print(f"{self.name}, {self.breed} born in {self.birth_year}")
        
    def toggle_alive(self):
        self.is_alive = not self.is_alive
        
    def change_age(self, age):
        today = datetime.date.today()
        self.birth_year = today.year-age
        
    def change_weight(self, weight):
        if (weight > 30):
            print ("Nieprawidlowa waga kota")
        else:
            self.weight = weight
            
class Dog(Animal):
    def __init__(self, name, breed, birth_year, is_alive, weight, bark_sound):
        super(Dog, self).__init__(name, birth_year, is_alive, weight)
        self.breed = breed
        self.bark_sound = bark_sound
    
    def bark(self):
        print(f"{self.bark_sound}!")

cat = Cat("Shadow", "Abyssinian", 2017, True, 8)
cat.print_name()
cat.print_data()
cat.toggle_alive()
cat.print_name()
cat.print_age()
cat.rename("Jack")
cat.print_name()
cat.change_age(8)
cat.print_age()
cat.change_weight(31)

dog = Dog("Keith", "Shepherd", 2015, True, 32, "woof")
dog.bark()

# Zaletą dziedziczenia na pewno można uznać możliwość przekazywania jednej implementacji, opisanej w klasie bazowej, do wszystkich klas dziedziczących. Jednocześnie, wadą może okazać się trudność zmiany małej części implementacji - gdy klasy różnią się małym szczegółem, dziedziczenie możę "narzucać"takie samo zachowanie klasy dziedziczącej i bazowej.

# Wadą polimorfizmu jest ograniczona czytelność kodu -np. podczas wywołania metody może nie być oczywiste czy wywołujemy metodę widocznej klasy, czy klasy do niej nadrzędnej. Zaletą może być natomiast łatwe użycie tych metod - dla różnych typów metoda może nazywać się tak samo i w momencie wywołania "automatycznie" uruchomi się odpowiednia metoda w zależności od typu obiektu.

# Do zalet hermetyzacji możemy zaliczyć możliwość ukrycia niepotrzebnych danych, funkcjonalnośc lub szczegółów implementacyjnych klasy, a mimo tego i tak korzystać z nich w obrębie tej klasy. Jako wadę można uznać dodatkowy nakład pracy, gdy np. hermetyczna metoda okaże się potrzebna "na zewnątrz", w miejscu, w którym jest niedostępna.
