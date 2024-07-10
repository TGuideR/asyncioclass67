# นักศึกษา A อยากกินข้าวไว ๆ ขอจานแรกที่เสร็จ
from random import random
import asyncio

# ทำข้าวผัด
async def fried_rice():
    # generate a random value between 0 and 1
    value = random() + 1
    # block for a moment
    print(f'Microwave (Fried Rice): cooking {value} sec...')
    await asyncio.sleep(value)
    # report the value
    print(f'Fried Rice Finish cooking')

async def noodle():
    # generate a random value between 0 and 1
    value = random() + 1
    # block for a moment
    print(f'Microwave (Noodle): cooking {value} sec...')
    await asyncio.sleep(value)
    # report the value
    print(f'Noodle Finish cooking')

async def curry():
    # generate a random value between 0 and 1
    value = random() + 1
    # block for a moment
    print(f'Microwave (Curry): cooking {value} sec...')
    await asyncio.sleep(value)
    # report the value
    print(f'Curry Finish cooking')

async def main():
    meal1 = asyncio.create_task(fried_rice(), name='Fried Rice')
    meal2 = asyncio.create_task(noodle(), name='Noodle')
    meal3 = asyncio.create_task(curry(), name='Curry')
    meal = [meal1, meal2, meal3]
    done, pending = await asyncio.wait(meal, return_when=asyncio.FIRST_COMPLETED)
    for x in done:
        first_complete= x.get_name()
    print(f'นักศึกษา A ได้กิน {first_complete} แล้ว')
    print(f'Complete task: {len(done)}.')
    print(f'\t- {first_complete} is complete')
    print(f'Uncomplete task: {len(pending)}')
asyncio.run(main())