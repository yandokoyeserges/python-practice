#python program to test bmi
weight=float(input("enter weight:"))
height=float(input("enter height:"))

bmi=round(weight/height**2,2)

if bmi<18.5:
    print(f"your bmi is {bmi}and you are underweight")
elif bmi>18.5 and bmi<24.9:
    print(f"your bmi is {bmi} and you are normal weight")
elif bmi>24.9 and bmi<29.9:
    print(f"your bmi is {bmi} and you are overweight")
else:
     print(f"your bmi is {bmi} and you are obese")


