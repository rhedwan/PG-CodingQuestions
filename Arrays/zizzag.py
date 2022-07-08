def solution(str, numRows):

    if numRows == 1:
        return str

    res = ''
    for r in range(numRows):
        increment = 2 * (numRows -1)
        for i in range(r, len(str), increment):
            print('ascd',i)
            res += str[i]
            print(i + increment - (2 * r ))
            # print( numRows -1)
            if ( r > 0 and r < numRows -1 and i + increment - (2 * r )< len(str) ):

                res += str[i + increment - (2 * r )]
    print(res)
    return res

solution('PAYPALISHIRING', 4)