"""Уже примеры асинхроной работы"""

import selectors
import socket
from original import server_socket


selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()
    #register принемает 3 аргумента: фаиловый обект, событие котоое интресует, любые связанные данные
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)

#Функция принемает серверны socket
def accept_connection(server_socket):

    client_socket, addr = server_socket.accept()
    print("Connection", addr)
    # register принемает 3 аргумента: фаиловый обект, событие котоое интресует, любые связанные данные
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)



# Функция принемает клиентский soket
def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = "Hi is ok".encode()
        client_socket.send(response)
    else:
        #register снимаем с регистрации
        selector.unregister(client_socket)
        client_socket.close()


#Функция гавная которая запускает осталные функции
def event_loop():
    while True:
        #Выборка обьектов готовых для чтения и записи
        events = selector.select() #key, events
        # SelectorKey принемает 3 аргумента: фаиловый обект, событие котоое интресует, любые связанные данные
        # достаем только key, events(_) сейчас нам не нужны
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)





if __name__ == "_main_":
    server()
    event_loop()