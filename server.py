import socket
port = 3456

def _main():
    sock = socket.socket() #запуск сервера
    sock.bind(('', port)) #подключение к порту
    print('Server start')
    sock.listen() #подключение прослушки
    print('Port listening:', port)
    connection, address = sock.accept() #получение порта и адреса
    print('Client connection:', address)

    while 1:
        data = connection.recv(1024)
        if not data:
            break
        decoded = data.decode()
        print(f'Came from a client "{decoded}"')
        connection.send(data)
        print('Message sent successfully')

    connection.close() #закрытие подключение сокетов
    print('Disabling a client', address)
    sock.close() #закрытие сервера
    print('Server shutdown')


if __name__ == '__main__':
    _main()
