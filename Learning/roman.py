def roman(string):
    roman_value = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    num = 0
    for i in range(len(string)):
        if i + 1 < len(string) and roman_value[string[i]] <= roman_value[string[i + 1]]:
            num -= roman_value[string[i]]

        else:
            num += roman_value[string[i]]

    return num


print(roman('III'))
print(roman('IX'))
print(roman('CM'))
