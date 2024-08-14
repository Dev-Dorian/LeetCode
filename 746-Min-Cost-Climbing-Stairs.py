def minCost(cost):
    memo = len(cost)
    number = [0] * memo
    number[0] = cost[0]
    number[1] = cost[1]
    for i in range(2, memo):
        number[i] = min(number[i - 1] + cost[i], number[i - 2] + cost[i])
    return min(number[memo - 1], number[memo - 2])


print(minCost([10, 15, 20]))
