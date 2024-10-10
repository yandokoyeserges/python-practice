def o1knapsack(values,weights,W):
    n=len(values)

    ratios=[(values[i]/weights[i],values[i],weights[i]) for i in range(n)]

    ratios.sort(reverse=True)
    total_value=0
    current_weight=0
    for ratio,value,weight in ratios:
        if current_weight<=W:
            total_value=total_value+value
            current_weight=current_weight+weight
        else:
            fraction=(W-current_weight)/weight
            total_value=total_value*fraction
            break
    return total_value
values = [200, 100, 110]
weights = [60, 50, 45]
W = 200

max_value = o1knapsack(values, weights,W)
print(f"The maximum value that can be put in the knapsack is {max_value}")