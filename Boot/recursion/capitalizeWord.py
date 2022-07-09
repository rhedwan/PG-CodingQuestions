def capitalizeWord(arr):
    result = []
    if len(arr) == 0:
        return result

    result.append(arr[0].upper())
    return result + capitalizeWord(arr[1:])


print(capitalizeWord(['a', 'love', 'polw']))