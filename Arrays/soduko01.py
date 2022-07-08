

def valid_row(row, grid):
    temp = grid[row]
    temp = list(filter(lambda x: x != '.', temp))

    if len(temp) != len(set(temp)):
        return 0
    return 1

def valid_col(col, grid):
    temp = [row[col] for row in grid ]
    temp = list(filter(lambda x: x != '.', temp))

    if len(temp) != len(set(temp)):
        return 0
    return 1

def valid_subsquares_col(row, grid):
    temp = []
    for i in range(3):
        temp.append(grid[row][i])

    temp = list(filter(lambda x: x != '.', temp))
    if len(temp) != len(set(temp)):
        return 0
    return 1

def valid_subsquares_row(col, grid):
    temp = [row[col] for row in grid]
    temp = list(filter(lambda x: x !='.', temp))
    if len(temp) != len(set(temp)):
        return 0
    return 1



def valid_board(grid):
    # valid = False
    for i in range(9):
        row_checker = valid_row(i, grid)
        col_checker = valid_row(i, grid)
        if row_checker < 1 or col_checker  < 1:
            return False

        return True

    for i in range(0,9, 3):
        for k in range(3):
            valid_sq_col_checker = valid_subsquares_col(k, grid)
            valid_sq_row_checker = valid_subsquares_row(k, grid)
            if valid_sq_row_checker < 1 or valid_sq_col_checker  < 1:
                return False

            return True





board_c =[
     ["5","3",".",".","7",".",".",".","5"]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

board_w = [
     ["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
# print_board(board2)

# print(valid_row(1, board))
# print(valid_col(0, board))
print(valid_board(board_c))
print(valid_board(board_w))