from cryptography.fernet import Fernet

secret_key = b'zPJ2dKzRdgemBJBlfFuCpTC_W-z55tAMJjopY_VqaJA='
encrypted_data = b'gAAAAABnAVVcWnmsgHKeEGe94aa8InPbs0Sb8_b_OoZx3ThuYU-wdm3SFymr3NP71762GDzTrPaHcEMKWBAua1-BhQ6WIH5WBA=='

fernet_key = Fernet(secret_key)

decrypted_data = fernet_key.decrypt(encrypted_data)

decrypted_data = decrypted_data.decode('utf-8')
print(decrypted_data)