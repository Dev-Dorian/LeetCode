def checkInclusion(s1, s2):
    stringS1 = len(s1)
    stringS2 = len(s2)

    if stringS2 < stringS1:
        return False

    countS1 = [0] * 26
    countS2 = [0] * 26

    for index in range(len(s1)):
        countS1[ord(s1[index]) - ord('a')] += 1
        countS2[ord(s2[index]) - ord('a')] += 1
    left = 0
    right = len(s1)

    while right < len(s2):
        if countS1 == countS2:
            return True
        countS2[ord(s2[right]) - ord('a')] += 1
        countS2[ord(s2[left]) - ord('a')] -= 1
        left += 1
        right += 1
    return False


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
