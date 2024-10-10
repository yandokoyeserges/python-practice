def printMaxActivity(s,f):
    n=len(f)
    print("the following activities are selected")
    #the activity is always seleceted
    i=0
    print(i)
    #consider test of the activities
    for j in range(n):
        if s[j]>=f[j]:
            print(j)
            i=j
            
#exemple
s=[1,3,0,5,8,5]
f=[2,4,6,6,7,9]

printMaxActivity(s,f)
