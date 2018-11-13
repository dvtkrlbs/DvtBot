from gino import Gino
import asyncio

db = Gino()


async def setup():
    await db.set_bind('postgresql://localhost/discord')

asyncio.get_event_loop().run_until_complete(setup())