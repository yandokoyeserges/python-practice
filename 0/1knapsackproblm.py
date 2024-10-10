

def fractional_knapsack(values,weights,W):
    n=len(values)
    #calculate v/weight ratio or every iterm
    ratios=[(values[i]/weights[i],values[i],weights[i]) for i in range(n)]
    #sort iterms based on ratio in no-increasing order
    ratios.sort(reverse=True)
    total_value=0 #initialize total-value
    current_weight=0 #initialize current weight
    #loop through all iterns
    for ratio,value,weight in ratios:
        if current_weight+weight<=W:
           #add entire item
            total_value +=value
            current_weight +=weight
        else:

           #fraction=(W-current_weight)/weight

           #total_value +=value*fraction
           break
    return total_value


values=[15,20,30,45]
weights=[20,45,67,89]
W=20

res=fractional_knapsack(values,weights,W)
print(round(res,1))
print("max value:",round(res,1))