import socket
from  threading import Thread
import time
import os

def acceptConnections():
    global SERVER
    global clients
    
    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        client[client_name] = {
            "client": client,
            "address": addr,
            "connected_with": "",
            "file_name": "",
            "file_size": 4096
        }
        print(f"Connection established with (client_name) : (addr)")

        thread = Thread(target = handleClint, args = (client, client_name,))
        thread.start()