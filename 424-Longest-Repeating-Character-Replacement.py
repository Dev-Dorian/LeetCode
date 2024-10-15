def characterReplacement(s, k):
    longest = 0
    left = 0
    counts = [0] * 26
    for right in range(len(s)):
        counts[ord(s[right]) - 65] += 1
        while (right - left + 1) - max(counts) > k:
            counts[ord(s[left]) - 65] -= 1
            left += 1
        longest = max(longest, (right-left+1))
    return longest


s = "ABAB"
k = 2

print(characterReplacement(s, k))
