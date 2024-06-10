

def palindrome(word):
    word = str(word)
    inverse = word[::-1]
    return inverse == word


print(palindrome("10"))
