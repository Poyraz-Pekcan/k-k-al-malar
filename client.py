import socket as s

HEADER = 64
PORT = 5050
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "172.18.160.1"
ADDR = (SERVER, PORT)

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello World")
send("Hello World")
send("Hello World")
send("Hello World")