import base64

# test values
# input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

def main():
    hex_string = input("Enter hex string: ") 

    # perform encoding operation on raw bytes
    hex_bytes = bytes.fromhex(hex_string)
    encoded_data = base64.b64encode(hex_bytes)

    print(encoded_data.decode("utf-8"))

main()