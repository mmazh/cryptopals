import base64

hex_string = input("Enter hex string: ") 

# perform encoding operation on raw bytes
hex_bytes = bytes.fromhex(hex_string)
encoded_data = base64.b64encode(hex_bytes)

print(encoded_data.decode("utf-8"))