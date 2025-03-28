# test values
# plaintext: Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal
# xor key: ICE
# result: 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
#         a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f


def xor_bytes(plaintext, xor_key):
    return bytes(a ^ b for a, b in zip(plaintext, xor_key))


def generate_key(xor_key, plaintext):
    plaintext_size = len(plaintext)
    repetitions = (plaintext_size // len(xor_key)) + 1
    xor_key *= repetitions
    return xor_key[:plaintext_size]


def collect_input():
    plaintext = input("Enter text to encrypt: ")
    xor_key = input("Enter key for repeating-key XOR: ")
    return plaintext.encode('utf-8'), xor_key.encode('utf-8')


def output_results(cipher):
    print(cipher.hex())


def main():
    plaintext, xor_key = collect_input()
    xor_key = generate_key(xor_key, plaintext)
    ciphertext = xor_bytes(plaintext, xor_key)
    output_results(ciphertext)
    

main()