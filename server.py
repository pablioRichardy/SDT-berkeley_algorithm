import socket, time, os

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

server.bind(('127.0.0.1', 5050))
server.listen(3)
refreshCLOCK = 0
clientTIme = 0

while True:
    print('[SOCKET] Inicializado - Esperando conexão do client')
    client, addr = server.accept()
    clients.append(client)

    print(f'[{addr[0]}] se conectou.')

    ans = client.recv(2048).decode()
    clientTIme = ans

    times.append(serverTime - int(ans))

    refreshCLOCK = int(avarage(times))
    if refreshCLOCK < 0:
        refreshCLOCK = refreshCLOCK * -1
    client.send(f'{(serverTime + refreshCLOCK) - int(clientTIme)}'.encode())
    
    if not ans:
        server.close()
        break
    
    break

mins = today.tm_min + refreshCLOCK

os.system(f'time {today.tm_hour}:{today.tm_min + (refreshCLOCK)}:{00}')
print(f'Novo horário do sistema é: {today.tm_hour}:{today.tm_min + (refreshCLOCK)}:{00}')
server.close()


