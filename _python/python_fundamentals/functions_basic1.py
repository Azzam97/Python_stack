#1
print("function1")
def a():
    return 5
print(a()) # 5

#2
print("function2")
def a():
    return 5
print(a()+a()) # 10

#3
print("function3")
def a():
    return 5
    return 10
print(a()) # 5

#4
print("function4")
def a():
    return 5
    print(10)
print(a()) # 5

#5
print("function5")
def a():
    print(5)
x = a()
print(x) # 5, none

#6
print("function6")
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) # 3,5,none

#7
print("function7")
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) # 25

#8
print("function8")
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) #100,10

#9
print("function9")
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3)) #7,14,21

#10
print("function10")
def a(b,c):
    return b+c
    return 10
print(a(3,5)) # 8

#11
print("function11")
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b) # 500,500,300,500

#12
print("function12")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b) #500,500,300,500

#13
print("function13")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b) # 500,500,300,300

#14
print("function14")
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() #1,3,2

#15
print("function15")
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y) #1,3,5,10


