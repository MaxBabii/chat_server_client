import socket, threading


host = '192.168.0.109'
port = 23435

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


def broadcast(message):  # Функция связи
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:  #Отримання сповіщень
            message = client.recv(1024)
            broadcast(message)
        except:  # Видалення клієнтів
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{}!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():  # Підключення декількох юзерів
    while True:
        client, address = server.accept()
        print("З'єднаний з {}".format(str(address)))
        client.send('NICKNAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print("Нік користувача {}".format(nickname))
        #broadcast("{}".format(nickname).encode('utf-8'))
        #client.send('!'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()