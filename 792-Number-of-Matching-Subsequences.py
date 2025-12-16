from collections import defaultdict


def numMatchingSubseq(s, words):
    def is_subsequence(word, s):
        it = iter(s)
        return all(char in it for char in word)

    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1

    count = 0
    for word, freq in word_count.items():
        if is_subsequence(word, s):
            count += freq
    return count


s = "abcde"
words = ["a", "bb", "acd", "ace"]

print(numMatchingSubseq(s, words))
