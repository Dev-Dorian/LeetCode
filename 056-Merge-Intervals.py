def merge(intervals):
    # intervals.sort(key=lambda x: x[0])
    intervals.sort()
    print(intervals)
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
            print(merged[-1], merged[-1][1], interval[0])
        else:
            print(merged[-1][1], interval[1])
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


intervals = [[1, 3], [8, 10],  [2, 6], [15, 18]]
print(merge(intervals))
