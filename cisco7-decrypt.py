import sys
from binascii import unhexlify

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} [level 7 hash]")
    exit()

static_key = "tfd;kfoA,.iyewrkldJKD"
enc   = sys.argv[1]
start = int(enc[:2], 16) - 1
enc   = unhexlify(enc[2:])
key   = static_key[start:] + static_key[:start]

plain = ''.join([chr(x ^ ord(key[i % len(key)]))  for i, x in enumerate(enc)])
print(plain)