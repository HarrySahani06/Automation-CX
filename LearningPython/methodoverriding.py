"""

Method overriding


class Methodoverridbase:
    def __init__(self):
        print("inside base constructor")
    def add(self):
        print("inside base ")


class Methodoverridbase1(Methodoverridbase):
    def __init__(self):
        super().__init__()
        print("inside base constructor")
    def add(self):
        super().add()
        print("inside base 1 file ")

obj=Methodoverridbase1()
obj.add()

"""
"""

# type of methods 
1:Instance method
2: class method
3: static method
"""