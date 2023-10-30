#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def print_solutions(solutions):
    for solution in solutions:
        print("[", end="")
        for i in range(len(solution)):
            print("[{}, {}]".format(i, solution[i]),
                  end=", " if i < len(solution) - 1 else "]\n")


def solve_nqueens(N):
    if N < 4:
        return
    board = [-1] * N
    solutions = []

    def solve(col):
        if col == N:
            solutions.append(list(board))
            return
        for row in range(N):
            if is_safe(board, row, col, N):
                board[col] = row
                solve(col + 1)
                board[col] = -1

    solve(0)
    print_solutions(solutions)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

solve_nqueens(N)
