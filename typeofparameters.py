def typeofparameters(name,age):
    print(f"my name is {name}, i am {age} old")
typeofparameters("serges",78)

def sumof(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c}")

sumof(12,70,34,224)

def subtract(*numbers):
    c=0
    for i in numbers:
        c=c-i
    print(f"difference is {c}")
subtract(50,34)
sumof(78,90,12,10,1111)