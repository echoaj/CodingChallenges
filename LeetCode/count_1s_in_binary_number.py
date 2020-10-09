# - Programming Interviews Exposed.pdf

# Write a function that determines the number of 1 bits
# in the binary representation of a given integer.



dec = 5000

print(bin(dec))
count = 0

while dec:
    num = dec & 1
    dec = dec >> 1
    count += 1 if num == 1 else 0


print(count)