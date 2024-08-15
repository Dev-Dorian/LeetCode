def ValidAnagram(s, t):
    s = s.lower()
    t = t.lower()
    return sorted(s) == sorted(t)


print(ValidAnagram("roMa", "orma"))


def ValidAnagram1(s, t):
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


print(ValidAnagram1("ROMa", "roAm"))
