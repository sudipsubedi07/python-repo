class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname + ' ' + self.lastname)

x = Person("Sabin", "Adhikari")
x.printname()

class Student(Person):
    pass

y = Student("Aakash", "Kandel")
y.printname()