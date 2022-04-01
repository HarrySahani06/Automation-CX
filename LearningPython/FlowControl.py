# Python Flow Control
"""
1: IF statement
2: IF Else Statement
3: IF ELIF Statement
4:For Loop
5: While Loop
5: Nested Loop
7:Break
8:continue
9: loop with else block
"""
#indentation for code is very important
a=10
b=20
if a<b:
    print(a)
    print ("inside if block")
else:
    print("Second number  is greater", b)
print ("outside block")

marks = int(input("Enter marks : "))
if marks>80:
    if a==10:
        print("pass")
    print ("80%")
elif 60<marks<80:
    print ("grade B")
else:
    print ("grade c")





