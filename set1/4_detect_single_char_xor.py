
import os

keys = []
file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), '4.txt')

with open(file_path, 'r') as file:
    for line in file:
        line = bytes.fromhex(line)
        for a in range(128):
            key = str.encode(chr(a) * len(line))
            res = bytes(a ^ b for a, b in zip(line, key))

            # had to use latin-1 since utf-8 was throwing errors, not sure why
            res = res.decode("latin-1")
            score = 0
            for r in res:
                if r.isalpha() or r.isspace():
                    score += 1

            keys.append((score, res))

result = sorted(keys,key=lambda x: x[0], reverse=True)[0][1]
print(result)