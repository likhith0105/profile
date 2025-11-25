# Using Iteration (Two-pointer Approach)
n = 9
b = bin(n)[2:]
left, right = 0, len(b) - 1

is_palindrome = True
while left < right:
    if b[left] != b[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)