# Loops in Python
# container = [1,2,3,5,4]

# for i in container:
#     print(i)

# ===============================================================================================#
# For loops with Lists
# ===============================================================================================#
# list_materials = ['wood', 'steel', 'glass', 'bricks']

# for mat in list_materials:
#     # print(mat)
#     print(f"{mat.lower()} ---- {mat.upper()}")

# ===============================================================================================#
# For loop with Strings
# ===============================================================================================#
# for char in "Hello, Welcome to my World":
#     print(f"{char.lower()} ---- {char.upper()}")

# ===============================================================================================#
# For loop with Numbers
# ===============================================================================================#
# big_number = 123456789

# for str_num in str(big_number):
#     num  = int(str_num)
#     sq   = num**2
#     cube = num**3
#     print(num, sq, cube)

# ===============================================================================================#
# For Loop with Range
# ===============================================================================================#
# for i in range(11):
#     print(i)
#     print(f"Hello World")


# floor_plants = []

# for i in range(1, 11):
#     floor_plants.append(f"Floor Plants_{i}")

# print(floor_plants)

# ===============================================================================================#
# For Loop over Dict
# ===============================================================================================#
# my_dict = {'key1': 'value1',
#             'key2': 'value2',
#             'key3': 'value3',
#             'key4': 'value4'
#             }

# for i in my_dict:
#     print(i) # Key1....

# for i in my_dict.values():
#     print(i) # value1......

# for i, j in my_dict.items():
#     print(f"{i} ---- {j}")

# ===============================================================================================#
# Break out of Loops
# ===============================================================================================#
# nums = [1,2,4,5,6,7,8,9,7,6,4,3]

# for i in nums:
#     if i%2 == 0 and i!=0:
#         print(f"First Even number is: {i}")
#         break # Stop the loop at here
# print("Finished...!")

# ===============================================================================================#
# Continue out of Loops
# ===============================================================================================#
# real_money = [10,20,30,40,50]
# wallet = [10,30,25,20,40,50]

# total = 0
# for notes in wallet:
#     if notes not in real_money:
#         continue
#     total += notes
# print(f"Total: {total} RUP")

# ===============================================================================================#
# Nested Loops
# ===============================================================================================#
# course = [
#     ["Lesson_01.01", "Lesson_01.02", "Lesson_01.03", "Lesson_01.04"],
#     ["Lesson_02.01", "Lesson_02.02", "Lesson_02.03"],
#     ["Lesson_03.01", "Lesson_03.02"],
# ]

# for module in course:
#     print(f'Starting Module: {module}')

#     for lesson in module:
#         print(f'Completed: {lesson}.')

#     print('Module is Complete!')
#     print('-'*10)

# ===============================================================================================#
# While Loop
# ===============================================================================================#
# count = 0
# while True:
#     if count == 10:
#         break

#     print(count)
#     count += 1


# tickets = 100

# while True:
#     n = int(input("Buy tickets: "))
    
#     if tickets - n < 0:
#         print('Not enough tickets. Try again')
#         continue

#     tickets -= n
#     print(f'Tickets left: {tickets}')

#     if tickets == 0:
#         print('Tickets Sold Out!')
#         break