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
    roman = roman[::-1]

    for number in roman:
        temp = diccionary[number]
        if temp * 3 > result:
            result += temp
        else:
            result -= temp
    return result


print(romanNumber("LXIV"))
