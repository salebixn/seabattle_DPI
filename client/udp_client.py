from sys import exit
from socket import socket, AF_INET, SOCK_DGRAM
from config import HOST, PORT

from table import generate_table
from field import field
from spawn_ships import spawn_ships


def parse_ship(data: str) -> list:
    list_data = []
    for val in data[0].decode('UTF-8'):
        if val not in ('(', ')', ' ', ',', '[', ']'):
            list_data.append(int(val))
    list_data = [list_data[0], list_data[1], list_data[2:]]
    return list_data


def connect():
    with socket(AF_INET, SOCK_DGRAM) as s:
        s.sendto(b'connect', (HOST, PORT))
        try:
            data = s.recvfrom(1024)

            print('server message:\n\n', generate_table(
                spawn_ships(field, parse_ship(data))))

        except KeyboardInterrupt:
            exit()

        while True:
            data = s.recvfrom(1024)
            if data[0].decode('UTF-8') == 'your step':
                step = input('your step: ')
                if step == 'exit':
                    exit()

                s.sendto(step.encode('UTF-8'), (HOST, PORT))
            else:
                print(data[0].decode('UTF-8'))


connect()
