import os
from cryptography.fernet import Fernet

base_dir = r"D:\JustCode\pythonProject\lesson_30\spy_reports"
base_dir_2 = r"D:\JustCode\pythonProject\lesson_30\decrypted_reports"
filenames = os.listdir(base_dir)
# print(filenames)

file_dates = []
for filename in filenames:
    file_date = filename[:2]
    dates = int(file_date)
    file_dates.append(dates)

for i in range(1, 31):
    if i in file_dates:
        print(f"{i}_10_2023 - отчет по этому дню есть.")

    else:
        print(f"{i}_10_2023 - отчет по этому дню нет.")

with open(r"D:\JustCode\pythonProject\lesson_30\spy.key", "r") as f:
    secret_key = f.read()

fernet_key = Fernet(secret_key)


for filename in filenames:
    filepath = f"{base_dir}/{filename}"
    with open(filepath, "r") as f:
        data = f.read()

    decrypted_data = fernet_key.decrypt(data)
    decrypted_data = decrypted_data.decode('utf-8')

    filepath_2 = f"{base_dir_2}/{filename}"
    with open(filepath_2, "w", encoding='utf-8') as f:
        f.write(decrypted_data)




