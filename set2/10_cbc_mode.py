import os
import base64
from Crypto.Cipher import AES

# sources: https://how.dev/answers/what-is-cbc

def get_file_data():
    file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), './files/10.txt')
    file_data = ""
    with open(file_path, 'r') as file:
        for line in file:
            file_data += line.strip()
    return base64.b64decode(file_data)


def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))


def create_blocks(data):
    blocks = []
    block_size = 16
    for i in range(block_size, len(data) + 1, block_size):
        blocks.append(data[i - block_size: i])
    bytes_to_pad = len(data) % block_size
    if bytes_to_pad:
        blocks.append(data[-bytes_to_pad:] + (b'\0' * (block_size - bytes_to_pad)))
    return blocks


def output_decrypt_results(data):
    for i in range(len(data)):
        data[i] = data[i].decode('ascii')
    res = ''.join(data)
    print(res)
    print()


def cbc_decrypt(cipher, blocks):
    plaintext = []
    for i in range(1, len(blocks)):
        ecb_decrypted_block = cipher.decrypt(blocks[i])
        plain_block = xor_bytes(ecb_decrypted_block, blocks[i - 1])
        plaintext.append(plain_block)
    return plaintext


def main():
    initial_vector = b'\0' * 16
    key = b'YELLOW SUBMARINE'
    cipher = AES.new(key, AES.MODE_ECB)

    encrypted_data = get_file_data()
    blocks = create_blocks(encrypted_data)
    blocks.insert(0, initial_vector)
    plaintext = cbc_decrypt(cipher, blocks)
    output_decrypt_results(plaintext)


if __name__ == "__main__":
    main()