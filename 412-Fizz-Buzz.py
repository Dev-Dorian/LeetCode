def fizzBuzz(n):
    array = []
    for numbers in range(1, n + 1):
        if numbers % 3 == 0 and numbers % 5 == 0:
            array.append("FizzBuzz")
        elif numbers % 3 == 0:
            array.append("Fizz")
        elif numbers % 5 == 0:
            array.append("Buzz")
        else:
            array.append(str(numbers))
    return array


print(fizzBuzz(10))


def fizzBuzz1(n):
    for numbers in range(1, n + 1):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)


print(fizzBuzz1(15))
