# Source: https://www.ibm.com/docs/en/zos/2.4.0?topic=rules-pkcs-padding-method


def collect_input():
    plaintext = input("Enter plaintext to pad: ")
    pad_size = input("Enter padding size (in bytes): ")
    return plaintext, int(pad_size)


def pad_data(plaintext, pad_size):
    plaintext = plaintext.encode('utf-8')
    required_pad_bytes = pad_size - (len(plaintext) % pad_size)
    plaintext += bytes([required_pad_bytes] * required_pad_bytes)
    return plaintext


def main():
    plaintext, pad_size = collect_input()
    padded_data = pad_data(plaintext, pad_size)
    print("Padded plaintext: ", padded_data)


if __name__ == "__main__":
    main()