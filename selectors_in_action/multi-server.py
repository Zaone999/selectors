import socket
import selectors
import json

sel = selectors.DefaultSelector()
connected_users = {}

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read

    print(f"Accepted connection from {addr}")
    username = conn.recv(1024).decode()
    print(f"user's username is {username}")
    conn.setblocking(False)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=username)
    connected_users[username] = conn


def get_connected_users(connected_users):
    user_list = '\n'.join(f"[*] {key}" for key in connected_users)
    return user_list

def echo(connected_users, recv_data):
        for username , connection_obj in connected_users.items():
            connection_obj.sendall(recv_data.encode())
            print(f"log : echo to {username}")  


def send_output(packet, receiver):
    connected_users[receiver].sendall(packet.encode())

def handle_request(connected_users,recv_data, sock):
    parsed_data = json.loads(recv_data)
    header = parsed_data['header']
    content = parsed_data['content']
    receiver = parsed_data['receiver']
    sender = parsed_data['sender']
    if header == 'info':
        users = get_connected_users(connected_users)
        packet = json.dumps({'sender' : None, 'content' : users})
        send_output(packet, receiver)
    elif header == 'echo':
        packet = json.dumps({'sender' : sender, 'content' : content})
        echo(connected_users, packet)
    else:
        if receiver in connected_users:
            packet = json.dumps({'sender' : sender, 'content' : content})
            send_output(packet, receiver)
        else:
            content = f"user {receiver} doesn't exist"
            packet = json.dumps({'error' : content})
            sock.sendall(packet.encode())            

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            handle_request(connected_users,recv_data,sock)
        else:
            print(f"Closing connection to {data}")
            del connected_users[data]
            sel.unregister(sock)
            sock.close()
            


host = "127.0.0.1"
port = 65432

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
