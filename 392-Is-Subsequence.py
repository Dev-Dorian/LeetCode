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


def isSubsequence_1(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == len(s) else False


def isSubsequence_2(s, t):
    S = len(s)
    T = len(t)
    i = 0
    j = 0
    while i < S and j < T:
        if s[i] == t[j]:
            i += 1
        j += 1
    return True if i == S else False


def isSubsequence_3(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


s = "abc"
t = "ahbgdc"

print(isSubsequence(s, t))
print(isSubsequence_1(s, t))
print(isSubsequence_2(s, t))
print(isSubsequence_3(s, t))
