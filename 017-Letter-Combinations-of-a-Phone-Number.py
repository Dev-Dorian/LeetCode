def phoneNumber(digits):
    if not digits:
        return []

    map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []
    combinations("", digits, map, result)
    return result


def combinations(combination, nextDigits, map, result):
    if len(nextDigits) == 0:
        result.append(combination)
    else:
        for letter in map[nextDigits[0]]:
            combinations(combination + letter, nextDigits[1:], map, result)


print(phoneNumber("23"))
