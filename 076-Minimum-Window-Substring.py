def minWindow(s, t):
    if t == "":
        return ""
    countT = {}
    countS = {}

    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    need = len(countT)
    have = 0
    ansL = -1
    ansR = -1
    minLen = float("inf")

    left = 0
    for right, c in enumerate(s):
        if c in countT:
            countS[c] = 1 + countS.get(c, 0)
            if countS[c] == countT[c]:
                have += 1
        while have == need:
            newLen = right - left + 1
            if newLen < minLen:
                ansL = left
                ansR = right
            if s[left] in countT:
                countS[s[left]] -= 1
                if countS[s[left]] < countT[s[left]]:
                    have -= 1
            left += 1
    return s[ansL:ansR+1]


s = "ADOBBAN"
t = "AB"
print(minWindow(s, t))
