# CSS324-simple-socket

This project demonstrates a simple socket communication setup between a server and a client using Python and Docker. The server listens for connections and reverses the messages sent by the client. The client allows interactive input or predefined messages to be sent to the server.

## Features

- **Server:** Listens for incoming connections and reverses received messages.
- **Client:** Sends messages to the server and displays the reversed response.
- **Dockerized Setup:** Easily deploy server and client using Docker Compose.
- **Interactive Input:** The client can accept user input dynamically.

## Project Structure

```bash
CSS324-simple-socket/
├── docker-compose.yml
├── server/
│   ├── Dockerfile
│   └── server.py
├── client/
│   ├── Dockerfile
│   └── client.py
└── README.md
```

## Installation and Setup

1. Clone the repository
    ```bash
    git clone https://github.com/DRepresser/CSS324-simple-socket.git
    cd CSS324-simple-socket
    ```
2. Build and start the services
    ```bash
    docker-compose up --build
    ```
3. To run the server only (in detached mode)
    ```bash
    docker-compose up -d server
    ```
4. To run the client interactively
    ```bash
    docker-compose run client
    ```

## Usage

### Server

The server listens on port `8080` (mapped to your host). It handles incoming connections and reverses the received messages.

### Client

The client connects to the server and

- Prompts the user for input interactively.
- Sends the input to the server.
- Displays the reversed response from the server.

Example session

```
Connected to the server. Type your message (or 'exit' to quit):
> Hello, Server!
Received: !revreS ,olleH
> How are you?
Received: ?uoy era woH
> exit
Exiting.
```

## Configuration

### Docker Compose

- `stdin_open: true` and `tty: true` are set for the client to allow interactive input.

### Ports

- The server listens on port `8080`, which is exposed to the host.

## Troubleshooting

- **Input Not Working:** Ensure you run the client with `docker-compose run client` to enable interactive input.

- **Manual Container Access:** Use `docker exec` to attach to the client container.
    ```bash
    docker exec -it css324-simple-socket-client-1 python client.py
    ```

- **Test Without Docker:** Run `server.py` and `client.py` directly on your host machine to debug any issues unrelated to Docker.