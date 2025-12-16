
# Test values
# input: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# output: Cooking MC's like a pound of bacon

def xor_bytes(byte, encrypted_string):
    key = str.encode(chr(byte) * len(encrypted_string))
    res = bytes(a ^ b for a, b in zip(encrypted_string, key))
    return res

def find_score(decrypted_string):
    score = 0
    for r in decrypted_string:
        if r.isalpha() or r.isspace():
            score += 1
    return score

def score_strings(line):
    keys = []
    for a in range(128):
        res = xor_bytes(a, line)
        res = res.decode("utf-8")
        score = find_score(res)
        keys.append((score, res))
    return keys


def main():
    ciphertext = input("Enter encrypted string: ")
    ciphertext = bytes.fromhex(ciphertext)
    keys = score_strings(ciphertext)
    result = sorted(keys,key=lambda x: x[0], reverse=True)[0][1]
    print(result)


if __name__ == "__main__":
    main()