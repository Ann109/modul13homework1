import time
import asyncio


async def start_strongman(name, power):
        count_balls = 5
        print(f'Силач {name} начал соревнования.')
        for ball in range(count_balls):
                await asyncio.sleep(power) #После поставьте каждую задачу в ожидание (await)
                print(f'Силач {name} поднял шар номер {ball + 1}')
        print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    player1 = asyncio.create_task(start_strongman('Pasha', 3))
    player2 = asyncio.create_task(start_strongman('Denis', 4))
    player3 = asyncio.create_task(start_strongman('Apollon', 5))
    await player1
    await player2
    await player3


asyncio.run(start_tournament())