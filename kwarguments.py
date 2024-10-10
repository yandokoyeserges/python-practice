def sum(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c}")
sum(12,33,45,66,8)

def info(**info):
   for key,value in info.items():
    print(key,value)
info(name="serges",age=24,deprt="mca")
info(name="kana",depart="biologie")

def infoo(*numbers,**info):
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c}")
    for key,value in info.items():
        print(key,value)
infoo(1,2,name="serges",age=28)
infoo(12,45,proince="kayanza",commune="kabarore")




