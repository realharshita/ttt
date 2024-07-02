import random

def initialize_board():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return board

def print_board(board):
    print("\n")
    print("Tic-Tac-Toe")
    print("============")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

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

def get_computer_move(board):
    available_moves = [i for i in range(9) if board[i] not in ['X', 'O']]
    return random.choice(available_moves)

def check_win(board):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] in ['X', 'O']:
            return True
    return False

def check_tie(board):
    return all(cell in ['X', 'O'] for cell in board)

def choose_game_mode():
    while True:
        try:
            mode = int(input("Choose game mode:\n1. Player vs. Player\n2. Player vs. Computer\nEnter 1 or 2: "))
            if mode in [1, 2]:
                return mode
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    board = initialize_board()
    print_board(board)
    
    game_mode = choose_game_mode()
    current_player = 1
    
    while not check_win(board) and not check_tie(board):
        if game_mode == 1:
            player_move = get_player_move(board, current_player)
            board[player_move] = 'X' if current_player == 1 else 'O'
        else:
            if current_player == 1:
                player_move = get_player_move(board, current_player)
                board[player_move] = 'X'
            else:
                computer_move = get_computer_move(board)
                board[computer_move] = 'O'
        
        print_board(board)
        current_player = 2 if current_player == 1 else 1
    
    if check_win(board):
        print(f"Player {current_player} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
