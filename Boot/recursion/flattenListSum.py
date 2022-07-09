def flatten(arr):
    resultArr = []

    for custItem in arr:

        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)

    return resultArr


def arrSum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + arrSum(arr[1:])


# print(flatten([1,2,3,[4,5,6,7]]))
# print(flatten([1,3,[4,5,6,7,[7,[4,5,6,7],90]]]))
print(arrSum(flatten([[9, 0, 4, 56], 3, [4, 5, 6, 7]])))
print(arrSum(flatten([[1, 2], 3, [1, 2]])))
# print(arrSum([9, 0, -4, 56, 3, 4, 5, 6, 7]))
