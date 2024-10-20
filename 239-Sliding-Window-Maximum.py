from collections import deque


def maxSlidingWindow(nums, k):
    q = deque()
    answer = []
    for index, value in enumerate(nums):
        if q and index - k + 1 > q[0]:
            q.popleft()
        while q and nums[q[-1]] <= value:
            q.pop()
        q.append(index)
        if index >= k - 1:
            answer.append(nums[q[0]])
    return answer


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))
