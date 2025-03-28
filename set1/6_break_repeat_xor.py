import os
import base64


def hamming_distance(b1, b2):
    result = 0
    for c1, c2 in zip(b1, b2):
        x = c1 ^ c2
        diff = 0
        # the result of the xor operation is 1 when bits differ, 0 otherwise
        # so add up the number of 1 bits from the xor result to get num bits that differ
        while (x > 0):
            diff += x & 1
            x >>= 1
        result += diff
    return result


def average_hamming_distance(blocks, keysize):
    hamming_distances = []
    for i in range(len(blocks) - 1):
        dist = (hamming_distance(blocks[i], blocks[i + 1])) / keysize
        hamming_distances.append(dist)
    return sum(hamming_distances) / len(hamming_distances)


def guess_key_size(data):
    res = []
    for keysize in range(2, 41):
        key_size_blocks = create_blocks(data, keysize)[:10]
        average = average_hamming_distance(key_size_blocks, keysize)
        res.append({ "keysize": keysize, "distance": average})
    return sorted(res, key=lambda x: x["distance"])[0]["keysize"]


def create_blocks(data, block_size):
    blocks = []
    for i in range(block_size, len(data), block_size):
        blocks.append(data[i - block_size: i])
    return blocks
                      

def transpose_blocks(blocks, block_size):
    transposed = []
    for i in range(block_size):
        ith_byte_block = []
        for block in blocks:
            ith_byte_block.append(block[i])
        transposed.append(bytearray(ith_byte_block))
    return transposed


def xor_bytes(val1, val2):
    res = bytes(a ^ b for a, b in zip(val1, val2))
    return res


def find_score(string):
    score = 0
    for r in string:
        freq = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', '.']
        if r in freq:
            score += 1
    return score


def score_blocks(block):
    keys = []
    for a in range(128):
        key = [a] * len(block)
        res = xor_bytes(key, block)
        res = res.decode("utf-8")
        score = find_score(res)
        keys.append({"score": score, "xor_key": a})
    return keys


def guess_key(transposed):
    key_guess = []
    for block in transposed:
        result = score_blocks(block)
        highest_score_xor = sorted(result,key=lambda x: x["score"], reverse=True)[0]["xor_key"]
        key_guess.append(highest_score_xor)
    return bytearray(key_guess)
        

def generate_key(xor_key, ciphertext):
    ciphertext_size = len(ciphertext)
    repetitions = (ciphertext_size // len(xor_key)) + 1
    xor_key *= repetitions
    return xor_key[:ciphertext_size]


def decode_data(data, key):
    repeated_key = generate_key(key, data)
    return xor_bytes(data, repeated_key)


def output_results(plaintext, key):
    print("Repeating XOR Key: ", key.decode('utf-8'))
    print("Plaintext: ", plaintext.decode('utf-8'))


def get_file_data():
    file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), './files/6.txt')
    file_data = ""
    with open(file_path, 'r') as file:
        for line in file:
            file_data += line.strip()
    return base64.b64decode(file_data)


def main():
    data = get_file_data()
    key_size_guess = guess_key_size(data)
    blocks = create_blocks(data, key_size_guess)
    transposed = transpose_blocks(blocks, key_size_guess)
    key_guess = guess_key(transposed)
    plaintext = decode_data(data, key_guess)
    output_results(plaintext, key_guess[:key_size_guess])


main()
