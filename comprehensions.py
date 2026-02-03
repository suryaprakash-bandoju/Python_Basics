# Comprehensions in Python
# 1.If statement comprehension
# toggle = False
# # This is normal way
# if toggle:
#     word = 'Enable'
# else:
#     word = 'Disable'
# print(word)

# # This is a comprehensive way
# word = 'Enable' if toggle else 'Disable'
# print(word)

# 2.List Comprehension

# items = ['item_a', 'item_b', 'item_c']

# # Traditional way
# upper_items = []
# for item in items:
#     item_upper = item.upper()
#     upper_items.append(item_upper)

# print(upper_items)

# # Using List Comprehension
# upper_items = [item.upper() for item in items]
# print(upper_items)

# List Comprehension with Conditions

# items = ['item_a', 'item_b', 'item_c', 'wrong_data']

# # Traditional way
# upper_items = []
# for item in items:
#     if 'item_' in item:
#         item_upper = item.upper()
#         upper_items.append(item_upper)
# print(upper_items)


# # Using List Comprehension

# upper_items = [item.upper() for item in items if 'item_' in item]
# print(upper_items)


# numbers = [1, 2, 3, 4, 5]
# num_sq = [num**2 for num in numbers] # Squared numbers
# num_cube = [num**3 for num in numbers] # Cube numbers
# num_cube_even = [num**3 for num in numbers if num % 2 == 0] # Cube of even numbers
# even_odd = ['Even' if num % 2 == 0 else 'Odd' for num in numbers] # Even Odd CLassification

# print(num_sq)
# print(num_cube)
# print(num_cube_even)
# print(even_odd)


# Dictionary Comprehension

mats = ['wood', 'steel', 'concrete', 'briks', 'glass', 'plastic']
dict_mats = {mat.lower():mat.upper() for mat in mats}

print(dict_mats)