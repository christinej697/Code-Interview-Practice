# Given an mxn integer matrix, if an element is 0, set its entire row and column to 0's
def setZeroes(matrix) -> None:
    m = len(matrix)
    n = len(matrix[0])
    index = []
    num_of_zeroes = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                index.extend([i,j])
                num_of_zeroes += 1

    print(index)
    # if as many zeroes as greatest length, whole array will be zeroes
    if (i >= max(m,n)):
        for i in range(m):
            for j in range(n):
                matrix[i][j] = 0
    for k in range(num_of_zeroes):
        i = index[k*2]
        j = index[k*2+1]
        for l in range(n):
            matrix[i][l] = 0
        for l in range(m):
            print(l,",",j)
            matrix[l][j] = 0




if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix)
    print(matrix, "\n")

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setZeroes(matrix)
    print(matrix)
