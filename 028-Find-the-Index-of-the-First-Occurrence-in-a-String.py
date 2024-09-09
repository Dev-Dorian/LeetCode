def occurrence(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return (-1)


haystack = "hello"
needle = "ll"
print(occurrence(haystack, needle))
