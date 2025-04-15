import asyncio

class Server:
    def __init__(self, ip = '127.0.0.1', socket_port = 8765):
        self.ip = ip
        self.socket_port = socket_port
        self.ws_reader = None
        self.ws_writer = None

    async def connect(self):
        self.ws_reader, self.ws_writer = await asyncio.open_connection(self.ip, self.socket_port)


    async def listen(self):
        while True:
            data = await self.ws_reader.read(1024)
            if not data:
                break
            print("Received:", data.decode().strip())

    async def start(self):

        while True:
            message = input("You: ")
            message = f"{message}\n"
            self.ws_writer.write(message.encode())
            await self.ws_writer.drain()