def occurrence(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack) + 1 - len(needle)):
        if haystack[i: i + len(needle)] == needle:
            return i
        return -1


haystack = "sadbutsad"
needle = "sad"
print(occurrence(haystack, needle))
