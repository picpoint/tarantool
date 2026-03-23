from ping3 import ping, verbose_ping
from termcolor import colored

def ping_network_func(ip):
    sub_network = ip[:-2]   

    for x in range(1, 255):
        res = ping(f"{sub_network}.{x}")
        if res:
            print(colored(f"[+]Host {sub_network}.{x} => ACTIVE", 'green'))
        else:
            print(colored(f"[-]Host {sub_network}.{x} => is dead ...", 'red'))
