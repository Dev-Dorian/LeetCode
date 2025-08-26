
import collections


def maxNumberOfBalloons(text):
    count = collections.Counter(text)
    print(count)
    letters = {
        "b": 1,
        "a": 1,
        "l": 2,
        "o": 2,
        "n": 1
    }
    return min(count[index] // letters[index] for index in letters)


text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))
