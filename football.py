bills=[1000,2000,3000]
age=int(input("enter your age:"))
bill=int(input("enter your bill:"))
if age>18:
    if bill==bills[0]:
                  print("take seat in simple place")
    elif bill==bills[1]:
                  print("take siat in VP")
    elif bill==bills[2]:
                 print("take seat in VVP")
    else:
                   print("sorry")
if age<18:
    print("you are stupid")
