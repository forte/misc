import hashlib
import string
import random
import socket

# start listening for messages
s = socket.socket()
host = '127.0.0.1'
port = 1234             
s.bind((host, port))
s.listen(5)

while True:
    # accept data from a client
    c, addr = s.accept()

    # receive and split message into the components of the block
    rec = c.recv(1024)
    split = rec.split('.')
    nonce = split[0]
    p_prev = split[1]
    p_root = split[2]
    time_stamp = split[3]
    target = split[4]

    # hash block
    hash_val = hashlib.sha256(p_prev + p_root + time_stamp + nonce)
    hash_as_int = int(hash_val.hexdigest(), 16)

    # verify the hash is smaller than the target
    if (hash_as_int < target):
        print('YES')
    else: 
        print('NO')

    c.close()