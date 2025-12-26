from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

KEY_FILE = "secret.key"

def load_key():
    
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_file(file_data):
    
    key = load_key()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)

    encrypted_data = cipher.nonce + tag + ciphertext
    return encrypted_data

def decrypt_file(encrypted_data):
    
    key = load_key()

    nonce = encrypted_data[:16]
    tag = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

