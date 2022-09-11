from ast import arg
from http import client
from pydoc import cli
import socket, time, threading

times = [0]

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

today = time.localtime()
serverTime = (today.tm_hour * 60) + today.tm_min

clients = []

def avarage(arr):
    total = 0
    for i in range(0, int(len(arr))):
        total += arr[i]
    return total / int(len(arr))

server.bind((socket.gethostbyname(socket.gethostname()), 5050))
server.listen(3)

while True:
        client, addr = server.accept()
        print(f'[{addr[0]}] Connected.')
        clients.append(client)

        ans = client.recv(2048).decode()
        times.append(serverTime - 650)

        print(times)
        client.send(f'{int(avarage(times))}'.encode())
        print(avarage(times))

