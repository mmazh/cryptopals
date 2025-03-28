# test values
# 1: 1c0111001f010100061a024b53535009181c
# 2: 686974207468652062756c6c277320657965
# result: 746865206b696420646f6e277420706c6179


def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))


def collect_input():
    str1 = input("Enter hex string 1: ")
    str2 = input("Enter hex string 2: ")
    return bytes.fromhex(str1), bytes.fromhex(str2)


def output_results(res):
    print("xor result: ", res.hex())


def main():
    str1, str2 = collect_input()
    res = xor_bytes(str1, str2)
    output_results(res)

main()