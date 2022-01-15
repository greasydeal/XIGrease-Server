import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 33420))
s.listen(5)

print("Listening for connections...")

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address}.")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))