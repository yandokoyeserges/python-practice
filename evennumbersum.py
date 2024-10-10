sum=0
for i in range(1,101):
    if i%2==0:
        sum=sum+i
print(sum)

for i in range(1,100):
    if i%3==0 and i%5==0:
             print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
       print("buzz")
    else:
       print(i)
for num in range(1,120):
    if num%2==0:
        print("absent")
    elif num%3==0:
        print("present")
    else:
        print("exclus")
EMPLOYEE_experiNCE_LIST=[5,10,3,1,5,6,7,8,9,5,4,6,7,8,9,0,14,15]
for i in EMPLOYEE_experiNCE_LIST:
    if i<5:
        print('EXLUS')
    elif i<10:
        print("prime")
    else:
        print("major")
