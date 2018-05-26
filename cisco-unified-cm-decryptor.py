#!/usr/bin/env python3
import sys
import binascii
from Cryptodome.Cipher import AES

# Standard Cisco key
key = b"\x73\x6d\x65\x74\x73\x79\x73\x6f\x63\x73\x69\x63\x63\x6e\x69\x00"

if (len(sys.argv) != 2):
    print("{} <password>".format(sys.argv[0]), file=sys.stderr)
    sys.exit(0)

if (len(sys.argv[1]) < 24) and (len(sys.argv[1]) % 2):
    print("ERROR: password length error", file=sys.stderr)
    sys.exit(1)

data = binascii.unhexlify(sys.argv[1])

iv = data[0:16]
data = data[16:]
c = AES.new(key, AES.MODE_CBC, iv)
decrypted = c.decrypt(data)
if not decrypted:
    print("ERROR: decryption error", file=sys.stderr)
    sys.exit(2)
print("Decrypted password (raw bytes):", decrypted)
# Unpad encrypted data
decrypted = decrypted[:-decrypted[-1]]
print("Decrypted password:", decrypted.decode('utf-8', errors='ignore'))
