# Chess Exhibition
import time


opponent = 3
pair_move = 30
judit_move = 0.1
opponent_move = 0.5

def board(pair_move, judit, opponent): 
    for move in range(1, pair_move+1):
        print(f'Judit move his {move} move.')
        time.sleep(judit)
        print(f'Opponent move his {move} move.')
        time.sleep(opponent)

def game(num_oppo):
    for game in range(1, num_oppo+1):
        start_game = time.perf_counter()
        print(f'Game {game} start.')
        board(pair_move, judit_move, opponent_move)
        game_end = time.perf_counter() - start_game
        print(f"Game {game} end in {game_end} seconds.")

        
start_exhibition = time.perf_counter()
game(opponent)
elapsed = time.perf_counter() - start_exhibition
print(f'{time.ctime()} - exhibition end in {elapsed} seconds.')