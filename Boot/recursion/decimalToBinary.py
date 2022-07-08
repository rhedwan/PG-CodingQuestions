

def decimalToBinary(n):
    assert n < 0 and int(n) == n , 'Parameter must be integer '
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))


print(decimalToBinary(5))
print(decimalToBinary(-1))