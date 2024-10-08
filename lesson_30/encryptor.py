import os
from cryptography.fernet import Fernet

base_dir = r"D:\JustCode\pythonProject\lesson_30\decrypted_reports"
base_dir_2 = r"D:\JustCode\pythonProject\lesson_30\encrypted_reports"
filenames = os.listdir(base_dir)

secret_key = Fernet.generate_key()
with open("./new_spy.key", "wb") as f:
    f.write(secret_key)

fernet_key = Fernet(secret_key)

for filename in filenames:
    filepath = f"{base_dir}/{filename}"
    if not "c" in filename or "C" in filename:
        with open(filepath, "rb") as f:
            data = f.read()

        encrypted_data = fernet_key.encrypt(data)
        with open(f"{base_dir_2}/{filename}", "wb") as f:
            f.write(encrypted_data)

