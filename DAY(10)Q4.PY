# Using Manual Reverse Construction
n = 9
original = n
rev = 0
bits = n.bit_length()

for i in range(bits):
    rev = (rev << 1) | (n & 1)
    n >>= 1

print(original == rev)