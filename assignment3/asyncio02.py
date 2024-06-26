# example of running a coroutine
import asyncio
#define a coroutine
async def custom_coro():
    #await another coroutine
    await asyncio.sleep(5)
    # print('Done')

# main coroutine
async def main():
    # execute my custom coroutine
    await custom_coro()
    # print('Wait a sec')
    # await asyncio.sleep(3)
    # print('Custom done so I am')

# start the coroutine program
asyncio.run(main())
