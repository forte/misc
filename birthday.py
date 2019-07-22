'''
---Birthday Attack on a 40-bit Hash---

Problem:
Write a program that returns a tuple (s, t, n), where 
1. s and t are different ASCII strings
2. their SHA-1 hashes have the same high-order 40 bits
   (same 10 initial hex digits) 
3. n is the number of calls to SHA-1
'''

import hashlib
import string
import random

def birthday():
    ascii_lst = string.ascii_letters + string.digits + string.punctuation
    n = 0
    hashDict = {}
    while (True):
        n = n + 1
        s = ''.join(random.choice(ascii_lst) for _ in range(10))
        hash_val = hashval=hashlib.sha1(s).hexdigest()[:10]
        t = hashDict.get(hash_val)
        if (t and s is not t):
            print(hash_val)
            return (s, t, n)
        else:
            hashDict[hash_val] = s

tpl = birthday()
print(tpl)

'''
Successful runs:
1. ('iRETar$6$u', '}h)}xi)MQJ', 1152972)
hash_val = 0cfb6ad30e

2. ('DnKZ>@)7WA', '3O3v~ZcqB(', 734658)
hash_val = 3679369843

3. ('_asAsq^N4*', '^<MZ.yYMkQ', 848160)
hash_val = bc1ef6a63a

4. ('3UpZpLy+fH', '`F/>?b\\2mo', 1172575)
hash_val = f7f72fcf5a
'''
