import unittest
from main import ChessBoard
import json
import sys

# Color codes to display text in different colors in the terminal
ORANGE = '\033[41m'
COLOR = '\033[91m'
RESET_COLOR = '\033[0m'

class DuplicateGameIDError(Exception):
    """Custom exception raised when duplicate game IDs are detected in the JSON data."""
    pass

def check_duplicate_game_ids(json_file_path):
    """Checks for duplicate game IDs in the JSON data and raises a custom exception if duplicates are found.

    Args:
        json_file_path (str): Path to the JSON file containing the game data.
    """
    game_ids = {}  # Dictionary to store unique game IDs

    with open(json_file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if '"game_id"' in line:
                try:
                    game_id_key, game_id_value = line.split(":")
                    game_id = int(game_id_value.strip().rstrip(","))
                    
                    # Check if the game_id is already present in the dictionary
                    if game_id in game_ids:
                        # If it is, then it's a duplicate and raise an error
                        error_msg = (f"Error: Duplicate game_id: {game_id} found!\n"
                                     f"Lines {game_ids[game_id]} and {line_number} have the same game_id value: {game_id}\n"
                                     f"Content from line {game_ids[game_id]}: {line}\n"
                                     f"Content from line {line_number}: {line}\n")
                        raise DuplicateGameIDError(error_msg)
                    else:
                        # Otherwise, add the game_id to the dictionary
                        game_ids[game_id] = line_number
                except ValueError:
                    # This will be triggered if parsing the game_id fails
                    print(f"Error parsing game_id on line {line_number}.")

def simulate_game(game, chess_board):
    """Simulates a single chess game on a given chess board.

    Args:
        game (dict): A dictionary containing game details and moves.
        chess_board (ChessBoard): An instance of the ChessBoard class.
    """
    game_id = game['game_id']
    description = game.get('description', f'Game {game_id}')
    print(f'{COLOR}<--- Simulating: {description} --->{RESET_COLOR}')
    
    # Iterate through the moves and apply them to the chess board
    for move in game['moves']:
        # The move might be a dictionary or a simple string
        if isinstance(move, dict):
            move_str = move['move']
        else:
            move_str = move

        chess_board.handleMove(move_str)
        # If the move is invalid, display an error
        if not chess_board.result['status']:
            print(f'Invalid move: {move_str} in game {game_id}')

        chess_board.display()
    
    print(f'Simulation of game {game_id} completed\n')
    
    # Reset the chess board for the next game
    chess_board.__init__()

def simulate_games_from_json(json_file_path, chess_board, specified_game_id=None):
    """Loads game data from a JSON file and simulates them on a given chess board.

    Args:
        json_file_path (str): Path to the JSON file containing the game data.
        chess_board (ChessBoard): An instance of the ChessBoard class.
        specified_game_id (int, optional): Game ID of a specific game to simulate. If not specified, all games in the JSON will be simulated.
    """
    # First, check for duplicate game IDs to ensure data integrity
    check_duplicate_game_ids(json_file_path)
        
    # Load the JSON data from the file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Simulate each game in the loaded JSON data
    for game in data['games']:
        game_id = game['game_id']
        if specified_game_id is None or game_id == specified_game_id:
            simulate_game(game, chess_board)
            break  # Stop simulating after the specified game ID if provided

if __name__ == "__main__":
    try:
        chess_board = ChessBoard()  # Create an instance of the ChessBoard class
        # Simulate games using data from the specified JSON file and a particular game ID (in this case, game_id=4)
        simulate_games_from_json('testMoves.json', chess_board, specified_game_id=4)
    except SystemExit as e:
        print(e)
