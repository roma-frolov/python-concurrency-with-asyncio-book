# Реализация неблокирующих сокетов с неограниченным количеством подключений, использующая систему уведомлений ОС;
# Имитация цикла событий

import selectors
import socket


selector = selectors.DefaultSelector()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events = selector.select(timeout=1)

    if len(events) == 0:
        print('Событий нет, подожду еще!')

    for event, _ in events:
        event_socket = event.fileobj

        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'Получен запрос на подключение от {address}')
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f'Получены данные: {data}')
            event_socket.send(data)
