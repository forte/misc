import hashlib
import string
import random
import socket

host = '127.0.0.1'
port = 1234
target = 2312848583266388373324160190187140051835877600158453279131187530910662655

def blockchain_puzzle(target):
    # random data to mimic data in blockchain header
    p_prev = "21312476870123241093"
    p_root = "65324987025126798347"
    time_stamp = "5234176896370832"

    while (True):
        hash_val = hashlib.sha256(p_prev + p_root + time_stamp)
        nonce = try_nonce(hash_val, target)
        if (nonce):
            send(nonce, p_prev, p_root, time_stamp)
            break

def send(nonce, p_prev, p_root, time_stamp):
    # send block to be verifed
    s = socket.socket()
    s.connect((host, port))
    s.send(str(nonce) + '.' + str(p_prev) + '.' + str(p_root) + '.' + str(time_stamp) + '.' + str(target))
    print("Done Sending")
    s.shutdown(socket.SHUT_WR)
    s.close()

def try_nonce(hash_val, target):
    nonce = int(random.getrandbits(32)) # generate random nonce
    hash_val.update(str(nonce)) # update hash with nonce
    hash_as_int = int(hash_val.hexdigest(), 16)

    # check if the hash (as an integer) is less than the target
    if (hash_as_int < target):
        return nonce
    return False

blockchain_puzzle(target)
