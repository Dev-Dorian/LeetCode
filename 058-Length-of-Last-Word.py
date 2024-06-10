def Length(s):
    if len(s) == 0:
        return 0
    array = s.split()
    amount = len(array)
    lastWord = array[amount - 1]
    return len(lastWord)
    # print(amount, array, lastWord)


print(Length('   fly me   to   the moon  '))
