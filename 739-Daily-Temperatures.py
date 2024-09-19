def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)  # Initialize the answer array with zeros
    stack = []  # Stack to store indices of temperatures
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index

        stack.append(i)
    return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))

l1 = ["sleep", "eat", "repeat", "up"]


# for count, ele in enumerate(l1):
#    print(count, ele)

enum_l1 = enumerate(l1)
next_element = next(enum_l1)
next_element = next(enum_l1)
# print(next_element)
