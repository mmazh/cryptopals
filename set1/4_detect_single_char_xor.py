import os


def xor_bytes(val1, val2):
    return bytes(a ^ b for a, b in zip(val1, val2))

def find_score(decrypted_string):
    score = 0
    for r in decrypted_string:
        if r.isalpha() or r.isspace():
            score += 1
    return score

def score_data(data):
    keys = []
    for line in data:
        for a in range(128):
            key = str.encode(chr(a) * len(line))
            res = xor_bytes(key, line)
            res = res.decode("latin-1")
            score = find_score(res)
            keys.append((score, res))
    return keys


def get_file_data():
    file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), './files/4.txt')
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(bytes.fromhex(line))
    return lines


def main():
    data_lines = get_file_data()
    keys = score_data(data_lines)
    result = sorted(keys,key=lambda x: x[0], reverse=True)[0][1]
    print(result)


if __name__ == "__main__":
    main()