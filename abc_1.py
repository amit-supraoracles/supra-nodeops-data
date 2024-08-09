import asyncio
import websockets

URI = "wss://127.0.0.1:8000"  # Replace with your WebSocket server URI
NUM_REQUESTS = 10
MESSAGE = "Hello, WebSocket!"

async def send_messages():
    try:
        async with websockets.connect(URI) as websocket:
            for i in range(NUM_REQUESTS):
                await websocket.send(MESSAGE)
                response = await websocket.recv()
                print(f"Response: {response}")
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(send_messages())
