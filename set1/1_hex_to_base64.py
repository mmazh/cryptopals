import base64

# test values
# hex string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# expected output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t 

# collect hex string from user
hex_string = input("Please enter your hex string: ")

# perform encoding operation on raw bytes
hex_bytes = bytes.fromhex(hex_string)
encoded_data = base64.b64encode(hex_bytes)

# convert encoded bytes back to encoded string because it looks better
print(encoded_data.decode("utf-8"))