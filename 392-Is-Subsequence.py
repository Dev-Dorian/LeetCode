def isSubsequence(s, t):
    S = len(s)
    T = len(t)
    if s == '':
        return True
    if S > T:
        return False
    j = 0
    for index in range(T):
        if t[index] == s[j]:
            if j == S-1:
                return True
            j += 1
    return False


s = "abc"
t = "ahbgd"

print(isSubsequence(s, t))
