"""
polymorphism

1:operator overloading
2: method overloading
3: constructor overloading




class operator_Overload:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        total_pages=self.pages - other.pages
        return total_pages

obj= operator_Overload(10)
obj2 = obj= operator_Overload(10)

print(obj+obj2)

"""

# Method Overloading

class methodoverload:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c

obj3= methodoverload()
print(obj3.add(10,20))
print(obj3.add(10,20,30))

# Method overloading, Constructor oveload  is not at all not allowed in python