# Set up the board
board = [["-" for _ in range(8)] for _ in range(8)]
board[0][0] = "R"
board[0][1] = "N"
board[0][2] = "B"
board[0][3] = "Q"
board[0][4] = "K"
board[0][5] = "B"
board[0][6] = "N"
board[0][7] = "R"
board[1][0] = "P"
board[1][1] = "P"
board[1][2] = "P"
board[1][3] = "P"
board[1][4] = "P"
board[1][5] = "P"
board[1][6] = "P"
board[1][7] = "P"
board[6][0] = "p"
board[6][1] = "p"
board[6][2] = "p"
board[6][3] = "p"
board[6][4] = "p"
board[6][5] = "p"
board[6][6] = "p"
board[6][7] = "p"
board[7][0] = "r"
board[7][1] = "n"
board[7][2] = "b"
board[7][3] = "q"
board[7][4] = "k"
board[7][5] = "b"
board[7][6] = "n"
board[7][7] = "r"

# Print the board
for row in board:
    print(" ".join(row))

# Handle a move
def move(start, end):
    # Check if the start position is valid
    if start[0] < 0 or start[0] > 7 or start[1] < 0 or start[1] > 7:
        return False
    if board[start[0]][start[1]] == "-":
        return False
    
    # Check if the end position is valid
    if end[0] < 0 or end[0] > 7 or end[1] < 0 or end[1] > 7:
        return False
    
    # Make the move
    board[end[0]][end[1]] = board[start[0]][start[1]]
    board[start[0]][start[1]] = "-"
    return True

# Test the move function
move((0, 0), (0, 1))
move((1, 0), (2, 0))

# Print the board again to see the result of the moves
for row in board:
    print(" ".join(row))