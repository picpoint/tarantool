import socket
# import ldap
from dns import resolver,reversename
from ping3 import ping, verbose_ping

# # hostname = socket.gethostbyaddr("192.168.24.94")
# # print(hostname)

# socket.gethostname()
# res = socket.getfqdn("192.168.24.90")
# print(res)

# print(socket.gethostbyaddr("192.168.24.90"))
hostname = socket.gethostbyaddr('192.168.24.90')
print(hostname)


'''
def ping_network(part_ip):
    for x in range(1, 255):
        res = ping(f"{part_ip}.{x}")
        if res:
            print(f"Host {part_ip}.{x} => ACTIVE")
        else:
            print(f"Host {part_ip}.{x} => is dead ...")

ping_network("192.168.24")
'''