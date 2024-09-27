def carFleet(target, position, speed):
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []
    for p, s in sorted(pair)[::-1]:
        stack.append((target - p) / float(s))
        # print(stack[-1])
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


def carFleet1(target, position, speed):
    stack = []
    for pos, v in sorted(zip(position, speed), reverse=True):

        dist = target - pos
        time = dist / float(v)

        if not stack:
            stack.append(time)
        elif time > stack[-1]:
            stack.append(time)

    return len(stack)


target = 10
position = [6, 8]
speed = [3, 2]
print(carFleet(target, position, speed))
