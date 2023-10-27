import tkinter as tk
from tkinter import simpledialog
import tkinter as tk
from tkinter import messagebox
import json
from LargeInputDialog import LargeInputDialog


class ChessBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Board")
        self.geometry("400x400")

        self.setup_variables()
        self.setup_controls()
        self.setup_board()
        self.setup_headers()

    def setup_variables(self):
        self.selected_piece = None
        self.selected_position = None
        self.moves = []
        self.turn = "Red"  # Red goes first

    def setup_controls(self):
        self.finish_button = tk.Button(
            self, text="Finish", command=self.on_finish_click)
        self.finish_button.grid(row=11, column=1, columnspan=4, sticky='nsew')

        self.restart_button = tk.Button(
            self, text="Restart", command=self.on_restart_click)
        self.restart_button.grid(row=11, column=5, columnspan=4, sticky='nsew')

    def setup_board(self):
        self.initial_setup = self.get_initial_setup()
        self.buttons = [[tk.Button(self, command=lambda i=i, j=j: self.on_cell_click(
            i, j)) for j in range(8)] for i in range(8)]
        for i, row in enumerate(self.buttons):
            for j, button in enumerate(row):
                piece_obj = self.initial_setup[i][j]
                button_text = piece_obj.name if piece_obj else ""
                button.config(text=button_text,
                              fg=piece_obj.team if piece_obj else 'black')
                button.grid(row=i+1, column=j+1, sticky='nsew')

        for i in range(8):
            self.grid_rowconfigure(i+1, weight=1)
            self.grid_columnconfigure(i+1, weight=1)

    def setup_headers(self):
        for i in range(1, 9):
            label_left = tk.Label(self, text=str(9-i))
            label_left.grid(row=i, column=0, sticky='nsew')
            label_right = tk.Label(self, text=str(9-i))
            label_right.grid(row=i, column=9, sticky='nsew')

        for j, letter in enumerate("ABCDEFGH"):
            label_top = tk.Label(self, text=letter)
            label_top.grid(row=0, column=j+1, sticky='nsew')
            label_bottom = tk.Label(self, text=letter)
            label_bottom.grid(row=10, column=j+1, sticky='nsew')

    def get_initial_setup(self):
        return [
            [piece("Rook", "Blue"), piece("Knight", "Blue"), piece("Bishop", "Blue"), piece("Queen", "Blue"), piece(
                "King", "Blue"), piece("Bishop", "Blue"), piece("Knight", "Blue"), piece("Rook", "Blue")],
            [piece("Pawn", "Blue") for _ in range(8)],
        ] + [[None for _ in range(8)] for _ in range(4)] + [
            [piece("Pawn", "Red") for _ in range(8)],
            [piece("Rook", "Red"), piece("Knight", "Red"), piece("Bishop", "Red"), piece("Queen", "Red"), piece(
                "King", "Red"), piece("Bishop", "Red"), piece("Knight", "Red"), piece("Rook", "Red")]
        ]

    def on_finish_click(self):
        # Ask the user if they want to save the game simulation
        result = messagebox.askyesno("Save Game", "Do you want to save this game simulation to the JSON file?")

        # If user selects 'Yes'
        if result:
            # Prompt the user for a description using the custom dialog
            dialog = LargeInputDialog(self, title="Description", prompt="Please describe your test case")
            description = dialog.user_input
            if description is None:  # If user clicked "Cancel"
                description = ""  # Default to an empty string

            # 1. Read the existing content of the JSON file
            with open('testMoves.json', 'r') as file:
                data = json.load(file)
                games = data['games']

            # 2. Compute the next game ID
            max_game_id = max(game['game_id'] for game in games)
            next_game_id = max_game_id + 1

            # Create the new game data
            new_game = {
                "game_id": next_game_id,
                "description": description,
                "status": "",
                "moves": self.moves
            }

            # 4. Append the new game to the existing games
            games.append(new_game)

            # 5. Write the updated content back to the JSON file
            with open('testMoves.json', 'w') as file:
                json.dump(data, file, indent=4)

        # Close the GUI
        # self.destroy()
        self.on_restart_click()
        return

    def on_restart_click(self):
        # Reset variables
        self.setup_variables()

        # Update the board state
        self.setup_board()

    def on_cell_click(self, i, j):
        cell_piece = self.initial_setup[i][j]

        if self.selected_piece:
            # If the same piece is clicked again or another piece of the same color is clicked, deselect the current piece
            if cell_piece and cell_piece.team == self.turn:
                self.deselect_current_piece()
                # If a different piece of the same color is clicked, select it
                if (i, j) != self.selected_position:
                    self.select_piece(cell_piece, i, j)
                return

            self.perform_move(i, j)
            self.switch_turn()
        elif cell_piece and cell_piece.team == self.turn:
            self.select_piece(cell_piece, i, j)

    def deselect_current_piece(self):
        if self.selected_position:
            i, j = self.selected_position
            # Reset the background color to default
            self.buttons[i][j].config(bg='SystemButtonFace')
        self.selected_piece = None
        self.selected_position = None

    def perform_move(self, i, j):
        dest = chr(j + ord('A')) + str(8 - i)
        start = chr(
            self.selected_position[1] + ord('A')) + str(8 - self.selected_position[0])
        self.moves.append({"move": f"{start}-{dest}"})
        self.initial_setup[i][j] = self.selected_piece
        self.initial_setup[self.selected_position[0]
                           ][self.selected_position[1]] = None
        self.buttons[i][j]['text'] = self.selected_piece.name
        self.buttons[i][j]['fg'] = 'red' if self.selected_piece.team == "Red" else 'blue'
        self.buttons[self.selected_position[0]
                     ][self.selected_position[1]]['text'] = ""
        self.buttons[self.selected_position[0]
                     ][self.selected_position[1]]['fg'] = 'black'

        # Reset the background color of the original position
        self.buttons[self.selected_position[0]
                     ][self.selected_position[1]].config(bg='SystemButtonFace')

        self.selected_piece = None
        self.selected_position = None

    def switch_turn(self):
        self.turn = "Blue" if self.turn == "Red" else "Red"

    def select_piece(self, cell_piece, i, j):
        if self.selected_position:  # If another piece is already selected, deselect it
            self.deselect_current_piece()
        self.selected_piece = cell_piece
        self.selected_position = (i, j)
        # Change the background color to indicate selection
        self.buttons[i][j].config(bg='lightgray')

    def get_moves(self):
        return {
            "game_id": None,
            "description": "",
            "status": "Not tested yet",
            "moves": self.moves
        }


class piece:
    def __init__(self, name, team):
        self.name = name
        self.team = team


if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.mainloop()

    data = chess_board.get_moves()

    # Indent each move with 11 spaces, then join them with ",\n"
    moves_str = ",\n".join(
        "       " + json.dumps(move, separators=(',', ': ')) for move in data['moves'])
    data['moves'] = "REPLACE_ME"  # Temporary placeholder
    base_data_str = json.dumps(data, indent=4, separators=(',', ': '))

    # Replace the placeholder with the formatted moves string
    formatted_json = base_data_str.replace(
        '"REPLACE_ME"', f'[\n{moves_str}\n    ]')
    print(formatted_json)
