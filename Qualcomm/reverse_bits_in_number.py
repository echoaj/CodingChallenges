
# Reverse the bits in a number


def reverse_bits_in_number(n):
    # Reverse the bits in a number
    # n: int
    # return: int
    return int(bin(n)[2:].zfill(32)[::-1], 2)


print(reverse_bits_in_number(0b00000010100101000001111010011100))
print(reverse_bits_in_number(0b11111111111111111111111111111101))
print(reverse_bits_in_number(0b10000000000000010100000000000000))
print(reverse_bits_in_number(0b00000000000000000000000000000001))
print(reverse_bits_in_number(0b0101))
print(reverse_bits_in_number(0b00111001111111111111111111111111).to_bytes(4, 'big'))
# 11111111111111111111111110011100
