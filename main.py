from ping_hosts import ping_network_func
from socket_client import client_connect_func
from socket_server import server_connect_func

'''
Модуль сканирования сети
'''
# print("Маска по умолчанию /24")
# network = input("Введите IP подсети: ")
# ping_network(network)


res_client = client_connect_func(("192.168.24.51", 22))
print(res_client)

res_server = server_connect_func()
print(res_server)

