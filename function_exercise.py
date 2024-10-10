import math
def wall(we,he,cavar):
    no=we*he/cavar
    print(f"number of canse needed is {round(no)} ")
w=int(input("enter weight:"))
h=int(input("enter heigha:"))
c=8
wall(we=w,he=h,cavar=c)
wall(12,45,67)

def area(Longeur,largeur):
    surface=math.ceil(Longeur*largeur/2)
    print(f"surface es {surface}")
L=int(input("enter longueur:"))
l=int(input("enter largeur:"))
area(Longeur=L,largeur=l)