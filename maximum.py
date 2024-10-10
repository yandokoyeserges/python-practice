numbers=input("enter numbers of a list:")
list=numbers.split()
count=0
for i in list:
    count=count+1
print("lentght of list is:" ,count)
for i in range(count):
    list[i]=int(list[i])
print(list)
maximum= list[0]
for i in list:
    if i>maximum:
        maximum=i
print(f"maximum number is: {maximum}")



