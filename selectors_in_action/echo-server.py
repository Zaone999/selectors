# simple server socket 
# the server only echo the data recived

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("no data recieved")
                break
            conn.sendall(data)