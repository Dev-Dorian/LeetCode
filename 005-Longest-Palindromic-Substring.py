def palindromic(s):
    current = ""
    maxPalindromic = ""

    for i in range(len(s)):
        odd = expandAround(s, i, i)
        even = expandAround(s, i, i + 1)
        current = odd if len(odd) > len(even) else even
        maxPalindromic = maxPalindromic if len(
            maxPalindromic) > len(current) else current
    return maxPalindromic


def expandAround(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


print(palindromic("ABC"))


def longest(s):
    N = len(s)

    def LP(l, r):
        while r < N and l >= 0:
            if s[r] != s[l]:
                break
            r += 1
            l -= 1
        return l+1, r
    start, end = 0, 0

    for i in range(N):
        l, r = LP(i, i)
        if (r-l) > (end-start):
            end = r
            start = l
        l, r = LP(i, i+1)
        if (r-l) > (end-start):
            end = r
            start = l
    return s[start:end]


print(longest("ABC"))
