from collections import deque


class RecentCounter(object):
    def __init__(self):
        self.times = deque()

    def ping(self, t):
        self.times.append(t)
        # print(self.times[0], t, t - 3000)
        while self.times and self.times[0] < t - 3000:
            self.times.popleft()
        return len(self.times)


comand = ["RecentCounter", "ping", "ping", "ping", "ping"]
values = [[], [1], [100], [3001], [3002]]

# 2. List to save the outputs
objet = None
results = []

# 3. Step-by-step processing
for cmd, val in zip(comand, values):
    if cmd == "RecentCounter":
        objet = RecentCounter()
        results.append(None)
    elif cmd == "ping":
        result = objet.ping(val[0])
        results.append(result)

# 4. Show the final result
print("Result:", results)

""" recentCounter = RecentCounter()

print(recentCounter.ping(0))
print(recentCounter.ping(1))
print(recentCounter.ping(100))
print(recentCounter.ping(3001))
print(recentCounter.ping(3002)) """
