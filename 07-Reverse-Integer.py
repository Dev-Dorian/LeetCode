def reverseInteger(x):
    result = 0
    prev = 0

    while (x != 0):
        cur = x % 10
        x //= 10
        result = result * 10 + cur
        if ((result - cur) // 10 != prev):
            return 0
        prev = result
    return result


if __name__ == "__main__":
    print(reverseInteger(123))
