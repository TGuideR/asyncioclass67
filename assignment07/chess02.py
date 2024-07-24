# Chess Exhibition
import time
import asyncio


opponent = 24
pair_move = 30
judit_move = 0.1
opponent_move = 0.5

async def board(game, pair_move, judit, opponent):
    start_game = time.perf_counter()
    print(f'Game {game} start.')

    for move in range(1, pair_move+1):
        time.sleep(judit)
        print(f'Judit made a move in game {game}.')
        await asyncio.sleep(opponent)
        print(f'Opponent {game} made a move in game {game}.')

    game_end = time.perf_counter() - start_game
    print(f"Game {game} end in {game_end} seconds.")

async def main(num_oppo):
    coros = [board(g, pair_move, judit_move, opponent_move) for g in range(1, num_oppo+1)]
    await asyncio.gather(*coros)
        

        
start_exhibition = time.perf_counter()
asyncio.run(main(opponent))
elapsed = time.perf_counter() - start_exhibition
print(f'{time.ctime()} - exhibition end in {elapsed} seconds.')