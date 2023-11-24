# Time O(N*KlogK)
def group_anagrams(strings):
    # Space O(N*K) worse case word is unique
    anagrams = {}
    for word in strings:  # O(N) N is number of the word in string
        group = "".join(sorted(word))  # O(KlogK) K is the length of word
        if group in anagrams:
            anagrams[group].append(word)
        else:
            anagrams[group] = [word]
    return list(anagrams.values())


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))
