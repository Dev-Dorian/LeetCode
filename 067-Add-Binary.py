def addBinary(a, b):
    res = []
    carry = 0

    i = len(a) - 1  # 11 - 1 = 1
    j = len(b) - 1  # 1 - 1 = 0
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        res.append(str(carry % 2))
        carry //= 2
    return ''.join(reversed(res))


print(addBinary("11", "1"))


def addBinary1(a, b):
    res = ""
    carry = 0

    a, b = a[::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        digitA = ord(a[i]) - ord("0") if i < len(a) else 0
        digitB = ord(b[i]) - ord("0") if i < len(b) else 0

        total = digitA + digitB + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2
    if carry:
        res = "1" + res
    return res


# print(addBinary1("11", "1"))


def addBinary2(a, b):
    binary = int(a, 2) + int(b, 2)
    return "{:b}".format(binary)


# print(addBinary2("11", "1"))
