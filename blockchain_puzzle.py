'''
---Blockchain Puzzle---

Problem:
Write a program that estimates the time of solving
hash-based puzzle given a specific difficulty.

Largest 256-bit int ("easiest difficulty"):
115792089237316195423570985008687907853269984665640564039457584007913129639935

The plan is to keep dividing this number by 256, then 128, then 64, etc
until it takes my computer > ~5 mins to solve the puzzle.

Target 1:
452312848583266388373324160190187140051835877600158453279131187530910662655

Target 2:
3533694129556768659166595001485837031654967793751237916243212402585239551

Target 3:
55213970774324510299478046898216203619608871777363092441300193790394367

Target 4:
1725436586697640946858688965569256363112777243042596638790631055949823
'''

import hashlib
import string
import random
import time

def blockchain_puzzle(target):
    start = time.time() # start timer

    # random data to mimic data in blockchain header
    p_prev = "21312476870123241093"
    p_root = "65324987025126798347"
    time_stamp = "5234176896370832"

    while (True):
        hash_val = hashlib.sha256(p_prev + p_root + time_stamp)
        if (try_nonce(hash_val, target)):
            end = time.time()
            return (end-start) # time to solve puzzle

def try_nonce(hash_val, target):
    nonce = int(random.getrandbits(32)) # generate random nonce
    hash_val.update(str(nonce)) # update hash with nonce
    hash_as_int = int(hash_val.hexdigest(), 16)

    # check if the hash (as an integer) is less than the target
    if (hash_as_int < target):
        return True
    return False

# Code below will calculate 5 solutions for a target
target = 1725436586697640946858688965569256363112777243042596638790631055949823
for i in range(5):
    ans = blockchain_puzzle(target)
    print(ans)
