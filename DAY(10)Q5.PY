# . Using String Slicing (for strings):
def is_palindrome_string(s):
    return s == s[::-1]

# Example usage:
print(is_palindrome_string("madam"))  # Output: True
print(is_palindrome_string("racecar")) # Output: True
print(is_palindrome_string("hello")) # Output: False