import random
#first way
list1=["serges","kana","aaron","kadogo"]
y=random.choice(list1)
print(f"{y} will pay the bill")
#second way
names=str(input("enter names separated by camma:"))
list2=names.split(",")
y=random.choice(list2)
print(f"{y} will pay all bill that we take")
#third way
namess=str(input("enter names:"))
list3=namess.split(",")
m=len(list3)
k=random.randint(0,m-1)
n=list3[k]
print(f"{n} will pay all the bill")
