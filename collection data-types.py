# Collection Data Types
# ---------------------------------------------------------------------
# Lists, Tuples, Sets, and Dictionaries
# ---------------------------------------------------------------------
# Lists
# empty_list = []
# my_list = ["surya", 123, 2.33,True,"prakash",783.4,False]

# print(my_list)
# print(type(my_list))

# print(my_list[0]) # Accessing the first element
# print(my_list[-3]) # Accessing the third element from the end

# Slicing
# #---------------------------------------------------------------------
# print(my_list[1:3]) # From 1 to 2
# print(my_list[:5]) # From 0 to 4
# print(my_list[1:6:2]) # From 1 to 6 with a step of 2
# print(my_list[::-1]) # Revesing the list
# print(my_list[::4]) # From 0 to end with a step of 4

# ---------------------------------------------------------------------


# List - Replace list items
# ---------------------------------------------------------------------
# my_list = ["surya",123,3.23,True,"prakash",5435,False]
# my_list[0] = "prakash"
# print(my_list)
# my_list[-1] = "lastitem"
# print(my_list)
# my_list[1:3] = ['a','b']
# print(my_list)

# ---------------------------------------------------------------------

# List - membership operators
# ---------------------------------------------------------------------
# my_list = ["surya",123,3.23,True,"prakash",5435,False]

# print("surya" in my_list)
# print(123 not in my_list)

# ---------------------------------------------------------------------

# List - Popular Functions
# ---------------------------------------------------------------------

# my_list = ["surya",123,3.23,True,"prakash",5435,False]
# number = [1,5,3,9,7,6,2,8,4]
# print(len(my_list)) # Length of the list
# print(sorted(number)) # Sorted list
# print(sum(number)) # Sum of the List
# print(max(number)) # Maximum value in the list
# print(min(number)) # Minimum value in the list

# ---------------------------------------------------------------------

# List - Methods
# ---------------------------------------------------------------------

# my_list = ["surya",123,3.23,True,"prakash",5435,False]
# my_list2 = ["apple","banana","cherry"]

# my_list.append("bandoju") # Append on item to the end of the list
# print(my_list)

# my_list.insert(2,"inserted_item") # Insert an item at a given position
# print(my_list)

# my_list.remove(123) # Remove the first occurrence of an item
# print(my_list)

# my_list.pop() # Remove and return the last item
# print(my_list)

# my_list.extend(my_list2) # Extend the list by appending elements from another list
# print(my_list)

# my_list2.sort() # Sort the list
# print(my_list2)

# my_list.reverse() # Reverse the order of the list
# print(my_list)

# print(my_list.count("surya")) # Count the occurrences of an item

# print(my_list.index("prakash")) # Find the index of the first occurrence of an item

# my_list.copy() # Create a shallow copy of the list
# print(my_list)
# ---------------------------------------------------------------------


# List - Nested Lists
# ---------------------------------------------------------------------

# point = [ [1,2,3],
#           [4,5,6],
#           [7,8,9] ]

# print(point[0]) # Accessing the first sub-list
# print(point[1][2]) # Accessing the third element of the second sub list
# print(point[2][0]) # Accessiing the first element of the third sub-list
# ---------------------------------------------------------------------

# List - Looping through a List
# ---------------------------------------------------------------------

# my_list = ["surya",123,3.23,True,"prakash",5435,False]

# for i in my_list:
#     print(i)
# ---------------------------------------------------------------------

# Tuples
# ---------------------------------------------------------------------

# empty_tuple = ()
# list_data = [1,2,3,4,5]
# tuple_data = (1,2,3,4,5)
# nested_tuple = ((1,2,3), (3,4,5), (5,6,7))

# print(tuple_data[0]) # Accessing the first element
# print(tuple_data[-1]) # Accessing the last element
# print(nested_tuple[1]) # Accessing the second sub-tuple

# Tuple Slicing
# ---------------------------------------------------------------------

# print(tuple_data[1:4]) # From 1 to 3
# print(tuple_data[:5]) # From 0 to 4
# print(tuple_data[::2]) # From 0 to end with a step of 2

# ---------------------------------------------------------------------

# Tuple - Replate tuple items (Tuples are immutable)
# ---------------------------------------------------------------------
# tuple_data[1] = 10 # This will raise an error
# ---------------------------------------------------------------------

# Tuple - Popular Functions
# ---------------------------------------------------------------------

# data = (1, 2, 3, 4, 5)
# list = [1, 2, 3, 4, 5]

# print(len(data))
# print(sorted(data))
# print(sum(data))
# print(max(data))
# print(min(data))
# print(tuple(sorted(list)))

# ---------------------------------------------------------------------

# Tuple - Methods
# ---------------------------------------------------------------------

# data = (1, 2, 3, 4, 5, 2, 3, 2)
# print(data.count(2))
# print(data.index(4))

# ---------------------------------------------------------------------


# Sets
# ---------------------------------------------------------------------

# empty_set = set()
# set_items = {22,4,34,'EW',True,4,22,34,'prakash'}

# print(set_items)
#-- ---------------------------------------------------------------------

# Set - Remove duplicates
# list_data = [1,2,3,4,5,3,2,1,4,5]
# set_data = set(list_data)
# unique_list = list(set_data)
# print(unique_list)

# ---------------------------------------------------------------------

# Set - Common Methods
# data = {1, 2, 3, 4, 5}
# data.add(8)
# print(data)
# data.remove(3)
# print(data)
# data.discard(10) # Does not raise an error if the item does not exist
# print(data)

#-----------------------------------------------------------------------

# # Set - compassions
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a.union(b)) # Union
# print(a.intersection(b)) # Intersection
# print(a.difference(b)) # Difference
# print(a.symmetric_difference(b)) # Symmetric Difference
# print(a.issubset(b)) # Subset
# print(a.issuperset(b)) # Superset

# ---------------------------------------------------------------------

# Set - Popular Functions

# data = {5, 3, 8, 1, 2, 7, 4, 6}

# print(len(data))
# print(sorted(data))
# print(max(data))
# print(min(data))
# print(sum(data))
# # ---------------------------------------------------------------------

# Dictionaries
# ---------------------------------------------------------------------

# empty_dict = {}
# person = {
#     "name": "surya",
#     "age": 21,
#     "city": "mahabubabad",
#     "is_student": True
# }

# print(person['name'])
# print(person['age'])
# print(person.get('city'))
# print(person['is_student'])
# print(person.setdefault('country', 'India'))
# print(person)

# person['age'] = 22
# person['city'] = 'hyderabad'

# print(person)

# ---------------------------------------------------------------------

# # Membership Operators
# print('name' in person)
# print('country' in person)

# ---------------------------------------------------------------------

# print(list(person.keys()))
# print(list(person.values()))
# print(list(person.items()))

# ---------------------------------------------------------------------

# Dictionary - looping through a Dictionary
# for i, j in person.items():
#     print(i,'----',j)

# ---------------------------------------------------------------------

