def romanNumber(roman):
    diccionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    """ roman = roman[::-1]
    print(roman)

    for number in roman:
        temp = diccionary[number]
        if temp * 3 > result:
            result += temp
        else:
            result -= temp
    return result """
    for index in range(len(roman) - 1):
        if diccionary[roman[index]] < diccionary[roman[index + 1]]:
            result -= diccionary[roman[index]]
        else:
            result += diccionary[roman[index]]
    # result += diccionary[roman[-1]]
    return result


print(romanNumber("LXIV"))
