class Solution:
    def reverseInteger(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while (x > 0):
            cur = x % 10
            result = result * 10 + cur
            x //= 10
        result *= sign

        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result


if __name__ == "__main__":
    print(Solution().reverseInteger(-123))
