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
