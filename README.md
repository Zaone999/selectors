# Multi-Client Chat Server

## Project Overview
This project is a multi-client chat server and client implemented in Python. It enables real-time communication among users through a server that can handle multiple client connections simultaneously.

## Features
- **Server-Client Architecture**: Separate scripts for server and client.
- **Real-time Communication**: Enables multiple clients to connect and chat in real-time.
- **User Handling**: Supports multiple user connections with unique usernames.
- **Message Broadcasting and Direct Messaging**: Server can broadcast messages to all clients or send messages to specific clients.
- **Commands**:
  - `info`: Lists all connected users.
  - `send [username] message`: Sends a private message to a specified user.
  - `echo message`: Broadcasts a message to all connected users.

## Learning Outcomes
- **Understanding Selectors**: Gained a deep understanding of selectors in Python, providing a simpler and more efficient way to handle I/O multiplexing compared to threads.
- **Selectors vs Threads**: Learned about the advantages of selectors over threads, particularly in reducing overhead and improving scalability in network programming.
- **Flexibility of Selectors**: Discovered the broad applicability of selectors in managing file-like objects beyond sockets, opening avenues for use in various I/O-intensive applications.
- **Debugging Advantages**: Found that selectors offer easier debugging compared to a multi-threaded approach, making the application's behavior more predictable and linear.

## Known Bugs and Limitations
- **Username Uniqueness**: The system does not enforce unique usernames, leading to issues in message reception.
- **Lack of Username Validation**: Absence of server-side checks for username uniqueness can lead to conflicts.
- **Data Exchange Protocol**: Manual parsing of data for each socket operation is repetitive and inefficient. A better protocol is needed.
- **Repetitive Code**: Current handling of data serialization and deserialization leads to code redundancy.

## Technology Stack
- **Python**: Both server and client are implemented in Python.
- **Socket Programming**: Used for network communication.
- **Selectors Module**: For handling multiple connections simultaneously.
- **JSON**: For message serialization and deserialization.

## Installation Instructions
1. Ensure Python is installed on your system.
2. Download `multi-server.py` and `multi-client.py`.
3. No additional libraries are required.

## Usage Instructions
1. Start the server by running `python multi-server.py`.
2. In separate terminal windows, start each client by running `python multi-client.py`.
3. Use the provided commands (`info`, `send [username] message`, `echo message`) to interact within the chat.

## License
This project is released under the [MIT License](https://opensource.org/licenses/MIT).

*Note: Contributions and suggestions for improvements are highly welcome. If you encounter a bug, have a solution, or a feature request, please feel free to open an issue or submit a pull request on the project repository.*
