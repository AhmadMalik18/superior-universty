# Topic 15: Backtracking

# Task 1: Solving the N-Queens Problem Using Backtracking


def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if a queen can be placed at board[row][col]
        for i in range(row):
            if board[i][col] == 'Q':  # Check column
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':  # Check left diagonal
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == 'Q':  # Check right diagonal
                return False
        return True

    def solve(row):
        if row == n:
            # Convert board to a list of strings and add to solutions
            solutions.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'  # Place queen
                solve(row + 1)  # Recur to place the next queen
                board[row][col] = '.'  # Backtrack

    # Initialize the board and solutions list
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(0)
    return solutions

# Example usage
n = 4
solutions = solve_n_queens(n)
for idx, solution in enumerate(solutions, 1):
    print(f"Solution {idx}:")
    for row in solution:
        print(row)
    print()



# Task 2: Generating All Possible Permutations of a String


# Task 2: Generating All Possible Permutations of a String

def permute(string):
    def backtrack(start):
        if start == len(chars):
            # Add the current permutation to the result
            permutations.append(''.join(chars))
            return
        for i in range(start, len(chars)):
            # Swap characters at indices start and i
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)  # Recur for the next character
            # Backtrack (undo the swap)
            chars[start], chars[i] = chars[i], chars[start]

    # Convert the string to a list of characters
    chars = list(string)
    permutations = []
    backtrack(0)
    return permutations

# Example usage
string = "ABC"
permutations = permute(string)
print("All permutations of the string:")
print(permutations)





# Task 3: Solving the Sudoku Puzzle Using Backtracking

def solve_sudoku(board):
    def is_valid(num, row, col):
        # Check if num can be placed at board[row][col]
        # Check the row
        if num in board[row]:
            return False
        # Check the column
        if num in [board[i][col] for i in range(9)]:
            return False
        # Check the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # Find an empty cell
                    for num in range(1, 10):  # Try numbers 1-9
                        if is_valid(num, row, col):
                            board[row][col] = num  # Place the number
                            if backtrack():  # Recur to solve the rest
                                return True
                            board[row][col] = 0  # Backtrack
                    return False  # No valid number found, trigger backtracking
        return True  # Puzzle solved

    backtrack()
    return board

# Example usage
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solved_board = solve_sudoku(sudoku_board)
print("Solved Sudoku Board:")
for row in solved_board:
    print(row)