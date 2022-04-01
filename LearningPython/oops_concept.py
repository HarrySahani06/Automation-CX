"""

oops concept/ procedural language(step oriented language)

1:Classes
2: Object
3: encapsulation
4:Abstraction
5: Inheritence
5: Polymorphism

"""

"""
class can be defined as a blue print/ template that can define the state or behaviour of object 

defination 

class<statement>:
    statement
"""

class human:
    eyes="blue"
    nose="large"

    def eye_function(self):
        print("functions of eyes")
        #here self states the instance  of class through which we can use its attributes etc

    def nose_function(self):
        print("functions of smell")
        #here self states the instance  of class through which we can use its attributes etc

    #declaring a object of  class
obj= human()
obj.nose_function()
obj.eye_function()


obj1= human()
obj1.nose_function()
obj1.eye_function()

#constructor  intro
"""
they are called first function of class

syntax:  __init__()

All classes have this function which is always executed when class is initiated or an object of class is created
"""


class construct:
    def __init__(self, name, id):
        print("inside a constructor ")
        self.name=name
        self.id=id

    def display(self):
        print("name is:", self.name)
        print("id is ",self.id)


#inheritence introduction

"""
Inheritence 

class A  ----> base /parent class

    def add(self)
    
class B  --->derived class/child class 


from inheritence we can access member, properties and methods of another class 

A  <--B  <--C   multi level inheritence 

A   B  
            this is known as multiple inheritence 
 C(A, B)    

"""

class Animal:
    def a(self):
        print("inside animal class")