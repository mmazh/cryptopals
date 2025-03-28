import base64

# test values
# input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t


def collect_input():
    hex_string = input("Enter hex string: ") 
    return bytes.fromhex(hex_string)


def output_results(b64_data):
    print(b64_data.decode("utf-8"))


def main():
    hex_bytes = collect_input()
    b64_encoded_data = base64.b64encode(hex_bytes)
    output_results(b64_encoded_data)
    

main()