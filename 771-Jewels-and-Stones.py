def numJewelsInStones(jewels, stones):
    count = 0
    for index in stones:
        if index in jewels:
            count += 1
    return count


JEWELS = "aA"
stones = "aAAbbbb"

print(numJewelsInStones(JEWELS, stones))
