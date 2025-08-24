from collections import Counter


def canConstruct(ransomNote, magazine):
    word_1 = Counter(ransomNote)
    word_2 = Counter(magazine)
    for index in word_1:
        if index not in word_2 or word_1[index] > word_2[index]:
            return False
    return True


ransomNote = "aa"
magazine = "ab"

print(canConstruct(ransomNote, magazine))
