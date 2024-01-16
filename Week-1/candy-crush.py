def candyCrush(board) -> None:
    crushCandies(board)
    flag = dropCandies(board)
    while flag:
        flag = dropCandies(board)

# function to crush any 3+ horizontal/vertical adjacent candies across board
def crushCandies(board) -> bool:
    marked = []
    # from top left to bottom right by row
    for i in range(len(board)):
        for j in range(len(board[0])):
            # if a cell is empty, don't need to check for adjecents
            if board[i][j] != 0:
                # check 3 to right
                if j < (len(board[0]) - 2):
                    if board[i][j] == board[i][j+1] == board[i][j+2]:
                        marked.extend([[i,j],[i,j+1],[i,j+2]])
                # check 3 below
                if i < (len(board) - 2):
                    if board[i][j] == board[i+1][j] == board[i+2][j]:
                        marked.extend([[i,j],[i+1,j],[i+2,j]])
    # remove duplicates from marked set
    #marked = set(marked)
    for index in marked:
        board[index[0]][index[1]] = 0
    print("Crushed:", board)
    if len(marked) == 0:
        return False
    return True

# function to drop remaining candies vertically into empty cells
def dropCandies(board) -> bool:
    # from bottom left to top right by column
    for j in range(len(board[0])):
        for i in reversed(range(len(board))):
            offset = 1
            if board[i][j] == 0:
                while board[i - offset][j] == 0:
                    # if only non empty peices above, move to next column
                    if i - offset < 0:
                        break
                    offset += 1
                if i - offset < 0:
                    break
                board[i][j] = board[i-offset][j]
                board[i-offset][j] = 0
    print("dropped:",board)
    # crush any adjecent candies on resulting board
    flag = crushCandies(board)
    return flag


if __name__ == "__main__":
    board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
    candyCrush(board)
    print("Completed", board, "\n")

    board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
    candyCrush(board)
    print("Completed", board)
