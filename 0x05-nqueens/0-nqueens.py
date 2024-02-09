#!/usr/bin/python3
'''The N queens puzzle is the challenge'''
import sys


def check_forQueen(b, row, col):
    '''check if there is a queen present'''
    for i in range(row):
        if b[i] == col:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if b[i] == j:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(b))):
        if b[i] == j:
            return False
    return True


def solve(b, row, n):
    '''solve the queen problem'''
    if row == n:
        print(b)
        return

    for col in range(n):
        if check_forQueen(b, row, col):
            b[row] = col
            solve(b, row + 1, n)
            b[row] = -1


def nqueens(N):
    '''the main'''
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
