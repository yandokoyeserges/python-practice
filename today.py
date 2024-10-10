import random

arr1=[12,34,56,78,90]
num=random.choice(arr1)
num1=random.randint(a=0,b=10)
num2=random.randrange(1,12,2)
p=num+num1
print(num2)
print(num)
print(num1)
print(p)
arr2=[num,num1,num2,p]
print(arr2)
if p%2==0:
    print("p is even")
else:
    print("p is odd")
