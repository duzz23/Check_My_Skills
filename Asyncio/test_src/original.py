import socket

#Сервер для обслуживания клиента(который принемает значение)
#SOCK_STREAM говорио о что соеденение TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#после таймаута по новому использовать метод
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Привязка к домену и порту
server_socket.bind(('localhost', 5000))
#Метод прослуштвания на ходячие подключения
server_socket.listen()
# клиент и сервер подключение через безконечного цикла
while True:
    print("находимся перед методом accept")
    #Сервер клиентский(который отправляет значения)
    client_socket, addr = server_socket.accept()
    print("Connection", addr)
    # Ожидание от клиента сообщения
    while True:
        print("находимся перед методом recv")
        #размер сообщения recv(4096)
        request = client_socket.recv(4096)

        # Условия для приревания цикла
        if not request:
            break
        else:
            #Ответ если сообщение принято
            response = "Hi is ok".encode()
            client_socket.send(response)

#python3 original.py
"""Метод send тоже можно назвать блокируншей операцией, пока клиент что то не пришлет. Любая функция пока не выполниться будет блокировать результат"""