

def xor_bytes(plaintext, xor_key):
    return bytes(a ^ b for a, b in zip(plaintext, xor_key))


def generate_key(xor_key, plaintext):
    plaintext_size = len(plaintext)

    repetitions = (plaintext_size // len(xor_key)) + 1
    xor_key *= repetitions

    return xor_key[:plaintext_size]


def main():
    plaintext = input("Enter text to encrypt: ")
    xor_key = input("Enter key for repeating-key XOR: ")

    plaintext = plaintext.encode('utf-8')
    xor_key = xor_key.encode('utf-8')

    xor_key = generate_key(xor_key, plaintext)
    ciphertext = xor_bytes(plaintext, xor_key)

    print(ciphertext.hex())


main()