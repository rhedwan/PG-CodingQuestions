def flatten(arr):
    resultArr = []

    for custItem in arr:

        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr


# print(flatten([1,2,3,[4,5,6,7]]))
# print(flatten([1,3,[4,5,6,7,[7,[4,5,6,7],90]]]))
print(flatten([[9, 0, 4, 56], 3, [4, 5, 6, 7]]))
