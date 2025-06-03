def mergeAlternately(word1, word2):
    merged = ""
    n = min(len(word1), len(word2))
    for index in range(n):
        merged = merged + word1[index] + word2[index]
    if len(word1) > len(word2):
        merged = merged + word1[n:]
    else:
        merged = merged + word2[n:]
    return merged


word1 = "ab"
word2 = "pqrs"

print(mergeAlternately(word1, word2))
