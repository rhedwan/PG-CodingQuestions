def capitalizeFirst(arr):

    # temp = []
    # for i in range(len(arr)):
    #     temp.append(arr[i][0].upper() + arr[i][1:].lower())
    #
    # return temp
    result = []
    if len(arr) == 0:
        return result

    result.append(arr[0][0].upper() + arr[0][1:].lower())
    return result + capitalizeFirst(arr[1:])


print(capitalizeFirst(['nigeria', 'lagOs', 'kano']))
