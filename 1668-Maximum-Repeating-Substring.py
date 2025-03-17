def maxRepeating(sequence, word):
    count = 0
    # da = word * count not in sequence
    # print(da)
    while True:
        if word * count not in sequence:
            return count - 1
        count += 1


def maxRepeating_1(sequence, word):
    if not sequence or not word:
        return 0
    dp = [0] * (len(sequence))
    w = len(word)
    mx = 0
    for index in range(len(sequence)):
        print(sequence[index:index+w])
        if sequence[index:index+w] == word:
            dp[index] = dp[index-w] + 1
            mx = max(mx, dp[index])
    return mx


sequence = "ababc"
word = "ab"
print(maxRepeating_1(sequence, word))
