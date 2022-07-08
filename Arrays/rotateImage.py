

def rotate(matrix):
    l , r =0, len(matrix) -1

    while l  < r:
        for i in range(r -l):
            top, bottom = l ,r

            # save the topleft
            topLeft = matrix[top][l+ i]

            # move the bottom left into the top left
            matrix[top][l + i] = matrix[bottom -i][l]

            # move  the bottom right into the bottom left
            matrix[bottom -i][l] = matrix[bottom][r -i]

            # move the top right to the bottom left
            matrix[bottom][r -i] = matrix[top +i][r]

            # move the top left into top right
            matrix[top +i][r] = topLeft

        r-= 1
        l +=1

    return matrix


print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

