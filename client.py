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
    
    refreshClock = int(ans)
    break

#print(refreshClock)
os.system(f'time {today.tm_hour}:{today.tm_min +refreshClock}:{00}')

print(f'Novo horário do sistema é: {today.tm_hour}:{today.tm_min + refreshClock}:{00}')
client.close()