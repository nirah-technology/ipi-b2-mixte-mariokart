from datetime import datetime
from pathlib import Path
from socket import socket as Socket, AF_INET, SOCK_STREAM
from threading import Thread


class Message:
    def __init__(self, id: str, sender: str, recipient: str, message: str, timestamp: datetime):
        self.id: str = id
        self.sender: str = sender
        self.recipient: str = recipient
        self.message: str = message
        self.timestamp: datetime = timestamp

class MessagesRepository:
    def __init__(self, database_file: Path|None = None):
        self.__database_file: Path = database_file
        self.cache = []

    def save_message(self, message: Message):
        self.cache.append(message)

    def list_all_messages(self) -> list[Message]:
        return self.cache.copy()

class MessagingServer:
    def __init__(self, bind_address: str, bind_port: int):
        self.bind_address: str = bind_address 
        self.bind_port: int = bind_port
        self.clients: dict[str, Socket] = {}
        self.messages_repository = MessagesRepository()

    def start(self):
        print("Starting server...")
        self.socket = Socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.bind_address, self.bind_port))
        print(f"Listening on: tcp://{self.bind_address}:{self.bind_port}")
        self.socket.listen(5)
        print("Waiting for client connection...")

        while True:
            client_socket, client_info = self.socket.accept()
            thread: Thread = Thread(
                target=self.process_client_connection, 
                args=(client_socket))
            thread.start()

    def process_client_connection(self, client_socket: Socket):
        print("A client is connected")
        client_id: str = client_socket.recv(1024).decode()
        self.clients.setdefault(client_id, client_socket)
        while True:
            message: str = client_socket.recv(1024).decode() # client_id:Bonjour tout:  le monde
            parts: list[str] = message.split(":", 2)
            recipient_id = parts[0]
            message_content = parts[1]
            recipient_socket = self.clients.get(recipient_id)
            if (recipient_socket is not None):
                recipient_socket.send(message_content.encode())
            

class MessagingClient:
    def __init__(self, host: str, port: int, client_id: str):
        self.host: str = host
        self.port: int = port
        self.socket: Socket = None
        self.client_id: str = client_id
    
    def exchange(self, message: str, recipient_id: str):
        if (self.socket is None):
            self.socket = Socket(AF_INET, SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.socket.send(self.client_id.encode())

        self.socket.send(f"{recipient_id}:{message}".encode())
        response = self.socket.recv(1024)