
def roman(string):
    roman_value ={
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
    }
    num = 0
    for i in range(len(string)-1, -1, -1):
        if roman_value[string[i]] <= roman_value[string[i+1]]
        print(roman_value[string[i]])



print(roman('VII'))