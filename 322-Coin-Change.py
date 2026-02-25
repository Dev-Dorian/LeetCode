def coinChange(coins, amount):
    # dp = [amount + 1] * (amount + 1)
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for index in range(1, amount + 1):
        for coin in coins:
            if index - coin >= 0:
                print(f"{index, coin} = {index - coin}")
                dp[index] = min(dp[index], 1 + dp[index-coin])
                print(dp[index], 1 + dp[index-coin])
    # return dp[amount] if dp[amount] != amount + 1 else -1
    return dp[amount] if dp[amount] != float("inf") else -1


def coinChangeRecursive(coins, amount):
    # Caso Base 1: Si el monto es 0, no necesitamos más monedas
    if amount == 0:
        return 0

    # Caso Base 2: Si el monto es negativo, este camino es imposible
    if amount < 0:
        return float('inf')

    min_monedas = float('inf')

    # Aquí es donde se crean las "ramas" de tu árbol
    for c in coins:
        # Llamamos a la función de nuevo (bajamos un nivel en el árbol)
        resultado = coinChangeRecursive(coins, amount - c)

        # Si el camino llegó a 0, sumamos 1 (por la moneda usada)
        if resultado != float('inf'):
            min_monedas = min(min_monedas, 1 + resultado)

    return min_monedas


# Probamos con el ejemplo que analizamos
coins = [2, 3]
amount = 5


# print(coinChange(coins, amount))
print(f"Mínimo de monedas: {coinChangeRecursive(coins, amount)}")
