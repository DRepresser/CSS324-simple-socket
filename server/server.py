import socket

HOST = '0.0.0.0'
PORT = 8080

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        # Reverse and send back the data
        response = data.decode()[::-1]
        conn.sendall(response.encode())
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server running on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        handle_client(conn, addr)
