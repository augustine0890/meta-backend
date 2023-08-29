
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(names) >= 6:
        better_list.append(name)
print(better_list)

best_list = [name for name in names if len(name) >= 6]
print(best_list)

# Rewrite the for loop to use enumerate
indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

# Print the list created above
print(names_uppercase)