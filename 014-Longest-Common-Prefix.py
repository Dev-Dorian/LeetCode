list = ["flopwer", "flop", "flopght", "floptad"]


def longest(strs):
    prefix = strs[0]
    # print(prefix)
    for word in strs:
        while word.find(prefix) != 0:
            # print(word.find(prefix))
            prefix = prefix[:-1]
            if prefix == "":
                print(prefix)
                return ""
    return prefix


print(longest(list))


def longestCommonPrefix(listing):
    if len(listing) == 0:
        return ""
    minlen = len(listing[0])
    for i in range(len(listing)):
        minlen = min(len(listing[i]), minlen)
    lcp = ""
    i = 0
    while i < minlen:
        char = listing[0][i]
        for j in range(i, len(listing)):
            if listing[j][i] != char:
                return lcp
        lcp = lcp + char
        i += 1
    return lcp


print(longestCommonPrefix(list))
