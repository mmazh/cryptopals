
import os

keys = []
file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), '4.txt')

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
    for a in range(128):
        res = xor_bytes(a, line)

        # had to use latin-1 since utf-8 was throwing errors, not sure why
        res = res.decode("latin-1")
        score = find_score(res)
        
        keys.append((score, res))

def main():
    with open(file_path, 'r') as file:
        for line in file:
            line = bytes.fromhex(line)
            score_strings(line)
    result = sorted(keys,key=lambda x: x[0], reverse=True)[0][1]
    print(result)

main()