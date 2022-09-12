from pydoc import cli
import socket, time, os

times = []

today = time.localtime()
clientTime = (today.tm_hour * 60) + today.tm_min


refreshClock = ''
minutesNow = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5050))

while True:
    client.send(f'{clientTime}'.encode())
    
    ans = client.recv(2048).decode()
    if ans != '':
        refreshClock = int(ans)
    break

today = time.localtime()
clientTime = (today.tm_hour * 60) + today.tm_min
hours = today.tm_hour
mins = (today.tm_min + refreshClock)
if (today.tm_min + refreshClock) > 60 :
    hours += 1
    mins -= 60

print(f'Novo horário do sistema é: {hours}:{mins}:{00}')
client.close()