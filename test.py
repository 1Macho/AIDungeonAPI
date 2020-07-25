from aidadventure import AIDungeonAdventure
from aidclient import AIDungeonClient
import asyncio

async def callback(result):
    print(result)

async def blocking_task():
    while True:
        await asyncio.sleep(10)

async def main():
    aidc = await AIDungeonClient(debug=True)
    adventure = await aidc.connect_to_public_adventure('51e86616-507f-49f7-b07d-9a58b3261781')
    await adventure.register_actions_callback(callback)
    await asyncio.create_task(blocking_task())

asyncio.run(main())
