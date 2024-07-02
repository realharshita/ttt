def initialize_board():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return board

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] not in ['X', 'O']:
                return move
            else:
                print("Invalid move. Please enter a valid position.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return True
    return False

def check_tie(board):
    return all(cell in ['X', 'O'] for cell in board)

if __name__ == "__main__":
    board = initialize_board()
    print_board(board)
    
    current_player = 1
    while not check_win(board) and not check_tie(board):
        player_move = get_player_move(board, current_player)
        board[player_move] = 'X' if current_player == 1 else 'O'
        print_board(board)
        
        current_player = 2 if current_player == 1 else 1
    
    if check_win(board):
        print(f"Player {current_player} wins!")
    else:
        print("It's a tie!")
