import contextlib, time

# @contextlib.contextmanager
# def ef_context_manager():
#     print('---Before---') # Code Before

#     yield

#     print('---After---') # Code After

# with ef_context_manager():
#     print('Inside block') # It Prints at yield place
"""
---Before---
Inside block
---After---
"""

# Before
# start = time.time() 

# # Main code
# for i in range(10000): 
#     print(f'Print Statement #{i}')

# # After
# end = time.time()
# timer = end - start
# print(f'Time token: {timer }s')

# @contextlib.contextmanager
# def time_it():
#     start = time.time() # Before
#     yield
#     end = time.time() # After
#     timer = end - start
#     print(f'Time Taken: {timer}s')

# # Loop
# with time_it():
#     result =[]
#     for i in range(100000):
#         result.append(i * 2)

# # Comprehension
# with time_it():
#     result = [i * 2 for i in range(100000)]



