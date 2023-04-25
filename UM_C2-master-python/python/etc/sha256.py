# Python program to find SHA256 hash string of a file
import hashlib

filename = "/tmp/a.txt"

sha256_hash = hashlib.sha256()
sha3_256_hash = hashlib.sha3_256()
with open(filename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())

with open(filename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha3_256_hash.update(byte_block)
    print(sha3_256_hash.hexdigest())
