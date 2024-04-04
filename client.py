import socket
from threading import Thread

def check_input(message=''):
    stopped_msg = input(message)
    if stopped_msg in ['exit', '/stop']:
        exit()
    return stopped_msg

connection_active = True

def receive_messages():
    global connection_active
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            print(data)
        except (ConnectionRefusedError, ConnectionAbortedError, ConnectionResetError) as e:
            connection_active = False
            print(e)
            break

def send_message(conn, message):
    message = message.encode('utf-8')
    conn.send(message)

try:
    print("Для использования настроек по умолчанию ничего не вводите")
    host = check_input("Имя хоста: ")
    if not host:
        host = '127.0.1.1'
        print(f"Адрес хоста по умолчанию {host}")
    port = check_input(f"Введите порт для {host}: ")
    if not port:
        port = 9000
        print(f"Порт по умолчанию: {port}")
    else:
        port = int(port)
except ValueError:
    print("Неверно указан порт")

try:
    sock = socket.socket()
    sock.connect((host, port))
    print(f"Подключение к {host}:{port} прошло успешно\n")
except (socket.gaierror, ConnectionRefusedError) as e:
    print(f"Не удается подключиться к {host}:{port} ({e})!")

Thread(target=receive_messages, daemon=True).start()

while True:
    while True:
        message = check_input()
        if connection_active:
            send_message(sock, message)
        else:
            sock.close()
            break
