def isPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        while start < end and not (s[start].isalpha() or s[start].isdigit()):
            start += 1
        while start < end and not (s[end].isalpha() or s[end].isdigit()):
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start, end = start + 1, end - 1
    return True


print(isPalindrome("racecar"))
