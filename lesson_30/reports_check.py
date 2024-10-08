import os
from cryptography.fernet import Fernet

base_dir = r"D:\JustCode\pythonProject\lesson_30\decrypted_reports"
filenames = os.listdir(base_dir)

for filename in filenames:
    filepath = f"{base_dir}/{filename}"
    with open(filepath, "r", encoding='utf-8') as f:
        data = f.read()
    print(data)
    print("==================================")


print("\nПосле замены всех префиксов из вра на дру\n")
for filename in filenames:
    filepath = f"{base_dir}/{filename}"
    with open(filepath, "r", encoding='utf-8') as f:
        data = f.read()

    words = data.split(" ")
    new_data = []
    for word in words:
        if "Вра" in word or "вра" in word:
            i_word = word[3:]
            if word[:3] == "Вра":
                new_data.append("Дру" + i_word)
            else:
                new_data.append("дру" + i_word)

        else:
            new_data.append(word)

    new_data = " ".join(new_data)
    new_data += "\nПроверено!"
    print(new_data)
    print("++++++++++++++++++++++++++++++++++++")
    with open(filepath, "w", encoding='utf-8') as f:
        f.write(new_data)




