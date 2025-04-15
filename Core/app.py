import asyncio

from Core import Server


class Application:
    def __init__(self):
        self.server = None
        self.setup()



    def setup(self):
        # first we need to setup the server
        self.server = Server()



    async def run(self):
        await self.server.connect()
        asyncio.create_task(self.server.listen())
        await self.server.start()

