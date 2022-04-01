"""
class AnimalParent:
    def ap(self):
        print("inside animal parent class ")
    def hello(self):

class Animal(AnimalParent):
    name="harry"
    def a(self):
        print("inside animal class")

class Mamals(Animal):
    def b(self):
        print( "inside mammal class")

mam= Mamals()
mam.b()
mam.a()
print(mam.name)
mam.ap()


"""
# multiple Inheritence

class AnimalParent:
    def ap(self):
        print("inside animal parent class ")
    def hello(self):
        print("inside hellp method")

class Animal():
    name="harry"
    def a(self):
        print("inside animal class")
    def hello(self):
        print("inside hello method")

class Mamals(AnimalParent,Animal):
    def b(self):
        print( "inside mammal class")

mam= Mamals()
mam.b()
mam.a()
print(mam.name)
mam.ap()
mam.hello()


