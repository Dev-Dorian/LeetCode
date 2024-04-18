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
        print("NUMERO DICCIONARIO ", diccionary[number])
        print("NUMERO TEMP", temp)
        print("RESULTADO: ", result)
        print("EXTERIOR IF: ", temp * 3)
        print()
        if temp * 3 > result:
            # print("INTERIOR IF", temp * 3, result)
            result += temp
            print("RESULTADO DESPUES POSITIVO", result)
        else:
            result -= temp
            print("RESULTADO DESPUES NEGATIVO", result)
    return result


print(romanNumber("LXIV"))
