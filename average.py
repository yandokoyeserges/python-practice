heights=input('enter the values of height:')
list1=heights.split()
count=0
for i in list1:
    count=count+1
print(count)
for i in range(count):
    list1[i]=int(list1[i])
total=0
for i in list1:
    total=total+i
aver=total/count
aver=round(aver,1)
print(aver)



