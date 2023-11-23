def first_non_repeating_char(string):
    freq_table = {}
    for char in string:
        freq_table[char] = freq_table.get(char, 0) + 1

    for char in string:
        if freq_table[char] == 1:
            return char
    return None


print(first_non_repeating_char("leetcode"))

print(first_non_repeating_char("hello"))

print(first_non_repeating_char("aabbcc"))
