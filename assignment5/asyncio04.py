# example of waiting for the first task to fail
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')

async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(20)]
    # wait for all taks to complete
    done, pending = await asyncio.wait(tasks, timeout=0.52)
    print('All done')

# start the asyncio program
asyncio.run(main())