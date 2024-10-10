import random
# user choice=a and must be 0,1,or2

a=int(input("enter a value from user ,0 for lock,1 for paper and 2 for scisssor:"))
      # computer choice
b=random.randint(0,2)
print('b:'+ str(b))
if a>2 or a<0:
    print("error")
elif a==b:
    print("none wins,drop")
elif a == 2 and b == 0:
    print("loose")
elif a == 0 and b == 2:
    print(" I win ")
#we can use also imagesss

elif b>a:
    print("user loose  means that computer wins")
elif a>b:
    print("i win means that computer loose")


