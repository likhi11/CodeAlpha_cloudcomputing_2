from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

KEY = os.getenv("AES_KEY", "ThisIsASecretKeyForAES256!!").encode('utf-8')
KEY = KEY.ljust(32, b' ')[:32]

def pad(s): return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
def unpad(s): return s[:-ord(s[-1])]

def encrypt_data(raw):
    raw = pad(raw)
    cipher = AES.new(KEY, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(raw.encode())).decode()

def decrypt_data(enc):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(enc)).decode())