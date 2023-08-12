import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def evaluate(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != "-":
            return 10 if row[0] == "X" else -10

    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] != "-" for row in range(3)):
            return 10 if board[0][col] == "X" else -10

    if all(board[i][i] == board[0][0] and board[0][0] != "-" for i in range(3)):
        return 10 if board[0][0] == "X" else -10

    if all(board[i][2 - i] == board[0][2] and board[0][2] != "-" for i in range(3)):
        return 10 if board[0][2] == "X" else -10

    return 0

def is_moves_left(board):
    return any(cell == "-" for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    best_score = max(best_score, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = "-"
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    best_score = min(best_score, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = "-"
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def find_best_move(board):
    best_move = (-1, -1)
    best_score = -math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = "X"
                move_score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = "-"

                if move_score > best_score:
                    best_score = move_score
                    best_move = (i, j)

    return best_move

def play_game():
    board = [["-" for _ in range(3)] for _ in range(3)]

    print("Tic-Tac-Toe - Human vs AI")
    print_board(board)

    while is_moves_left(board):
        row, col = find_best_move(board)
        board[row][col] = "X"
        print("AI's move:")
        print_board(board)

        if evaluate(board) == 10:
            print("AI wins!")
            return

        if not is_moves_left(board):
            print("It's a draw!")
            return

        user_row = int(input("Enter the row (0, 1, 2) for your move: "))
        user_col = int(input("Enter the column (0, 1, 2) for your move: "))

        while board[user_row][user_col] != "-":
            print("Invalid move. Try again.")
            user_row = int(input("Enter the row (0, 1, 2) for your move: "))
            user_col = int(input("Enter the column (0, 1, 2) for your move: "))

        board[user_row][user_col] = "O"
        print("Your move:")
        print_board(board)

        if evaluate(board) == -10:
            print("You win!")
            return

play_game()
