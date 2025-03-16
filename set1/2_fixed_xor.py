# Test values
# string 1: 1c0111001f010100061a024b53535009181c
# string 2: 686974207468652062756c6c277320657965
# result: 746865206b696420646f6e277420706c6179

while True:
    str1 = input("Enter hex string 1: ")
    str2 = input("Enter hex string 2: ")

    if len(str1) != len(str2):
        print("Error. Strings are not the same size")
        continue

    # convert to raw bytes
    str1 = bytes.fromhex(str1)
    str2 = bytes.fromhex(str2)
    
    # xor the raw bytes
    res = bytes(a ^ b for a, b in zip(str1, str2))

    # covert back to hex
    print("xor result: ", res.hex())
    break