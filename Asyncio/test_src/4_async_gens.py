""""Воспроизведение асинхронного поведения спомощью генераторов"""
# Крнкуретность в python с 0 в Живую (Доклад на эту тему)
from select import select
import socket

# Лучше использовать очереди из метода Q, мы используем в примере просто список
tasks = []

to_read = {}
to_write = {}

# Сокет сервера
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #  Установть на каком хосте сервер 
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:

        yield ('read', server_socket)
        client_socket, addr = server_socket.accept() # Читает

        print("Connection", addr)

        tasks.append(client(client_socket))

# Сокет клиента
def client(client_socket):
    while True:

        yield ('read', client_socket)
        request = client_socket.recv(4096) # Читает

        if not request:
            break
        else:
            response = "Hi is ok\n".encode() # Пишет

            yield ('write', client_socket)
            client_socket.send(response)

    client_socket.close()

# Теперь пишем функцию которая асинхронно читает и пишет
# 1 Зачача, определить какие сокеты уже готовы для чтения и запеси и вызвать соот. методы (SELECT будем использовать)
# 2 Задача, нужен механизм переключания между функуиями server and clint

def event_loop():
    # any() принемает список значений которые дают false или true, если хоть один равен true any() вернет нам значение
    while any([tasks, to_read, to_write]):

        while not tasks:
            # передали три списка, [] это список с ошибками
            # select заберед нужные сокеты и распакует и в эти списки ready_to_read, ready_to_write
            ready_to_read, ready_to_write, _  = select(to_read, to_write, [])
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task) # ('write', client_socet)

            if reason == "read":
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Все готово')


tasks.append(server())




