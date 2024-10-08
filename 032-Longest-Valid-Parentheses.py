def LongestValidParentheses(s):
    stack = [-1]
    print(stack)
    max_length = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length


print(LongestValidParentheses("())"))
