import unittest
from main import ChessBoard
import json

def simulate_games_from_json(json_file_path, chess_board, specified_game_id=None):
    """
    This function simulates games from a JSON file.
    
    Parameters:
    - json_file_path (str): The path to the JSON file containing game data.
    - chess_board (ChessBoard): An instance of the ChessBoard class where the game will be played.
    - specified_game_id (int, optional): If provided, only the game with this game_id will be simulated. Default is None.
    
    Usage:
    1. Create an instance of the ChessBoard class.
    2. Call this function, passing the path to the JSON file and the ChessBoard instance.
    3. Optionally, pass a specified_game_id to simulate a particular game.
    """
    with open(json_file_path, 'r') as file:
        data = json.load(file)  # Load game data from the JSON file

    for game in data['games']:  # Iterate through each game in the JSON data
        game_id = game['game_id']
        if specified_game_id is not None and game_id != specified_game_id:
            continue  # Skip games that don't match the specified game_id, if provided

        description = game.get('description', f'Game {game_id}')
        print(f'Simulating {description}')

        for move in game['moves']:  # Iterate through each move in the game
            if isinstance(move, dict):
                move_str = move['move']  # Extract move string if it's in a dictionary
            else:
                move_str = move  # Use the move string directly if it's not in a dictionary

            if not chess_board.handleMove(move_str):  # Handle each move on the chess board
                print(f'Invalid move: {move_str} in game {game_id}')
           
            chess_board.display()  # Display the board after each move

        print(f'Simulation of game {game_id} completed\n')
        break  # Exit after simulating the specified game or the first game if no game_id is specified


if __name__ == "__main__":
    # unittest.main() 
    chess_board = ChessBoard()  # Create an instance of the ChessBoard class
    simulate_games_from_json('testMoves.json', chess_board, specified_game_id=3)  # Simulate games from the specified JSON file
