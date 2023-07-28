import binascii
import os
import secrets

import pbkdf2
import pyaes

# Derive a 256-bit AES encryption key from the password
password = input("Please input password(8-10 chars minimal length is recommended): ")
passwordSalt = os.urandom(128)
key1 = pbkdf2.PBKDF2(password, passwordSalt).read(256)
print('AES encryption key:', binascii.hexlify(key1))

# AES Encryption (CTR Block Mode)
# Encrypt the plaintext with the given key:
#   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
password = input("Please input password: ")
iv = secrets.randbits(128)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
plaintext = "Text for encryption"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('Encrypted:', binascii.hexlify(ciphertext))
