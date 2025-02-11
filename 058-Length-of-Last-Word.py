def Length(s):
    if len(s) == 0:
        return 0
    array = s.split()
    amount = len(array)
    lastWord = array[amount - 1]
    return len(lastWord)
    # print(amount, array, lastWord)


def Length1(s):
    length = 0
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length


print(Length('   fly me   to   the moon  '))
print(Length1('   fly me   to   the moon  '))
