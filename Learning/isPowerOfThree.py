def isPowerOfThree(n):

    if n == 1:
        return True
    if n > 1:
        return isPowerOfThree(n/3)
    return False


print(isPowerOfThree(9))
print(isPowerOfThree(5))
print(isPowerOfThree(0))