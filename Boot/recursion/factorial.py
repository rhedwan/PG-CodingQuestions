def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positve integers only'
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))
print(factorial(10))
print(factorial(1))
print(factorial(1.2))