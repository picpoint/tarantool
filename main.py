from ping_hosts import ping_network_func
from socket_client import client_connect_func

'''
Модуль сканирования сети
'''
# print("Маска по умолчанию /24")
# network = input("Введите IP подсети: ")
# ping_network(network)


res = client_connect_func(('www.python.org', 80))
print(res)
