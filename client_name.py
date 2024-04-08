import socket

def get_client_name(client_ip):
    try:
        with open('clients.txt', 'r') as file:
            for line in file:
                ip, name = line.strip().split(',')
                if ip == client_ip:
                    return name
    except FileNotFoundError:
        pass
    return None