import socket

HOST = 'server'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input("Enter message to send: ")
    s.sendall(message.encode())
    data = s.recv(1024)

print(f"Received: {data.decode()}")
