import socket

from server import port

def _main():
    sock = socket.socket() #создание сокета
    sock.connect(('localhost', port)) #подключение к серверу
    print('Server connection')

    while 1:
        message = input('Input message:')
        if message == 'exit':
            break
        print(f'Sending to the server "{message}"')
        sock.send(message.encode())
        data = sock.recv(1024).decode()
        print(f'Came from the server "{data}"')
        print(data)

    sock.close() #закрытие сервера
    print('Server connection closed')


if __name__ == '__main__':
    _main()
