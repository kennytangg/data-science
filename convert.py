import chess.pgn
import csv

def convert_pgn_to_csv(pgn_file, output_csv):
    games_data = []
    
    with open(pgn_file, 'r', encoding='utf-8') as f:
        game_count = 0
        
        while True:
            game = chess.pgn.read_game(f)
            if game is None:
                break
            
            headers = game.headers
            
            # Extract ALL moves from the game
            board = game.board()
            moves = []
            for move in game.mainline_moves():
                moves.append(board.san(move))
                board.push(move)
            
            # Join all moves as space-separated string
            all_moves = " ".join(moves) if moves else ""
            
            # Extract game data
            game_data = {
                'Event': headers.get('Event', ''),
                'Site': headers.get('Site', ''),
                'Date': headers.get('Date', ''),
                'Round': headers.get('Round', ''),
                'White': headers.get('White', ''),
                'Black': headers.get('Black', ''),
                'Result': headers.get('Result', ''),
                'ECO': headers.get('ECO', ''),
                'WhiteElo': headers.get('WhiteElo', ''),
                'BlackElo': headers.get('BlackElo', ''),
                'PlyCount': headers.get('PlyCount', ''),
                'EventDate': headers.get('EventDate', ''),
                'EventType': headers.get('EventType', ''),
                'Moves': all_moves
            }
            
            games_data.append(game_data)
            game_count += 1
            
            if game_count % 10000 == 0:
                print(f"Processed {game_count:,} games...")
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Event', 'Site', 'Date', 'Round', 'White', 'Black', 
                      'Result', 'ECO', 'WhiteElo', 'BlackElo', 'PlyCount', 
                      'EventDate', 'EventType', 'Moves']
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(games_data)
    
if __name__ == "__main__":
    convert_pgn_to_csv('data/lichess_elite_2024_full.pgn', 'data/chess_games_raw.csv')
