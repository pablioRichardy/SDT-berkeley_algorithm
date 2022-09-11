import socket, time, threading

times = []

today = time.localtime()
clientTime = (today.tm_hour * 60) + today.tm_min


refreshClock = ''
minutesNow = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(socket.gethostname()), 5050))

while True:
    client.send(f'{clientTime}'.encode())
    ans = client.recv(2048).decode()

    print(ans)
