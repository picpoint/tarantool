from ping3 import ping, verbose_ping


def ping_network(part_ip):
    for x in range(1, 255):
        res = ping(f"{part_ip}.{x}")
        if res:
            print(f"Host {part_ip}.{x} => ACTIVE")
        else:
            print(f"Host {part_ip}.{x} => is dead ...")

ping_network("192.168.24")