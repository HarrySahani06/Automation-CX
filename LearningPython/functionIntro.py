"""
Functions
1: block of code to perform and specific task
2: Resuable block
3: have parameters
4: collection of mulptile function create a class
5: pre-defined function like print() etc
6:  naming convention  is like  function name should be in lower case

def functionName:
        statement/code

"""

"""
def printing_my_name(name):
    print("name is :", name)

printing_my_name("harshit")

def printing_my_name(name):
    #print("name is :", name)
    return "name is :", name

print(printing_my_name("harshit"))
"""

def printing_my_name(name,age,salar):
    print("name is :", name, "age is ", age," salary is ", salar)
printing_my_name("harshit",30,12000)

"""
types of arguments 
1: Required Arguments 
2:keywords argument 
3: Default agrument 
4: variable length argument 
"""

def req_arg(a,b):
    print(a+b)

req_arg(10,20)
# keyword argment
printing_my_name(name="Rahul",age=20,salar=12000)

#default argument
def default_arg(name, school="Oxford"):
    print("name- {}".format(name))
    print("school - {}".format(school))

default_arg("harry")
default_arg("corty", "dps")

#variable length argument

def var_arg(*name):
    for i in name:
        print(i)

var_arg("rahul",30,1.0)