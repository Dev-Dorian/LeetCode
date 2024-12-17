def platesBetweenCandles(s, queries):
    n = len(s)
    presum = [0] * (n + 1)
    for i, c in enumerate(s):
        presum[i + 1] = presum[i] + (c == '*')
    left = [0] * n
    right = [0] * n
    l = r = -1
    for i, c in enumerate(s):
        if c == '|':
            l = i
        left[i] = l
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            r = i
        right[i] = r
    ans = [0] * len(queries)
    for k, (l, r) in enumerate(queries):
        i, j = right[l], left[r]
        if i >= 0 and j >= 0 and i < j:
            ans[k] = presum[j] - presum[i + 1]

    return ans


def platesBetweenCandles1(s, queries):
    n = len(s)

    # Step 1: Precompute the prefix sum of plates, and left and right candle positions
    # plates_prefix[i] = number of plates in s[0:i]
    plates_prefix = [0] * (n + 1)
    # left_candle[i] = nearest candle to the left of index i
    left_candle = [-1] * n
    # right_candle[i] = nearest candle to the right of index i
    right_candle = [-1] * n

    # Fill plates_prefix
    for i in range(n):
        plates_prefix[i + 1] = plates_prefix[i] + (1 if s[i] == '*' else 0)

    # Fill left_candle
    last_candle = -1
    for i in range(n):
        if s[i] == '|':
            last_candle = i
        left_candle[i] = last_candle

    # Fill right_candle
    last_candle = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            last_candle = i
        right_candle[i] = last_candle

    # Step 2: Answer each query
    result = []
    for left, right in queries:
        # Find the nearest candles on the left and right within the range
        left_c = right_candle[left]  # nearest candle to the right of 'left'
        right_c = left_candle[right]  # nearest candle to the left of 'right'

        # If there's no valid candle range, return 0 plates
        if left_c == -1 or right_c == -1 or left_c >= right_c:
            result.append(0)
        else:
            # Calculate number of plates between the two candles
            # data1 = plates_prefix[right_c + 1]
            # data2 = plates_prefix[left_c]
            # print(data1, data2)
            result.append(plates_prefix[right_c + 1] - plates_prefix[left_c])

    return result


def platesBetweenCandles2(s, queries):
    n = len(s)
    left = [-1] * n
    right = [n]*n
    stack = []
# Encontrar la vela más cercana a la izquierda para cada posición
    for i, c in enumerate(s):
        if c == '|':
            stack.append(i)
        elif stack:
            left[i] = stack[-1]
# Encontrar la vela más cercana a la derecha para cada posición
    stack = []
    for i in range(n-1, -1, -1):
        if s[i] == '|':
            stack.append(i)
        elif stack:
            right[i] = stack[-1]
  # Procesar las consultas
    result = []
    for l, r in queries:
        count = 0
        for i in range(l + 1, r):
            if left[i] >= + l and right[i] <= r:
                count += 1
        result.append(count)
    return result


s = "**|**|***|"
queries = [[2, 5], [5, 9]]
print(platesBetweenCandles(s, queries))
print(platesBetweenCandles1(s, queries))
print(platesBetweenCandles2(s, queries))
