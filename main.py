import tkinter as tk
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.current_player = 'X'
        self.game_mode = tk.IntVar()
        self.statistics = {"Player 1 Wins": 0, "Player 2 Wins": 0, "Ties": 0}
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        self.mode_label = tk.Label(self.window, text="Choose game mode:")
        self.mode_label.grid(row=0, column=0, columnspan=3)
        
        self.pvp_button = tk.Radiobutton(self.window, text="Player vs. Player", variable=self.game_mode, value=1)
        self.pvp_button.grid(row=1, column=0, columnspan=3)
        
        self.pvc_button = tk.Radiobutton(self.window, text="Player vs. Computer", variable=self.game_mode, value=2)
        self.pvc_button.grid(row=2, column=0, columnspan=3)
        
        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        self.start_button.grid(row=3, column=0, columnspan=3)
        
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text=self.board[i], width=10, height=3, command=lambda i=i: self.make_move(i))
            button.grid(row=(i//3)+4, column=i%3)
            self.buttons.append(button)
        
        self.status_label = tk.Label(self.window, text="", fg="red")
        self.status_label.grid(row=7, column=0, columnspan=3)
        
        self.stats_label = tk.Label(self.window, text=self.get_statistics_text())
        self.stats_label.grid(row=8, column=0, columnspan=3)
        
    def get_statistics_text(self):
        return f"Player 1 Wins: {self.statistics['Player 1 Wins']}\nPlayer 2 Wins: {self.statistics['Player 2 Wins']}\nTies: {self.statistics['Ties']}"

    def start_game(self):
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.current_player = 'X'
        self.update_board()
        self.status_label.config(text="")

    def update_board(self):
        for i, button in enumerate(self.buttons):
            button.config(text=self.board[i])
    
    def make_move(self, index):
        if self.board[index] not in ['X', 'O']:
            self.board[index] = self.current_player
            if self.check_win():
                self.status_label.config(text=f"Player {self.current_player} wins!")
                self.update_statistics(self.current_player)
                self.update_board()
                return
            if self.check_tie():
                self.status_label.config(text="It's a tie!")
                self.update_statistics(None)
                self.update_board()
                return
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.update_board()
            if self.game_mode.get() == 2 and self.current_player == 'O':
                self.make_computer_move()
                
    def make_computer_move(self):
        available_moves = [i for i in range(9) if self.board[i] not in ['X', 'O']]
        move = random.choice(available_moves)
        self.make_move(move)
    
    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] in ['X', 'O']:
                return True
        return False
    
    def check_tie(self):
        return all(cell in ['X', 'O'] for cell in self.board)
    
    def update_statistics(self, winner):
        if winner == 'X':
            self.statistics["Player 1 Wins"] += 1
        elif winner == 'O':
            self.statistics["Player 2 Wins"] += 1
        else:
            self.statistics["Ties"] += 1
        self.stats_label.config(text=self.get_statistics_text())

if __name__ == "__main__":
    TicTacToe()
