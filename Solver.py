from time import time
from math import sqrt
t = time()

size = 9
size2 = int(sqrt(size))
success = False

board = [[0]*size for _ in range(size)]

"""
board9 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""
"""
board16 =[[0, 12, 5, 11, 0, 7, 0, 0, 0, 0, 0, 14, 15, 0, 3, 0],
        [0, 0, 13, 0, 8, 0, 10, 15, 2, 4, 7, 0, 6, 5, 14, 11],
        [10, 0, 0, 3, 0, 2, 1, 14, 0, 5, 11, 0, 0, 0, 0, 9],
        [0, 2, 7, 0, 0, 11, 0, 0, 3, 0, 10, 0, 0, 4, 16, 13],
        [0, 8, 1, 0, 6, 12, 0, 0, 11, 0, 0, 13, 0, 16, 0, 0],
        [0, 0, 0, 15, 1, 0, 0, 0, 0, 0, 4, 0, 9, 11, 0, 7],
        [0, 0, 11, 4, 10, 0, 3, 2, 6, 1, 9, 7, 0, 13, 8, 12],
        [0, 13, 0, 0, 0, 0, 0, 5, 16, 10, 14, 15, 0, 1, 0, 0],
        [7, 0, 0, 0, 9, 1, 0, 4, 5, 0, 3, 10, 16, 0, 0, 0],
        [1, 11, 0, 0, 0, 0, 7, 8, 14, 13, 0, 0, 12, 9, 10, 0],
        [0, 0, 4, 10, 15, 14, 0, 0, 7, 12, 0, 2, 11, 8, 0, 6],
        [0, 14, 0, 0, 0, 10, 0, 11, 0, 6, 0, 0, 0, 7, 1, 2],
        [4, 0, 0, 1, 0, 0, 6, 10, 0, 0, 12, 9, 13, 0, 11, 0],
        [5, 0, 12, 6, 3, 4, 2, 0, 15, 0, 13, 0, 14, 0, 9, 0],
        [0, 10, 9, 0, 0, 0, 0, 16, 4, 0, 0, 0, 0, 0, 12, 0],
        [0, 0, 0, 0, 0, 8, 0, 9, 10, 0, 0, 0, 0, 3, 2, 1]]
"""


# function to check if a number in a position is valid
def check(x, y, number):
    global board, size, size2

    # checking row
    for n in range(size):
        if board[y][n] == number: return False

    # checking column
    for m in range(size):
        if board[m][x] == number: return False

    # checking subgrid
    x_offset = int(x / size2) * size2
    y_offset = int(y / size2) * size2

    for k in range(y_offset, y_offset + size2):
        for n in range(x_offset, x_offset + size2):
            if n == x and k == y: continue
            if board[k][n] == number: return False

    return True


def loop(x, y):
    global board, success, size
    if success: return

    if x > size-1:
        x = 0
        y += 1

    if y > size-1:
        success = True
        return

    while board[y][x] != 0:
        x += 1
        if x > size-1:
            x = 0
            y += 1

        if y > size-1:
            success = True
            return

    for number in range(1, size+1):
        if check(x, y, number):
            board[y][x] = number
            loop(x + 1, y)
            if success: return
    board[y][x] = 0


loop(0, 0)

# printing solved board
for row in range(size):
    print(board[row])

print("\nTime taken:", time()-t, "seconds")
