from sys import exit
from socket import socket, AF_INET, SOCK_DGRAM
from copy import deepcopy

from config.server_config import HOST, PORT

from random_ship import random_ship


SYMBOLS = {
    'a': 0,
    'b': 1,
    'v': 2,
    'g': 3,
    'd': 4,
    'e': 5,
    'w': 6,
    'z': 7,
    'i': 8,
    'k': 9
}

def parse_ship(data: str) -> list:
    list_data = []
    for val in data:
        if val not in ('(', ')', ' ', ',', '[', ']'):
            list_data.append(int(val))
    list_data = [list_data[0], list_data[1], list_data[2:]]
    return list_data


def run():
    # конструктор udp-сокета
    with socket(AF_INET, SOCK_DGRAM) as s:
        # связываем ip-адрес и порт
        s.bind((HOST, PORT))

        players = []
        ships = []
        while True:
            data, addr = s.recvfrom(1024)
            print(addr)

            if len(players) < 2:
                players.append(addr)
                print(f'players: {players}')

                ship = random_ship()
                ships.append(ship)

                s.sendto(str(ship).encode('UTF-8'), addr)

                if len(players) == 2:
                    break

        for ship in ships:
            ship = parse_ship(str(ship))

        step = 'player1'
        print(step)
        while True:
            if len(ships[0][2]) == 0:
                s.sendto(b'player2 win', players[0])
                s.sendto(b'player2 win', players[1])
                exit()
            elif len(ships[1][2]) == 0:
                s.sendto(b'player1 win', players[0])
                s.sendto(b'player1 win', players[1])
                exit()

            if step == 'player1':
                try:
                    s.sendto(b'your step', players[0])
                    data, _ = s.recvfrom(1024)
                    if _:
                        print(_)
                    data = data.decode('UTF-8')
                    print(data)
                    data = data.split()
                    data[0] = SYMBOLS[data[0]]
                    data[1] = int(data[1]) - 1
                    print('ships', ships)
                    print(data)
                except Exception as e:
                    print(e)

                if ships[1][0] == 0:
                    if int(data[1]) == ships[1][1] and int(data[0]) in ships[1][2]:
                        response = b'ranil'
                        ships[1][2].remove(data[0])
                    else:
                        response = b'mimo'
                elif ships[1][0] == 1:
                    if int(data[0]) == ships[1][1] and int(data[1]) in ships[1][2]:
                        response = b'ranil'
                        ships[1][2].remove(data[1])
                    else:
                        response = b'mimo'

                s.sendto(response, players[0])
                step = 'player2'
                continue

            elif step == 'player2':
                try:
                    s.sendto(b'your step', players[1])
                    data, _ = s.recvfrom(1024)
                    print(_)
                    data = data.decode('UTF-8')
                    data = data.split()
                    data[0] = SYMBOLS[data[0]]
                    data[1] = int(data[1]) - 1
                    print('ships', ships)
                    print(data)
                except Exception as e:
                    print(e)

                if ships[0][0] == 0:
                    if int(data[1]) == ships[0][1] and int(data[0]) in ships[0][2]:
                        response = b'ranil'
                        ships[0][2].remove(data[0])
                    else:
                        response = b'mimo'
                elif ships[0][0] == 1:
                    if int(data[0]) == ships[0][1] and int(data[1]) in ships[0][2]:
                        response = b'ranil'
                        ships[0][2].remove(data[1])
                    else:
                        response = b'mimo'

                s.sendto(response, players[1])
                step = 'player1'
                continue


if __name__ == '__main__':
    run()
