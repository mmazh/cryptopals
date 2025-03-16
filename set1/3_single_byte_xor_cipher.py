
# Test values
# encrypted string: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# result: Cooking MC's like a pound of bacon

ciphertext = input("Enter encrypted string: ")
ciphertext = bytes.fromhex(ciphertext)

# keys is a list of tuples of the form (score, cleartext) 
# score = number of alphabetical characters in cleartext
# cleartext = the result when ciphertext is xor'ed against an ascii byte
keys = []

# ascii range is 0-127
for a in range(128):
    key = str.encode(chr(a) * len(ciphertext))

    # xor the ciphertext against the current ascii byte
    res = bytes(a ^ b for a, b in zip(ciphertext, key))

    # calculte the number of alphabetical characters in decrypted string
    res = res.decode("utf-8")
    score = 0
    for r in res:
        if r.isalpha():
            score += 1
    
    # add score and decrypted text to keys array
    keys.append((score, res))

# find the tuple with the largest score value in the keys array
# output its corresponding decrypted text
result = sorted(keys,key=lambda x: x[0], reverse=True)[0][1]
print(result)
