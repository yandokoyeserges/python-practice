names=["serges","jonathan","eraste","sakubu","kana"]
name=str(input("enter name:"))
x=int(input("enter percentage:"))
if name in names and x>=75:
    print(f"{name} is allowed to appear in exam")
elif name in names and x<75:
    print(f"{name} is not allowed to appear in exam")
else:
    print("you are not our student")



