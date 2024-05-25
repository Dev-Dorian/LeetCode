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


print(lengthOfLongestSub("bbbbb"))
