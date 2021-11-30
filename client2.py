import socket, threading
import cezar


nickname = input("Виберіть ім'я користувача: ")



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Ініціалізація сокета

client.connect(('192.168.0.109', 23435))  # З'єднання клієнта та сервера





def receive():
    s = input("a = decode, b = code")
    if s == "a":
        while True:  # Підтвердження з'єднання

            try:

                message = client.recv(1024).decode('utf-8')

                if message == 'NICKNAME':

                    client.send(nickname.encode('utf-8'))

                else:

                    print(cezar.cezar(message, -1))

            except:  # Якщо  неправильний іп

                print("Помилка!")

                client.close()

                break
    else:
        while True:  # Підтвердження з'єднання

            try:

                message = client.recv(1024).decode('utf-8')

                if message == 'NICKNAME':

                    client.send(nickname.encode('utf-8'))

                else:

                    print(message)

            except:  # Якщо  неправильний іп

                print("Помилка!")

                client.close()

                break




def write():

    while True:  # Вивід сповіщень

        message = cezar.cezar('{}: {}'.format(nickname, input()), 1) # Імпорт цезаря + крок
        client.send(message.encode('utf-8'))





receive_thread = threading.Thread(target=receive)  # Отримання сповіщень

receive_thread.start()

write_thread = threading.Thread(target=write)  # Відправка

write_thread.start()