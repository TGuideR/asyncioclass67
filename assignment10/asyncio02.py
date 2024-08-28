# example of using an asyncio queue without blocking
from random import random
import asyncio
import time
 
# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    start_time = time.perf_counter()
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    end_time = time.perf_counter()
    print(f'Producer: Done in {end_time - start_time}')
 
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    start_time = time.perf_counter()
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    end_time = time.perf_counter()
    print(f'Consumer: Done in {end_time - start_time}')
 
# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue)) 
# start the asyncio program
asyncio.run(main())