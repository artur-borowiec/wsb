import datetime

class Human:
    def __init__(self, name, surname, birthYear, profession, isAlive):
        self.name = name
        self.surname = surname
        self.birthYear = birthYear
        self.profession = profession
        self.isAlive = isAlive
    
    def printFullName(self):
        print(f"{self.name} {self.surname}")
        
    def printFullInfo(self):
        print(f"{self.name} {self.surname} was born in {self.birthYear}. ")
        print(f"He/she works as {self.profession}") if self.isAlive else print("R.I.P.")
        
    def printAge(self):
        today = datetime.date.today()
        print(f"{self.name}'s age: {today.year-self.birthYear}")
        
    def changeJob(self, newJob):
        self.profession = newJob
    
h1 = Human("John", "Blake", 1997, "accountant", True)
h1.printFullName()
h1.printFullInfo()
h1.printAge()
h1.changeJob("programmer")
h1.printFullInfo()

class Cat:
    def __init__(self, name, breed, birthYear, isAlive):
        self.name = name
        self.breed = breed
        self.birthYear = birthYear
        self.isAlive = isAlive
        
    def printName(self):
        print(f"{self.name}, meow!" if self.isAlive else "<silence>")
        
    def printData(self):
        print(f"{self.name}, {self.breed} born in {self.birthYear}")
        
    def printAge(self):
        today = datetime.date.today()
        print(f"{self.name}'s age: {today.year-self.birthYear}")
        
    def toggleAlive(self):
        self.isAlive = not self.isAlive
        
    def rename(self, newName):
        self.name = newName
        
    def changeAge(self, age):
        today = datetime.date.today()
        self.birthYear = today.year-age

cat = Cat("Shadow", "Abyssinian", 2017, False)
cat.printName()
cat.printData()
cat.toggleAlive()
cat.printName()
cat.printAge()
cat.rename("Jack")
cat.printName()
cat.changeAge(8)
cat.printAge()
