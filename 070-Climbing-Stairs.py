def functionClimb(n):
    if n <= 2:
        return n
    step = [0 for _ in range(n)]
    step[0] = 1
    step[1] = 2

    for climb in range(2, n):
        step[climb] = step[climb - 1] + step[climb - 2]
    return step[-1]


print(functionClimb(3))


def functionClimb1(n):
    if n <= 1:
        return 1
    a = 1
    b = 1
    c = 0

    for i in range(1, n):
        c = a + b
        b = a
        a = c
    return c


print(functionClimb1(3))
