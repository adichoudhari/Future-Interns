from Crypto.Random import get_random_bytes

key = get_random_bytes(32)
with open("secret.key", "wb") as f:
    f.write(key)

print("AES key generated successfully")

