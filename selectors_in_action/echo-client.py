# client socket that pings server or set to recieve a message from server

import socket
class Client():


    def __init__(self,x) -> None:
        super().__init__()
        self.x = x
        self.Host = "127.0.0.1"
        self.PORT = 65432
    

    def ping(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.Host, self.PORT))
            try:
                while True:
                    data = input(">")
                    s.sendall(data.encode())
            except KeyboardInterrupt:
                print(f"stop echo from client {self.x}")

    def recieve(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.Host, self.PORT))
            try:
                while True:
                    data = s.recv(1024).decode()
                    print(data)
            except KeyboardInterrupt:
                print(f"stop echo from client {self.x}")

            


client1 = Client(1)
client1.recieve()

