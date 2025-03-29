import os
import base64
from Crypto.Cipher import AES


def get_file_data():
    file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), './files/7.txt')
    file_data = ""
    with open(file_path, 'r') as file:
        for line in file:
            file_data += line.strip()
    return base64.b64decode(file_data)


def output_results(data):
    print(data.decode('utf-8'))


def main():
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = get_file_data()
    data = cipher.decrypt(encrypted_data)
    output_results(data)


main()