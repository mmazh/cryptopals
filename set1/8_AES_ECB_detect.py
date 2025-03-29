import os

def get_file_data():
    file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), './files/8.txt')
    file_data = []
    with open(file_path, 'r') as file:
        for line in file:
            file_data.append(line.strip())
    return file_data


def create_blocks(data):
    block_size = 16
    blocks = []
    for i in range(block_size, len(data), block_size):
        blocks.append(data[i - block_size: i])
    return blocks


def find_identical_blocks(data):
    has_identical_blocks = []
    for line in data:
        blocks = create_blocks(bytes.fromhex(line))
        if len(list(set(blocks))) < len(blocks):
            has_identical_blocks.append(line)
    return has_identical_blocks


def output_results(lines):
    print("Potential AES ECB candidates: ")
    for line in lines:
        print(line)


def main():
    hex_encoded_data = get_file_data()
    identical_blocks_data = find_identical_blocks(hex_encoded_data)
    output_results(identical_blocks_data)


main()