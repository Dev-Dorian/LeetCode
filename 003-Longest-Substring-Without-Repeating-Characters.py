def lengthOfLongestSub(s):
    ans = 0
    n = len(s)
    charIndex = {}
    i = 0
    for j in range(n):
        if s[j] in charIndex:
            i = max(i, charIndex[s[j]])
        ans = max(ans, j - i + 1)
        charIndex[s[j]] = j + 1
    return ans

# exercise using Sliding Window


def lengthOfLongestSub1(s):
    letters = set()
    maxLenght = 0
    left = 0
    for right, c in enumerate(s):
        while c in letters:
            letters.remove(s[left])
            left += 1
        letters.add(c)
        maxLenght = max(maxLenght, right - left + 1)
    return maxLenght


print(lengthOfLongestSub("abcabcbb"))
print(lengthOfLongestSub1("abcabcbb"))
