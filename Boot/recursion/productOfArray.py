
def productOfArray(arr):

    if len(arr) == 0: return 1
    return arr[-1] * productOfArray(arr[:-1])


print(productOfArray([1,2,3]))
print(productOfArray([1,2,3,10]))
print(productOfArray([1,2,3.23,10, 90]))
