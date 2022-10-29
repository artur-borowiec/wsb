def fileCreate():
    file = open("Countries.txt", "w")
    file.write("Italy\n")
    file.write("Germany\n")
    file.write("Spain\n")
    file.close()
    
def fileOpen():
    file = openFile("r")
    print(file.read())

def fileAppendFrance():
    file = openFile("a")
    file.write("France\n")
    file.close()
    
def openFile(mode):
    return open("Countries.txt", mode)
    
def task106():
    file = open("Names.txt", "w")
    names = ["John", "Anne", "Michael", "Dwight", "Kevin"]
    for i in range(len(names)):
        file.write(f"{names[i]}\n")
    file.close()

def task107():
    file = open("Names.txt", "r")
    print(file.read())
    file.close()
    
def createCsv():
    file = open("Stars.csv", "w")
    newRecord = "Brian,73,Taurus\n"
    file.write(str(newRecord))
    file.close()

def createBooksCsv():
    file = open("Books.csv", "w")
    file.write(str("0,Too Kill A Mockingbird,Harper Lee,1960"))
    file.write(str("1,A Brief History of Time,Stephen Hawking,1988"))
    file.close()
    