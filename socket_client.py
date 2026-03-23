import socket

def client_connect_func(address):
    client = socket.socket()
    client.connect(address)
    message = "GET / HTTP/1.1\r\nHost: www.python.org\r\nConnection: close\r\n\r\n"
    client.send(message.encode())
    data = client.recv(1024)
    res = data.decode()

    return res


