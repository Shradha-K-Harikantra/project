import random

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Check if the given player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def get_available_moves(board):
    """Return a list of available moves."""
    return [i for i, spot in enumerate(board) if spot == ' ']

def ai_move(board):
    """AI makes a random move."""
    available_moves = get_available_moves(board)
    if available_moves:
        return random.choice(available_moves)
    return None

def main():
    board = [' '] * 9
    player = 'X'
    ai = 'O'
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    while True:
        if player == 'X':
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if board[move] == ' ':
                    board[move] = player
                else:
                    print("Invalid move. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Enter a number between 1 and 9.")
                continue
        else:
            move = ai_move(board)
            if move is not None:
                board[move] = ai
            else:
                print("It's a draw!")
                break

        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break
        elif check_winner(board, ai):
            print(f"Player {ai} wins!")
            break
        elif not get_available_moves(board):
            print("It's a draw!")
            break

        # Switch players
        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
1