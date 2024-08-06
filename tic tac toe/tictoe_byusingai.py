import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe with AI")

        self.current_player = 'X'  # Human starts as 'X'
        self.board = [None] * 9
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font=('Arial', 20), width=5, height=2,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def button_click(self, index):
        if not self.board[index] and not self.check_winner() and not self.is_board_full():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                self.show_winner(self.current_player)
            elif self.is_board_full():
                self.show_tie()
            else:
                self.current_player = 'O'
                self.ai_move()
                self.current_player = 'X'

    def ai_move(self):
        best_move = self.minimax(self.board, 'O')['index']
        self.board[best_move] = 'O'
        self.buttons[best_move].config(text='O')
        if self.check_winner():
            self.show_winner('O')
        elif self.is_board_full():
            self.show_tie()

    def minimax(self, board, player):
        available_moves = [i for i in range(9) if board[i] is None]

        if self.check_winner() == 'X':
            return {'score': -10}
        elif self.check_winner() == 'O':
            return {'score': 10}
        elif not available_moves:
            return {'score': 0}

        moves = []
        for move in available_moves:
            board[move] = player
            result = self.minimax(board, 'O' if player == 'X' else 'X')
            moves.append({'index': move, 'score': result['score']})
            board[move] = None

        if player == 'O':
            best_move = max(moves, key=lambda x: x['score'])
        else:
            best_move = min(moves, key=lambda x: x['score'])

        return best_move

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] and self.board[condition[0]] is not None:
                return self.board[condition[0]]
        return None

    def is_board_full(self):
        return all(cell is not None for cell in self.board)

    def show_winner(self, player):
        messagebox.showinfo("Game Over", f"Player {player} wins!")
        self.reset_game()

    def show_tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_game()

    def reset_game(self):
        self.current_player = 'X'
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeAI(root)
    root.mainloop()
