from ping3 import ping, verbose_ping

for x in range(1, 255):
    res = ping(f"192.168.10.{x}")
    if res:
        print(f"Host 192.168.10.{x} => ACTIVE")
    else:
        print(f"Host 192.168.10.{x} => is dead ...")