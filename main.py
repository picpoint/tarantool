from ping_hosts import ping_network

print("Маска по умолчанию /24")
network = input("Введите IP подсети: ")
ping_network(network)