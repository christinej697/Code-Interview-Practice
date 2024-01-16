import math

# rotate nxn matrix 90 degrees clockwise
def rotate_matrix_bad(matrix) -> None:
    n = len(matrix)

    row_list = []
    for i in range(n):
        # grab the rows
        row_list.append(matrix[i])

    # each i row must become column at n-i
    for row in row_list:
        pass

def rotate_matrix(matrix) -> None:
    n = len(matrix)-1
    layers = len(matrix)//2
    start = 0
    # code to move through all layers
    for j in range(layers):
        # code to rotate a layer
        for i in range(start,n):
            replace = matrix[j][i]
            second_replace = matrix[i][n]
            matrix[i][n] = replace
            third_replace = matrix[n][n-i+j]
            matrix[n][n-i+j] = second_replace
            fourth_replace = matrix[n-i+j][j]
            matrix[n-i+j][j] = third_replace
            matrix[j][i] = fourth_replace
        print(matrix)
        n -= 1
        start += 1

if __name__ == "__main__":
    # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    matrix = [[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]
    print(matrix)
    rotate_matrix(matrix)
    print(matrix)
