def evaluateReverseNotation(tokens):
    stack = []
    for c in tokens:
        try:
            stack.append(int(c))
        except:
            b = stack.pop()
            a = stack.pop()
            if c == "+":
                a += b
            elif c == "-":
                a -= b
            elif c == "*":
                a *= b
            elif c == "/":
                a = int(a * 1.0 / b)
            stack.append(a)
    return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evaluateReverseNotation(tokens))


def evaluateReverseNotation1(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            b, a = stack.pop(), stack.pop()
            stack.append(int(a * 1.0 / b))
        else:
            stack.append(int(c))
    return stack[0]


tokens1 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evaluateReverseNotation1(tokens1))
