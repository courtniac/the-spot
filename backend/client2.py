import asyncio


async def tcp_echo_client(message, loop):
    # while True:
    reader, writer = await asyncio.open_connection('', 8888,
                                                       loop=loop)
    # while True:
    print('Send: %r' % message)
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print('Received: %r' % data.decode())
    while True:
        data = await reader.read(100)
        print('Received: %r' % data.decode())
    # writer.write(message.encode())
    #
    # data = await reader.read(100)
    # print('Received: %r' % data.decode())
    #
    # print('Close the socket')
    # writer.close()


message = 'Hello World!'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
