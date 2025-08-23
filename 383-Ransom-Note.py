from collections import Counter


def canConstruct(ransomNote, magazine):
    word_1 = Counter(ransomNote)
    word_2 = Counter(magazine)
    if word_1 == word_2:
        return True
    return False


ransomNote = "aa"
magazine = "aa"

print(canConstruct(ransomNote, magazine))
