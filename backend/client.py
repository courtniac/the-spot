import asyncio
message = ""
def getInput():
    global message
    message = input("Pause, Play, or Next: ")
async def tcp_echo_client(loop):
    # while True:
    global message
    reader, writer = await asyncio.open_connection('2601:644:401:e9b0:69a3:4d4b:438:3dad', 8888, loop=loop)

    while True:

        getInput()
        print('Send: %r' % message)
        writer.write(message.encode())
        # await writer.drain()

        data = await reader.read(100)
        print('Received: %r' % data.decode())

    # writer.write(message.encode())
    #
    # data = await reader.read(100)
    # print('Received: %r' % data.decode())
    #
    # print('Close the socket')
    # writer.close()



loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(loop))
loop.close()