import random
print("welcome to password generator!!!")
letters=int(input("how many letter do you want?\n"))
numbers=int(input("how many numbers do you want?\n"))
symbols=int(input("how many symbols do you want?\n"))
L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
N=['0','1','2','3','4','5','6','7','8','9']
S=['~','`','@','#','<','>','%','%','^','&','*','(',')','#' ,'=','+','_',',','.','?','/','[',']']
password=""
for i in range(1,letters+1):
    char=random.choice(L)
    password +=char
for i in range(1,numbers+1):
    num=random.choice(N)
    password +=num
for i in range(1,symbols+1):
    sym=random.choice(S)
    password +=sym
print(password)
