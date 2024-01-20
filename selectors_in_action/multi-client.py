import selectors
import socket
import sys
import types
import json

HOST = '127.0.0.1'
PORT = 65432
sel = selectors.DefaultSelector()


def service_connection(key, mask):
    sock = key.fileobj
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024).decode()
        if recv_data:
            parsed_data = json.loads(recv_data)
            if 'error' in recv_data:
                print(f"{parsed_data['error']}")
            else:
                if parsed_data['sender'] is not None:
                    print(f"{parsed_data['content']}  (sent by {parsed_data['sender']})")
                else:
                    print(f"{parsed_data['content']}")
        else:
            print("Closing connection")
            sel.unregister(sock)
            sel.unregister(sys.stdin)
            raise KeyboardInterrupt

def establich_connection(sock):
    sock.connect((HOST, PORT))
    username  = input("Enter username ")
    sock.sendall(username.encode())
    sock.setblocking(False)
    return username


supported_commands = ['send', 'echo' ,'info']

def parse_input(input_line):
    parts = input_line.strip().split()
    command = parts[0].lower()
    if command == 'send':
        arguments = parts[1:]
    elif command == 'echo':
        arguments = parts[1:]
    elif command == 'info':
        arguments = None
    else:
        arguments = None
    return command, arguments

command = None
arguments = None

def is_valid_input():
    global command, arguments
    non_parsed_input = input()

    command, arguments = parse_input(non_parsed_input)
    if command in supported_commands:
        return True
    else:
        arguments = None
        return False

def send_input(command, arguments):
    packet, receiver = forge_request(command, arguments)
    sock.sendall(packet.encode())


def forge_request(command, argument):
    if command == 'send':
        receiver_username = argument[0]
        message = ' '.join(argument[1:])
    elif command == 'echo':
        receiver_username = None
        message = ' '.join(argument[0:])
    else:
        message = None
        receiver_username = client_username
    packet = json.dumps({"receiver": receiver_username, "header": command , "content": message, "sender" : client_username})
    return packet, receiver_username


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_username = establich_connection(sock)
    sel.register(sock, selectors.EVENT_READ, data=types.SimpleNamespace(sock=sock))
except ConnectionRefusedError:
    client_username = None
    print(f"Can't connect , maybe server is down")
except KeyboardInterrupt:
    client_username = None
    print("Exiting client")


sel.register(sys.stdin, selectors.EVENT_READ, data=types.SimpleNamespace(sock=sock))

if client_username is not None:
    try:
        while True:
            events = sel.select(timeout=None)
            for key, mask in events:
                if key.fileobj == sys.stdin:
                    if is_valid_input():
                        send_input(command, arguments)
                    else:
                        print(f"invalid command")
                else:
                    service_connection(key, mask)
    except KeyboardInterrupt:
        print("Exiting client")
    finally:
        sel.close()
