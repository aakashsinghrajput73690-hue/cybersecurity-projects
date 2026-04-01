from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

with open("file.txt", "rb") as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open("encrypted_file.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

print("Encrypted!")
