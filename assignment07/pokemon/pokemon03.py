import asyncio
import json
import aiofiles

pokemonapi_directory = 'C:\\Users\\User\\OneDrive\\Desktop\\My Works\\2567_1\\Asynchronous Coding\\AsyncCode\\asyncioclass67\\assignment07\\pokemon\\pokemonapi'
pokemonmove_directory = 'C:\\Users\\User\\OneDrive\\Desktop\\My Works\\2567_1\\Asynchronous Coding\\AsyncCode\\asyncioclass67\\assignment07\\pokemon\\pokemonmove'


async def main():
    # Read the contents of json file.
    async with aiofiles.open(f'{pokemonapi_directory}\\articuno.json', mode='r') as f:
        contents = await f.read()

    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]
    
    # Open a new file to write the list of moves into.
    async with aiofiles.open(f'{pokemonmove_directory}\\{name}_move.txt', mode='w') as f:
        await f.write('\n'.join(moves))

asyncio.run(main())