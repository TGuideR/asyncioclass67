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
    print(pokemon['name'])

asyncio.run(main())