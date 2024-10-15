# exercise using Sliding Window

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

# exercise using Sliding Window


def characterReplacement1(s, k):
    count = {}
    maxLength = 0
    start = 0
    end = 0
    maxC = 0
    while end < len(s):
        count[s[end]] = 1 + count.get(s[end], 0)
        maxC = max(maxC, count[s[end]])
        while (end - start + 1) - maxC > k:
            count[s[start]] -= 1
            start += 1
        maxLength = max(maxLength, (end - start + 1))
        end += 1
    return maxLength


s = "ABAB"
k = 2

print(characterReplacement(s, k))
print(characterReplacement1(s, k))
