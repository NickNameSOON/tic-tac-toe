import random
import tkinter as tk
from tkinter import messagebox

# Function to create an empty 3x3 board
def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# Function to check for a winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if [board[i][col] for i in range(3)].count(player) == 3:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to handle player's move
def handle_player_move(row, col):
    global player_turn, game_board

    if game_board[row][col] == ' ':
        game_board[row][col] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED)
        player_turn = False

        if check_winner(game_board, 'X'):
            messagebox.showinfo('GAME OVER', 'Ви перемогли !')
            reset_game()
        elif all(cell != ' ' for row in game_board for cell in row):
            messagebox.showinfo('GAME OVER', 'Нічия!')
            reset_game()
        else:
            handle_computer_move()

# Function to handle computer's move
def handle_computer_move():
    global player_turn, game_board

    available_moves = [(row, col) for row in range(3) for col in range(3) if game_board[row][col] == ' ']
    row, col = random.choice(available_moves)
    game_board[row][col] = 'O'
    buttons[row][col].config(text='O', state=tk.DISABLED)
    player_turn = True

    if check_winner(game_board, 'O'):
        messagebox.showinfo('GAME OVER', 'Комп`ютер переміг !')
        reset_game()
    elif all(cell != ' ' for row in game_board for cell in row):
        messagebox.showinfo('GAME OVER', 'Нічия!')
        reset_game()

# Function to reset the game
def reset_game():
    global player_turn, game_board

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', state=tk.NORMAL)
            game_board[row][col] = ' '

    if not player_turn:
        handle_computer_move()

# Create the main window
window = tk.Tk()
window.title('Tic Tac Toe')

# Create the game board
game_board = create_board()

# Create the buttons for each cell
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=' ', width=10, height=5, command=lambda r=row, c=col: handle_player_move(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Variable to keep track of player's turn
player_turn = True

# Start the game
reset_game()

# Run the main event loop
window.mainloop()
