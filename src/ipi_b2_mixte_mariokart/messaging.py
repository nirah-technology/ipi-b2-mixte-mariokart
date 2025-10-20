from datetime import datetime
from pathlib import Path

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