# Time: O(N) and Space O(N)
def has_unique_chars(string):
    # Assuming extented ASCII character set
    if len(string) > 256:
        return False
    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True


print(has_unique_chars("abcdefg"))  # should return True
print(has_unique_chars("hello"))  # should return False
print(has_unique_chars(""))  # should return True
print(has_unique_chars("0123456789"))  # should return True
print(has_unique_chars("abacadaeaf"))  # should return False
