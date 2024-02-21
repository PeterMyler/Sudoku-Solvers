from time import time
from math import sqrt, prod
import numpy as np
from copy import deepcopy
t = time()
def printArray(arr): print("\n".join(map(str, arr)))


size = 16  # height/width of board
size2 = int(sqrt(size))  # height/width of sub-grids
success = False  # global bool, indicates if board has been solved
possibles = [[[] for j in range(size)] for i in range(size)]
board = [[0 for _ in range(size)] for __ in range(size)]
CSP_arr = []
CSP_LIMIT = 35

"""
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 4, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 6, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
"""
"""
board = [[0, 0, 0, 1, 0, 2, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [2, 0, 0, 0, 8, 0, 0, 0, 1],
        [0, 0, 9, 0, 0, 0, 8, 0, 5],
        [0, 7, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 3, 0, 4, 0, 0, 0]]
"""
"""
board = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]]
"""

boards = [[[0, 5, 4, 11, 0, 8, 0, 0, 12, 0, 9, 7, 2, 1, 0, 0],
           [0, 9, 0, 7, 0, 1, 11, 14, 0, 0, 0, 0, 0, 4, 0, 16],
           [0, 0, 15, 0, 9, 5, 0, 16, 2, 1, 0, 14, 0, 7, 0, 0],
           [16, 14, 1, 2, 7, 0, 15, 4, 5, 0, 0, 0, 0, 0, 9, 10],
           [9, 6, 12, 0, 8, 7, 0, 0, 10, 0, 1, 0, 15, 0, 4, 14],
           [4, 0, 0, 0, 3, 0, 0, 0, 0, 13, 0, 0, 5, 0, 0, 6],
           [2, 15, 5, 14, 10, 9, 12, 0, 11, 4, 0, 16, 0, 0, 0, 0],
           [8, 10, 11, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 12],
           [0, 0, 3, 0, 0, 6, 0, 2, 0, 11, 10, 0, 12, 16, 0, 13],
           [10, 0, 0, 0, 0, 0, 4, 3, 0, 0, 16, 0, 9, 14, 11, 7],
           [0, 12, 0, 0, 0, 16, 0, 11, 0, 0, 3, 1, 10, 8, 0, 0],
           [14, 0, 0, 15, 12, 0, 10, 9, 0, 0, 0, 6, 0, 5, 0, 3],
           [0, 3, 2, 9, 13, 4, 0, 7, 0, 10, 0, 11, 0, 12, 0, 0],
           [0, 4, 6, 5, 16, 0, 0, 12, 1, 0, 13, 0, 11, 15, 0, 0],
           [0, 13, 0, 8, 0, 0, 0, 1, 3, 9, 12, 0, 16, 6, 0, 4],
           [0, 16, 14, 12, 15, 10, 0, 8, 7, 0, 5, 0, 0, 2, 0, 0]],
          [[0, 12, 5, 11, 0, 7, 0, 0, 0, 0, 0, 14, 15, 0, 3, 0],
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
           [0, 0, 0, 0, 0, 8, 0, 9, 10, 0, 0, 0, 0, 3, 2, 1]],
          [[0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 8, 1, 12, 0, 0, 14],
           [0, 0, 14, 0, 0, 0, 0, 0, 4, 0, 0, 0, 15, 5, 6, 0],
           [0, 0, 11, 0, 1, 0, 0, 10, 0, 0, 14, 15, 0, 2, 0, 16],
           [0, 0, 0, 3, 12, 0, 4, 0, 0, 7, 0, 5, 0, 13, 0, 10],
           [0, 0, 0, 10, 8, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 5],
           [0, 14, 0, 11, 0, 0, 0, 0, 0, 9, 0, 0, 10, 7, 15, 4],
           [0, 15, 13, 0, 0, 9, 5, 3, 14, 2, 0, 7, 8, 0, 0, 0],
           [8, 2, 0, 0, 0, 4, 0, 0, 16, 0, 10, 0, 14, 6, 3, 9],
           [0, 8, 1, 0, 13, 5, 0, 0, 0, 0, 0, 0, 11, 14, 0, 3],
           [4, 0, 0, 5, 14, 2, 0, 8, 0, 16, 15, 12, 0, 0, 0, 0],
           [14, 13, 0, 2, 0, 0, 15, 0, 10, 11, 0, 0, 4, 0, 0, 0],
           [0, 16, 12, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 1, 0, 15],
           [0, 5, 0, 8, 4, 3, 0, 0, 0, 0, 0, 6, 16, 11, 0, 0],
           [0, 3, 0, 0, 5, 1, 14, 0, 15, 12, 0, 16, 0, 9, 0, 0],
           [9, 1, 0, 14, 7, 0, 16, 13, 0, 0, 11, 4, 0, 0, 5, 0],
           [0, 0, 15, 0, 9, 8, 0, 0, 0, 0, 0, 14, 1, 3, 0, 0]],
          [[0, 13, 0, 15, 1, 0, 6, 0, 0, 0, 0, 0, 0, 9, 0, 0],
           [0, 7, 0, 16, 11, 0, 13, 3, 0, 14, 2, 0, 0, 0, 5, 8],
           [11, 0, 3, 0, 0, 8, 0, 5, 0, 9, 16, 0, 6, 0, 0, 0],
           [14, 0, 0, 0, 0, 0, 15, 12, 0, 1, 10, 5, 0, 16, 0, 2],
           [0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 12, 0, 10, 15],
           [0, 9, 0, 3, 0, 0, 12, 0, 7, 0, 0, 14, 0, 5, 0, 0],
           [0, 8, 0, 11, 0, 0, 9, 0, 0, 10, 0, 12, 7, 0, 4, 0],
           [0, 0, 0, 0, 0, 0, 7, 0, 5, 6, 0, 0, 9, 0, 0, 0],
           [7, 3, 0, 2, 9, 0, 0, 4, 0, 0, 11, 0, 0, 8, 0, 14],
           [0, 0, 6, 0, 0, 3, 0, 2, 0, 0, 0, 0, 13, 11, 12, 0],
           [12, 11, 8, 0, 0, 14, 0, 0, 2, 0, 0, 7, 0, 0, 3, 0],
           [16, 0, 0, 13, 0, 11, 10, 0, 0, 5, 0, 3, 0, 1, 9, 0],
           [9, 1, 5, 0, 0, 0, 0, 6, 0, 0, 3, 0, 0, 13, 11, 10],
           [8, 0, 0, 0, 0, 4, 3, 1, 0, 0, 0, 15, 0, 12, 16, 0],
           [13, 0, 0, 0, 0, 15, 14, 0, 4, 2, 0, 0, 0, 0, 0, 3],
           [0, 16, 0, 0, 0, 0, 11, 0, 9, 0, 0, 6, 0, 0, 0, 0]],
          [[0, 12, 0, 10, 0, 0, 0, 5, 0, 0, 0, 0, 0, 13, 0, 0],
           [0, 0, 0, 0, 2, 0, 0, 16, 0, 0, 0, 12, 1, 0, 15, 7],
           [14, 13, 2, 0, 7, 11, 4, 0, 0, 10, 0, 15, 0, 0, 0, 0],
           [3, 0, 16, 0, 0, 0, 14, 8, 0, 0, 0, 0, 11, 0, 5, 0],
           [1, 2, 3, 7, 0, 0, 15, 14, 0, 0, 0, 0, 10, 0, 12, 11],
           [5, 0, 0, 0, 0, 0, 11, 10, 0, 0, 2, 14, 0, 0, 0, 8],
           [0, 10, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 2],
           [6, 8, 14, 0, 0, 16, 2, 12, 10, 3, 0, 7, 5, 0, 13, 0],
           [10, 0, 0, 0, 6, 7, 5, 0, 11, 0, 12, 3, 15, 0, 0, 14],
           [0, 9, 0, 0, 0, 8, 3, 0, 0, 16, 0, 4, 13, 12, 0, 0],
           [8, 0, 13, 12, 0, 14, 0, 11, 1, 0, 15, 0, 0, 5, 7, 0],
           [0, 14, 0, 16, 0, 12, 0, 0, 2, 0, 5, 8, 9, 0, 0, 0],
           [4, 0, 0, 0, 0, 0, 10, 3, 0, 0, 1, 0, 0, 7, 0, 0],
           [2, 0, 0, 0, 0, 0, 1, 0, 14, 0, 10, 0, 0, 0, 0, 5],
           [0, 11, 0, 0, 0, 0, 0, 0, 16, 4, 3, 0, 0, 0, 0, 13],
           [0, 0, 0, 14, 8, 5, 0, 0, 0, 0, 0, 0, 4, 0, 2, 1]],
          [[0, 3, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 10, 0, 0, 1, 0, 2, 6, 16, 0, 0, 0, 11, 12, 4],
           [0, 0, 9, 0, 4, 0, 14, 10, 0, 1, 0, 0, 5, 2, 0, 7],
           [12, 0, 0, 1, 0, 0, 0, 0, 10, 0, 0, 14, 0, 0, 0, 15],
           [4, 8, 0, 13, 2, 10, 3, 16, 0, 0, 6, 0, 0, 9, 11, 1],
           [0, 0, 0, 12, 0, 14, 13, 0, 0, 15, 4, 0, 0, 0, 0, 3],
           [0, 0, 14, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
           [2, 0, 0, 6, 0, 0, 15, 7, 9, 3, 16, 0, 0, 12, 4, 13],
           [0, 7, 0, 5, 0, 0, 0, 4, 0, 0, 0, 9, 13, 0, 15, 11],
           [0, 1, 0, 0, 7, 0, 16, 0, 0, 0, 0, 6, 12, 8, 3, 14],
           [0, 6, 0, 0, 0, 0, 8, 15, 13, 0, 2, 0, 7, 0, 5, 0],
           [13, 15, 16, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 1, 0],
           [0, 0, 13, 9, 0, 2, 0, 6, 0, 8, 15, 5, 11, 0, 7, 0],
           [0, 2, 0, 4, 3, 0, 5, 0, 14, 0, 12, 0, 0, 6, 13, 0],
           [7, 0, 0, 0, 0, 0, 0, 14, 3, 0, 0, 16, 0, 1, 0, 5],
           [0, 5, 6, 8, 0, 0, 0, 9, 0, 0, 7, 0, 0, 0, 14, 0]]]

board = boards[5]


# returns the y position of an element in a 2d array
def findIn2dArray(arr, num):
    for y in range(len(arr)):
        if num in arr[y]:
            return y
    return -1


# returns the x, y position of an element in a 3d array
def findIn3dArray(arr, num):
    for y in range(len(arr)):
        x = findIn2dArray(arr[y], num)
        if x != -1:
            return x, y
    return -1


# counts occurrences of a number in a 2d array
def countNum2d(arr, num):
    return sum([row.count(num) for row in arr])


# counts occurrences of a number in a 3d array
def countNum3d(arr, num):
    s = 0
    for y in range(len(arr)):
        s += sum([col.count(num) for col in arr[y]])
    return s


# checks if a number in a position is valid (2d array)
def check(x, y, num):
    global board

    # checking row
    for n in range(size):
        if board[y][n] == num: return False
        if board[n][x] == num: return False

    # checking sub-grid
    x_of = (x // size2) * size2
    y_of = (y // size2) * size2
    for m in range(y_of, y_of + size2):
        for n in range(x_of, x_of + size2):
            if y == m and x == n: continue
            if board[m][n] == num: return False
    return True


# main backtracking function
def loop(x, y):
    global board, success, possibles, size, size2
    if success: return

    if x > size - 1:
        x, y = 0, y + 1
    if y > size - 1:
        success = True
        return
    while board[y][x] != 0:
        x += 1
        if x > size - 1:
            x, y = 0, y + 1
        if y > size - 1:
            success = True
            return

    save_pos = possibles[y][x].copy()
    for number in save_pos:
        if check(x, y, number):
            board[y][x] = number
            possibles[y][x] = [number]

            loop(x + 1, y)
            if success: return

    possibles[y][x] = save_pos
    board[y][x] = 0


# eliminate posses with the help of naked pairs, triples, etc.
def naked_pairs(arr):
    global hasChanged, board

    for cell in arr:
        poss_count = sum([len(_) for _ in arr])
        if arr.count(cell) > 1 and arr.count(cell) == len(cell) and poss_count > 18:
            for poss in arr:
                if poss != cell:
                    for num in cell:
                        if num in poss:
                            poss.remove(num)
                            hasChanged = True


# "brute-force" find all permutations of possibilities in a cage/row/column
def CSP_loop(curr_arr, posses, i):
    global CSP_arr

    if i >= len(posses):
        # check if its valid
        for num in range(1, size + 1):
            if curr_arr.count(num) != 1: return

        CSP_arr.append(curr_arr.copy())
        return

    for pos in posses[i]:
        curr_arr[i] = pos
        CSP_loop(curr_arr, posses, i + 1)


# create new board with every possible number in every cell
for j in range(size):
    for i in range(size):
        if board[j][i] == 0:
            for num in range(1, size + 1):
                if check(i, j, num):
                    possibles[j][i].append(num)
            if len(possibles[j][i]) == 1:
                board[j][i] = possibles[j][i][0]
        else:
            possibles[j][i] = [board[j][i]]

poss_nums = sum([len(x) for y in range(size) for x in possibles[y]]) - size * size
print("Before:", poss_nums)

runs = 0
hasChanged = True

printArray(possibles)
print()

# array of all coordinates with unknown values
toCheck = [[x, y] for x in range(size) for y in range(size) if board[y][x] == 0]
while hasChanged:
    hasChanged = False
    runs += 1

    ## naked singles
    for x, y in toCheck:
        if len(possibles[y][x]) == 1:
            # if only one possible number in a cell - add it to the main board
            if board[y][x] == 0:
                board[y][x] = possibles[y][x][0]
                toCheck.remove([x, y])
                hasChanged = True
            number = possibles[y][x][0]

            # remove number from possibles in the same
            # row, column
            for n in range(size):
                if n != x and number in possibles[y][n]:
                    possibles[y][n].remove(number)
                    hasChanged = True
                if n != y and number in possibles[n][x]:
                    possibles[n][x].remove(number)
                    hasChanged = True

            # subgrid
            x_of = (x // size2) * size2
            y_of = (y // size2) * size2
            for m in range(y_of, y_of + size2):
                for n in range(x_of, x_of + size2):
                    if y == m and x == n: continue
                    if number in possibles[m][n]:
                        possibles[m][n].remove(number)
                        hasChanged = True

    ## hidden singles:
    # rows
    for row in range(size):
        for num in range(1, size + 1):
            if countNum2d(possibles[row], num) == 1:
                col = findIn2dArray(possibles[row], num)
                if possibles[row][col] != [num]:
                    possibles[row][col] = [num]
                    board[row][col] = num
                    hasChanged = True
    # columns
    for col in range(size):
        for num in range(1, size + 1):
            full_col = [possibles[_][col] for _ in range(size)]

            if countNum2d(full_col, num) == 1:
                row = findIn2dArray(full_col, num)
                if possibles[row][col] != [num]:
                    possibles[row][col] = [num]
                    board[row][col] = num
                    hasChanged = True
    # cages
    for y in range(0, size, size2):
        for x in range(0, size, size2):
            cage = [rows[x:x + size2] for rows in possibles[y:y + size2]]

            ## hidden singles
            for num in range(1, size + 1):
                if countNum3d(cage, num) == 1:
                    col, row = findIn3dArray(cage, num)
                    if possibles[row + y][col + x] != [num]:
                        possibles[row + y][col + x] = [num]
                        board[row + y][col + x] = num
                        hasChanged = True

    ## naked pairs:
    # rows
    for row in range(size):
        naked_pairs(possibles[row])
    # columns
    for col in range(size):
        col_arr = [possibles[_][col] for _ in range(size)]
        naked_pairs(col_arr)
    # cages
    for y in range(0, size, size2):
        for x in range(0, size, size2):
            cage = [rows[x:x + size2] for rows in possibles[y:y + size2]]

            flattened_cage = []
            for _ in cage: flattened_cage.extend(_)
            naked_pairs(flattened_cage)

    ## do CSP (brute-force possibilities to find consistent cases) for:
    # rows
    for row in range(size):
        posses = possibles[row]
        # limit CSP to only run for groups of less than 34 possibilities
        poss_nums = sum([len(_) for _ in posses])
        if poss_nums > CSP_LIMIT: continue

        CSP_arr = []
        CSP_loop([0].copy() * size, posses, 0)

        # test to see if any element is always the same
        for i in range(size):
            if len(posses[i]) == 1: continue

            tester = True
            value = CSP_arr[0][i]
            for perm in CSP_arr:
                if perm[i] != value:
                    tester = False
                    break

            if tester:
                possibles[row][i] = [value]
                board[row][i] = value
                hasChanged = True
    # columns
    for col in range(size):
        # limit CSP to only run for groups of less than 34 possibilities
        col_arr = [possibles[_][col] for _ in range(size)]

        poss_nums = sum([len(_) for _ in col_arr])
        if poss_nums > CSP_LIMIT: continue

        CSP_arr = []
        CSP_loop([0].copy() * size, col_arr, 0)

        # test to see if any element is always the same
        for j in range(size):
            if len(possibles[j][col]) == 1: continue

            tester = True
            value = CSP_arr[0][j]
            for perm in CSP_arr:
                if perm[j] != value:
                    tester = False
                    break
            if tester:
                possibles[j][col] = [value]
                board[j][col] = value
                hasChanged = True
    # cages
    for y in range(0, size, size2):
        for x in range(0, size, size2):
            cage = [rows[x:x + size2] for rows in possibles[y:y + size2]]

            flattened_cage = []
            for _ in cage: flattened_cage.extend(_)

            poss_nums = sum([len(_) for _ in flattened_cage])
            if poss_nums > CSP_LIMIT: continue

            CSP_arr = []
            CSP_loop([0].copy() * size, flattened_cage, 0)

            # test to see if any element is always the same
            for j in range(size):
                real_x = (j % size2) + x
                real_y = (j // size2) + y

                if len(possibles[real_y][real_x]) == 1: continue

                tester = True
                value = CSP_arr[0][j]
                for perm in CSP_arr:
                    if perm[j] != value:
                        tester = False
                        break
                if tester:
                    possibles[real_y][real_x] = [value]
                    board[real_y][real_x] = value
                    hasChanged = True

    ## intersection:
    # rows and cages
    for row_n in range(size):
        for cage_n in range(size2):
            red_part = [possibles[row_n][:cage_n * size2], possibles[row_n][(cage_n + 1) * size2:]]

            purple_part = [possibles[row_n][cage_n * size2:(cage_n + 1) * size2]]

            k1 = (row_n // size2) * size2
            k2 = k1 + (row_n % size2)
            blue_part = [_[cage_n * size2:(cage_n + 1) * size2] for _ in possibles[k1:k2]]
            blue_part.extend([_[cage_n * size2:(cage_n + 1) * size2] for _ in possibles[k2 + 1:k1 + size2]])

            # more normal way:
            # blue_part = []
            # for new_row_n in range((row_n // size2) * size2, (row_n // size2 + 1) * size2):
            #     if new_row_n == row_n: continue
            #     blue_part.append(possibles[new_row_n][cage_n * size2:(cage_n + 1) * size2])

            for num in range(1, size + 1):
                if countNum3d(purple_part, num) > 0 == countNum3d(blue_part, num):
                    for m in red_part:
                        for n in m:
                            if num in n:
                                n.remove(num)
                                hasChanged = True
    # columns and cages
    for col_n in range(size):
        for cage_n in range(size2):
            col_arr = [possibles[_][col_n] for _ in range(size)]
            red_part = [col_arr[:cage_n * size2], col_arr[(cage_n + 1) * size2:]]

            purple_part = [col_arr[cage_n * size2:(cage_n + 1) * size2]]

            # get blue part
            blue_part = []
            for new_col_n in range((col_n // size2) * size2, (col_n // size2 + 1) * size2):
                if new_col_n == col_n: continue
                curr_coll_arr = [possibles[_][new_col_n] for _ in range(size)]
                blue_part.append(curr_coll_arr[cage_n * size2:(cage_n + 1) * size2])

            for num in range(1, size + 1):
                if countNum3d(purple_part, num) > 0 == countNum3d(blue_part, num):
                    for m in red_part:
                        for n in m:
                            if num in n:
                                n.remove(num)
                                hasChanged = True

    ## X-wing
    if hasChanged: continue
    for row_n1 in range(size):
        for row_n2 in range(row_n1+1, size):
            # skip rows that affect the same cages
            if row_n1 // size2 == row_n2 // size2: continue
            for col_n1 in range(size):
                for col_n2 in range(col_n1+1, size):
                    # skip columns that affect the same cages
                    if col_n1 // size2 == col_n2 // size2: continue

                    # rows (blue)
                    row_parts = []
                    for new_row_n in [row_n1, row_n2]:
                        for l, r in [(0, col_n1), (col_n1 + 1, col_n2), (col_n2 + 1, size)]:
                            a = possibles[new_row_n][l:r]
                            if a: row_parts.extend(a)

                    # cols (red)
                    column_parts = []
                    for new_row_n in range(size):
                        if new_row_n == row_n1 or new_row_n == row_n2: continue
                        column_parts.append(possibles[new_row_n][col_n1])
                        column_parts.append(possibles[new_row_n][col_n2])

                    # centres (purple)
                    centre_parts = []
                    for new_row_n in [row_n1, row_n2]:
                        for new_col_n in [col_n1, col_n2]:
                            centre_parts.append(possibles[new_row_n][new_col_n])

                    # cols as reds
                    for num in range(1, size + 1):
                        if countNum2d(centre_parts, num) > 0 == countNum2d(row_parts, num):
                            for n in column_parts:
                                if num in n:
                                    n.remove(num)
                                    hasChanged = True
                    # rows as reds
                    for num in range(1, size + 1):
                        if countNum2d(centre_parts, num) > 0 == countNum2d(column_parts, num):
                            for n in row_parts:
                                if num in n:
                                    n.remove(num)
                                    hasChanged = True


poss_nums = sum([len(x) for y in range(size) for x in possibles[y]]) - size * size
print("After:", poss_nums)
print("Run throughs:", runs)

printArray(possibles)

# start backtracking if needed
if countNum2d(board, 0) > 0:
    print("\nBacktracking...")
    loop(0, 0)
else:
    print("\nSkipping backtracking...")

# printing solved board
print("\nSolved board:")
printArray(board)
# # print out possible with cages visually separated
# for i, row in enumerate(possibles):
#     for col in row:
#         print(col, end=" "*(size*2-len(str(col))))
#
#     print()
#     if (i+1)%size2==0: print("\n")

print("\nTime taken:", time() - t, "seconds")

finalCheck = True
for j in range(size):
    for i in range(size):
        value = board[j][i]
        board[j][i] = 0
        if not check(i, j, value):
            finalCheck = False
        board[j][i] = value

print("Result validator:", finalCheck)
