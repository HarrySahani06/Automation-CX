# to add a commnet to any syntax use #

# to assign a value to variable, special charecters are not allowed while creating a variable name except _,
# a variable start with _ or alphabet

a=10
b="hello"
c="world"
print(b+c)
# python support multiple variable initialization
z=x=c=10
print(z)
print(x)
print(c)
r,s,t=10,1.0,"welcome"

print(type(r))
print(type(s))
print(type(t))
#identifier(variables are same )/ keywords(variable that are reserved by programming language)
# Datatypes
# Numercials = int, float,complex
# Text =str= "rahul"
# Boolean =true/false
# Sequence= list, tuple, range
# Map =dict
# Set= set, frozenset
# Binary =bytes, memoryview, bytery

x=["one", "two"]
print(type(x))
print(isinstance(x,int))

x={"one", "two"}
print(type(x))

x=("one", "two")
print(type(x))

x=frozenset({"one", "two"})
print(type(x))

x={"firstName":"one", "SecondName":"two"}
print(type(x))

print(2*2)
print(2**10)

import random
print(random.randrange(10,20))

from math import pi
print(pi)
print (type(pi))


# to  function to  know nature  type(), isinstance()

e="hello world"
print(e)

g="""
hello 
world 
my name is :
"""

print (g)
name="rahul"
print (name)
print (name[2])
print (name[1:4])
print (name[1:4:2])
print (name[::-1])#to reverse a sting
print(len(name))
print (e.strip())
print(e.upper())
a=e.split(" ")
print(b[0])

#string formatters
city="Gurgaon"
State = "Haryana"
print(f"hey i Live in {city} and state is {State}")
print (f"hey i Live in {city} and state is {State}".format(city, State))

#List  introduction
"""
the order of list is always preserved 
list allows duplicate values 
list is mutable 
"""
a=[]
b= [1,3.0,"Rahul",2+3j,True,"Rahul"]
print(type(b))
print(b)
print(b[2])

b.append("corty")
print(b)

#updating list values
b[2]="harshit"
print(b)
b[1:4]=["harry","sahani","citymall"]
print(b)
del b[6]
print(b)

# list can be concatenated


#Diction tutorial

"""
A Dictionary is a Key and a value pair

"""

D1={

    "Name":"Rahul",
    "Dept":"Tech",
    "Age":30
}
print(D1)
print(type(D1))

D2={

    "Name":"harshit",
    "Dept":"Tech",
    "Age":25,
    "Salary":10
}
#upadte dictionary

D2["Name"]="Sahani"
print(D2)


#introduction to tuples

"""
1: It is used to store the sequence of immutable objects 
2: Mostly all other operations are similar to List 

"""

T1=("rahul",1,1.2)
print(type(T1))

"""
1:Repeatation
2: concatination
3:Membership operation
4: Iteration 

"""

print(T1 *2) #repeatation
T2=("harry",2,2.2)
print(T1+T2) #concatination
print("harry" in T2) # Membership operation
print("harry"  not in T2)


#introduction to set
"""
1: It is similar to List 
2: It can store different type of values like int, string float, boolean etc
3: It cannot have duplicate values 
4: are defined in {}
5: It is a collection which is unordered and unindexed
"""

S1={"rahul","harshit","citymall",2,True}
print(S1)
S1.add(1.20)
S1.remove("citymall")
print(S1)

