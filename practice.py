list_ = 10

new_list = [i**2 for i in range(list_)]
print(new_list)


def check_column_wise(matrix):
    is_found = False
    length_of_matrix = len(matrix)
    for i in range(length_of_matrix):
        temp_storage = []
        for j in range(length_of_matrix):
            if (matrix[j][i] == "."):
                continue
            else:
                temp_storage.append(matrix[j][i])
        for k in temp_storage:
            if temp_storage.count(k) >= 2:
                is_found =  False
                break
            else:
                is_found = True
        if is_found:
            continue
        else:
            break
    return is_found

def check_row_wise(board):
    sudoku_formed = False
    for i in board:
        temp_storage = []
        for j in i:
            if j == ".":
                continue
            else:
                temp_storage.append(j)
        for k in temp_storage:
            if temp_storage.count(k) >= 2:
                sudoku_formed =  False
                break
            else:
                sudoku_formed = True
        if sudoku_formed:
            continue
        else:
            break
    return sudoku_formed

def check(board):
    result_for_rows = check_row_wise(board)
    if result_for_rows:
        result_for_columns = check_column_wise(board)
        if result_for_columns:
            print(True)
        else:
            print(False)
    else:
        print(False)

board =[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
check(board)