def sum(a,b):
    c=a+b
    print(f"value of c is {c}")
sum(12,45)
sum(11,10)
def summ(a=5,b=5):
    m=a+b
    print(f"value of m is {m}")
summ(5,5)
summ(11,34)
def ident(name,age):
    print(f"my name is {name} and i am {age} old")
ident("serges",32)
def addd(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(c)
addd(1,4)
addd(1,3,5)
def ident(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
ident(name="serges",age=23,school="SSET")
ident(name="kana",age=78,tell=25279)

def prime_cheker(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    if is_prime==True:
            print(f"number {n} is prime number")
    else:
            print(f"number {n} is not prime number")
n=int(input("enter a number:"))
prime_cheker(n)

