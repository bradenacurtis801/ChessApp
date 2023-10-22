import unittest
from main import ChessBoard
import json
import sys


ORANGE = '\033[41m'
COLOR = '\033[91m'
RESET_COLOR = '\033[0m'
class DuplicateGameIDError(Exception):
    """Custom exception for duplicate game IDs."""
    pass

def check_duplicate_game_ids(json_file_path):
    """Checks for duplicate game IDs in the data and raises an error if duplicates are found."""
    game_ids = {}

    with open(json_file_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if '"game_id"' in line:
                # Extract the game_id value from the line
                try:
                    game_id_key, game_id_value = line.split(":")
                    game_id = int(game_id_value.strip().rstrip(","))
                    
                    if game_id in game_ids:
                        error_msg = (f"Error: Duplicate game_id: {game_id} found!\n"
                                     f"Lines {game_ids[game_id]} and {line_number} have the same game_id value: {game_id}\n"
                                     f"Content from line {game_ids[game_id]}: {line}\n"
                                     f"Content from line {line_number}: {line}\n")
                        raise DuplicateGameIDError(error_msg)
                    else:
                        game_ids[game_id] = line_number
                except ValueError:
                    print(f"Error parsing game_id on line {line_number}.")



def simulate_game(game, chess_board):
    """Simulates a single game on the given chess board."""
    game_id = game['game_id']
    description = game.get('description', f'Game {game_id}')
    print(f'{COLOR}<--- Simulating: {description} --->{RESET_COLOR}')
    for move in game['moves']:
        if isinstance(move, dict):
            move_str = move['move']
        else:
            move_str = move

        chess_board.handleMove(move_str)
        if not chess_board.result['status']:
            print(f'Invalid move: {move_str} in game {game_id}')

        chess_board.display()
    print(f'Simulation of game {game_id} completed\n')

def simulate_games_from_json(json_file_path, chess_board, specified_game_id=None):
    # First, check for duplicate game IDs
    # Usage:
    check_duplicate_game_ids(json_file_path)
        
    # If no duplicates are found, load the JSON data to simulate games
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for game in data['games']:
        game_id = game['game_id']
        if specified_game_id is None or game_id == specified_game_id:
            simulate_game(game, chess_board)
            break



if __name__ == "__main__":
    try:
        # unittest.main() 
        chess_board = ChessBoard()  # Create an instance of the ChessBoard class
        simulate_games_from_json('testMoves.json', chess_board, specified_game_id=3)  # Simulate games from the specified JSON file
    except SystemExit as e:
        print(e)