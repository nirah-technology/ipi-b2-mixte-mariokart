from socket import socket as Socket, AF_INET, SOCK_STREAM
from threading import Thread

class MarioKartServer:
    def __init__(self, bind_address: str, bind_port: int):
        self.bind_address: str = bind_address 
        self.bind_port: int = bind_port
        self.socket: Socket|None = None


    def start(self):
        if (self.socket == None):
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
                    args=(client_socket, client_info))
                thread.start()

    def process_client_connection(self, client_socket: Socket, client_info: any):
        print("A client is connected")
        client_socket.send("Bonjour!".encode())
        # Longeur du message envoyé par le client = 164_857 bits
        buffer_size: int = 32
        message: str = ""
        message_part = client_socket.recv(buffer_size)
        message += message_part.decode()
        while len(message_part) == buffer_size:
            message_part = client_socket.recv(buffer_size)
            message += message_part.decode()
        client_socket.close()
                