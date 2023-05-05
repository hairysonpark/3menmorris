import copy

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Get all valid moves for the current player
def get_valid_moves(board, player_positions):
    moves = []

    # If the player has not placed all 3 pieces yet
    if len(player_positions) < 3:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    moves.append((i, j))
    else:
        # If the player has all 3 pieces on the board, consider moves for each piece
        for x, y in player_positions:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (dx == 0) != (dy == 0):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 3 and 0 <= ny < 3 and board[nx][ny] == '-':
                            moves.append(((x, y), (nx, ny)))

    return moves

# Check if a player has won the game
def check_win(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Evaluate the board state
def evaluate(board):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    return 0

# Minimax algorithm with alpha-beta pruning
def minimax(board, player_positions, opponent_positions, depth, maximizing_player, alpha, beta):
    if depth == 0 or check_win(board, 'X') or check_win(board, 'O'):
        return evaluate(board), None

    moves = get_valid_moves(board, player_positions)
    best_move = None

    if maximizing_player:
        max_eval = float('-inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            new_player_positions = copy.deepcopy(player_positions)

            # Update the board and player positions
            if len(player_positions) < 3:
                new_board[move[0]][move[1]] = 'X'
                new_player_positions.append(move)
            else:
                new_board[move[0][0]][move[0][1]] = '-'
                new_board[move[1][0]][move[1][1]] = 'X'
                new_player_positions.remove(move[0])
                new_player_positions.append(move[1])

            # Recursive call
            eval, _ = minimax(new_board, opponent_positions, new_player_positions, depth - 1, False, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in moves:
            new_board = copy.deepcopy(board)
            new_player_positions = copy.deepcopy(player_positions)

            # Update the board and player positions
            if len(player_positions) < 3:
                new_board[move[0]][move[1]] = 'O'
                new_player_positions.append(move)
            else:
                new_board[move[0][0]][move[0][1]] = '-'
                new_board[move[1][0]][move[1][1]] = 'O'
                new_player_positions.remove(move[0])
                new_player_positions.append(move[1])

            # Recursive call
            eval, _ = minimax(new_board, opponent_positions, new_player_positions, depth - 1, True, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def main():
    board = [['-' for _ in range(3)] for _ in range(3)]
    player_positions = []
    opponent_positions = []
    player_turn = True

    while not check_win(board, 'X') and not check_win(board, 'O') and (get_valid_moves(board, player_positions) or get_valid_moves(board, opponent_positions)):
        print_board(board)
        if player_turn:
            if len(player_positions) < 3:
                row, col = map(int, input("Enter your move (row col): ").split())
                if board[row][col] == '-':
                    board[row][col] = 'X'
                    player_positions.append((row, col))
                    player_turn = not player_turn
                else:
                    print("Invalid move. Try again.")
            else:
                old_row, old_col, new_row, new_col = map(int, input("Enter your move (old_row old_col new_row new_col): ").split())
                if (old_row, old_col) in player_positions and board[new_row][new_col] == '-':
                    board[old_row][old_col] = '-'
                    board[new_row][new_col] = 'X'
                    player_positions.remove((old_row, old_col))
                    player_positions.append((new_row, new_col))
                    player_turn = not player_turn
                else:
                    print("Invalid move. Try again.")
        else:
            _, best_move = minimax(board, opponent_positions, player_positions, 3, False, float('-inf'), float('inf'))
            if len(opponent_positions) < 3:
                board[best_move[0]][best_move[1]] = 'O'
                opponent_positions.append(best_move)
            else:
                board[best_move[0][0]][best_move[0][1]] = '-'
                board[best_move[1][0]][best_move[1][1]] = 'O'
                opponent_positions.remove(best_move[0])
                opponent_positions.append(best_move[1])
            player_turn = not player_turn

    print_board(board)

    if check_win(board, 'X'):
        print("Player wins!")
    elif check_win(board, 'O'):
        print("Computer wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
