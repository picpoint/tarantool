import socket

def server_connect_func():
    server = socket.socket()
    server.bind(("192.168.24.51", 22))
    server.listen(3)
    print("Server start")

    con, addr = server.accept()
    print(f"Connection: {con}")
    print(f"Address: {addr}")

    message = "Hello from server"
    con.send(message.encode())
    con.close()

    print("Server is close connect")
    con.close()




