def solve_n_queens(N):
    board = [-1] * N 
    solutions = []
    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or \
               abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True
    def solve(row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1 
    solve(0)
    return solutions
def print_solutions(solutions, N):
    for index, sol in enumerate(solutions):
        print(f"\nSolution {index + 1}:")
        for row in range(N):
            line = ""
            for col in range(N):
                if sol[row] == col:
                    line += " Q "
                else:
                    line += " . "
            print(line)
    print(f"\nTotal Solutions: {len(solutions)}")
N = 5
solutions = solve_n_queens(N)
print_solutions(solutions, N)
