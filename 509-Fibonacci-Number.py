def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for index in range(2, n + 1):
        dp[index] = dp[index - 1] + dp[index - 2]
    return dp[n]


def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    first = 0
    second = 1

    for _ in range(2, n + 1):
        temp = second
        second = first + second
        first = temp
    return second


n = 3
print(fib(n))
print(fib1(n))
