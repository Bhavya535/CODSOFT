def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_score = float('-inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = create_board()
    while True:
        print_board(board)
        row, col = map(int, input("\nEnter your move (row and column): ").split())
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'X'
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = 'O'
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

play_game()
