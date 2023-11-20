# T(n) = O(n) + O(n) + O(n) = O(n)
# S(n) = O(n) + O(n) = O(n)
def are_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq2[char] = 1
    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    for char in freq1:
        if char not in freq2 and freq2[char] != freq1[char]:
            return False
    return True


print(are_anagram("listen", "silent"))
print(are_anagram("Dormitory", "Dirty room"))
print(are_anagram("Conversation", "Voices rant on"))
print(are_anagram("12345", "54321"))
print(are_anagram("12345", "543210"))  # False
