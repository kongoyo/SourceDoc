import binascii
import os
import secrets

import pbkdf2
import pyaes

# Derive a 256-bit AES encryption key from the password
password_encrypt = input("Please input password(8-10 chars minimal length is recommended): ")
passwordSalt = os.urandom(128)
key_value = pbkdf2.PBKDF2(password_encrypt, passwordSalt).read(256)
print("AES encryption key:", binascii.hexlify(key_value))

# AES Encryption (CTR Block Mode)
# Encrypt the plaintext with the given key:
#   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
password_encrypt = input("Please input password: ")
iv = secrets.randbits(128)
key_encrypt = pbkdf2.PBKDF2(password_encrypt, passwordSalt).read(64)
# plaintext = "Text for encryption"
aes = pyaes.AESModeOfOperationCTR(key_encrypt, pyaes.Counter(iv))
ciphertext = aes.encrypt(password_encrypt)
print("Encrypted:", binascii.hexlify(ciphertext))
