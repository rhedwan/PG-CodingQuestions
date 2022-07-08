
def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'fibonacci number must be positve integers only'

    if n == 0:
        return n

    return n%10 + sumOfDigits(n//10)


print(sumOfDigits(3))
print(sumOfDigits(31))
print(sumOfDigits(131))
print(sumOfDigits(0))
print(sumOfDigits(24342))