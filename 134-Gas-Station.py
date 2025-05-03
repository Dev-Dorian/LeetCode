def canCompleteCircuit(gas, cost):
    start = 0
    currentGas = 0
    totalGas = 0

    for index in range(len(gas)):
        print(index)
        currentGas += gas[index] - cost[index]
        totalGas += gas[index] - cost[index]
        if currentGas < 0:
            currentGas = 0
            start = index + 1
    return start if totalGas >= 0 else -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircuit(gas, cost))
