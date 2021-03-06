import socket
import sys
from rc4 import enc, dec
from rsa import *
from Crypto.Util.number import *
import threading
import os
from message_threads import *

if(len(sys.argv) < 2):
    print('[x] USAGE: message HOST PORT')
    os.exit(0)

host = sys.argv[1]
port = int(sys.argv[2])

e, n, d = key_gen(1024)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

data = ('INTZ'+':'+str(e)+':'+str(n)).encode()
print(data)

client.sendall(data)
data = client.recv(1024)
msg = bytes_to_long(data)
key = long_to_bytes(pow(msg, d, n)).decode()
print(f'we recv this: {key}')
client.sendall(enc('we recv the key', key).encode())
data = client.recv(1024)
dec(data.decode(), key)
client.sendall(b'')
t1 = threading.Thread(target=send_msg, args=(client, key))
t2 = threading.Thread(target=recieve_msg, args=(client, key))

t1.start()
t2.start()
