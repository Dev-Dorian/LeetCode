def checkInclusion1(s1, s2):
    stringS1 = len(s1)
    stringS2 = len(s2)

    if stringS1 > stringS2:
        return False

    countS1 = [0] * 26
    countS2 = [0] * 26

    for index in range(len(s1)):
        countS1[ord(s1[index]) - ord('a')] += 1
        countS2[ord(s2[index]) - ord('a')] += 1

    for index in range(stringS2 - stringS1):
        if countS1 == countS2:
            return True
        countS2[ord(s2[index]) - ord('a')] -= 1
        countS2[ord(s2[index + stringS1]) - ord('a')] += 1
    return countS1 == countS2


s1 = "adc"
s2 = "dcda"

print(checkInclusion1(s1, s2))
