
def someAreEven(arr):
    if len(arr) == 0:
        return False
    if isEven(arr[0]):
        return True
    return someAreEven(arr[1:])


def isEven(num):
    return True if num % 2 == 0 else False


print(someAreEven([1, 3, 5, 7, 9]))
print(someAreEven([1, 2, 5, 7, 9]))