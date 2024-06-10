def plusOne(digits):
    listLigits = ""
    for i in range(len(digits)):
        listLigits += str(digits[i])
        print(listLigits)
    num = int(listLigits) + 1
    listLigits = str(num)
    print(listLigits)
    digits.clear()
    for j in range(len(listLigits)):
        digits.append(int(listLigits[j]))
    return digits


digits = [9, 9, 9]
print(plusOne(digits))
