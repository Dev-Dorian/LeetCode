def intToRoman(num):
    romanNumbers = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    romanNum = ""
    for value, symbol in romanNumbers.items():
        while num >= value:
            romanNum += symbol
            num -= value
    return romanNum


print(intToRoman(3749))
