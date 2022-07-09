def recursiveRange(n):
    if n <= 1:
        return n
    return n + recursiveRange(n -1)

print(recursiveRange(6))
print(recursiveRange(10))
print(recursiveRange(50))
print(recursiveRange(5.2))