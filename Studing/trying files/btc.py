import hashlib
import time

def sha256(text):
    return hashlib.sha256(text.encode("ascii")).hexdigest()

MAX_NONCE = 100000000000000000000000000000000000000000000000000000000000000000000000000000000

difficulty = 10

block_number = 0
transaction = 'A->B->10'
previous_hash = '0000000000000000000000000000000000000000000000000000000000000000'

for nonce in range(MAX_NONCE):
    text = str(block_number) + transaction + previous_hash + str(nonce)
    hash = sha256(text)
    if hash.startswith('0' * difficulty):
        print(f"Bitcoin mined with nonce value : {nonce}")
        break

    if nonce % 100000 == 0:  # print progress every 100000 attempts
        print(f'Tried {nonce} times...')

if nonce == MAX_NONCE - 1:
    print("Could not find a hash in the given range of upto", MAX_NONCE)