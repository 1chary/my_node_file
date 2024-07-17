m, n = map(int,input().split())
matrix = []
a = []

for i in range(m):
    inputs = input().split()
    matrix.append(inputs)

def get_rectangle_area(matrix,row,column,width,height):
    count = 0 
    for r in range(row,row + height):
        for c in range(column,column + width):
            if matrix[r][c] == "X":
                count += 1 
            else:
                return 0
    return count

for row in range(m):
    for column in range(n):
        if matrix[row][column] == "X":
            no_of_rows_possible = m-row
            no_of_columns_possible = n-column
            for width in range(1,no_of_columns_possible+1):
                for height in range(1,no_of_rows_possible+1):
                    rectangle_area = get_rectangle_area(matrix,row,column,width,height)
                    a.append(rectangle_area)

if len(a) == 0:
    print(0)
else:
    print(max(a))
                
                
                
                
                
                