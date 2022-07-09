
def reverse(string):

    if len(string) == 0:
        return ""
    if len(string) == 1:
        return  string

    return string[-1] + reverse(string[:-1])


print(reverse('lagos'))
print(reverse('rhedwan'))
print(reverse('Ridwan'))
print(reverse(''))