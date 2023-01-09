from original import server_socket
from select import select
import socket

#Переменная для мониторинга
to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

#Функция принемает серверны socket
def accept_connection(server_socket):

    client_socket, addr = server_socket.accept()
    print("Connection", addr)
    to_monitor.append(client_socket)


# Функция принемает клиентский soket
def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = "Hi is ok".encode()
        client_socket.send(response)
    else:
        client_socket.close()


#Функция гавная которая запускает осталные функции
def event_loop():
    while True:
        #select  работает с любыми типов обектов у которых есть fileno(),  который возвращает фаиловый дискриптор
        #select следит за состаяниями сокетамив когда они станут доступны: Записи, отправки, ожидает ошибки
        #передаем три списка, если пкстое начение ставим _
        ready_to_read, _, _ = select(to_monitor, [], []) #Записи, отправки, ошибки

        #Обработка в цикле
        for sock in ready_to_read:
            if sock in server_socket:
                accept_connection(sock)
            else:
                send_message(sock)

if __name__ == "_main_":
    to_monitor.append(server_socket)
    accept_connection(server_socket)
    event_loop()