import socket

HOST = 'server'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to the server. Type your message (or 'exit' to quit):")
    while True:
        message = input("> ")
        if message.lower() == 'exit':
            print("Exiting.")
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Received: {data.decode()}")
