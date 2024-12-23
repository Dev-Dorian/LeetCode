def isAnagram(s, t):
    s = s.lower()
    t = t.lower()
    return sorted(s) == sorted(t)


print(isAnagram("roMa", "orma"))


def isAnagram1(s, t):
    s = s.lower()
    t = t.lower()

    if len(s) != len(t):
        return False
    count = [0 for i in range(26)]

    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    for num in count:
        if num != 0:
            return False
    return True


print(isAnagram1("ROMa", "roAm"))


def isAnagram2(s, t):
    if len(s) != len(t):
        return False
    hashS = {}
    hashT = {}

    for i in range(len(s)):
        hashS[s[i]] = 1 + hashS.get(s[i], 0)
        hashT[s[i]] = 1 + hashT.get(s[i], 0)

    for i in s:
        if hashS[i] != hashT.get(i, 0):
            return False
    return True


print(isAnagram2("ROMa", "roAm"))


def isAnagram3(s, t):
    if len(s) != len(t):
        return False
    hashS = {}
    hashT = {}

    for i in range(len(s)):
        hashS[s[i]] = hashS.get(s[i], 0) + 1

    for i in range(len(t)):
        hashT[t[i]] = hashT.get(t[i], 0) + 1

    return hashS == hashT


print(isAnagram3("rac", "car"))


def isAnagram4(s, t):
    ms = {}
    mt = {}
    for char in s:
        ms[char] = ms.get(char, 0) + 1
    for char in t:
        mt[char] = mt.get(char, 0) + 1
    return ms == mt


print(isAnagram4("rac", "car"))
