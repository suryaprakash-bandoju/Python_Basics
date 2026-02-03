# PS: Not Recommended
# -------------------------------------------------------------------------------------------
# filename = 'example.txt'
# file     = open(filename, 'r') # Open
# content  = file.read()         # Read
# print(content)
# file.close()                   # Close

# Read Text Files
# -------------------------------------------------------------------------------------------
# filename = 'example.txt'

# with open(filename, 'r') as f:
#     content = file.read(f)
#     print(content)

# Read Line by Line
# -------------------------------------------------------------------------------------------
# filename = "example.txt"

# with open(filename, 'r') as f:
#     content = f.read()

#     for n, line in enumerate(content.splitlines()):
#         print(n, line)

# Append Text
# -------------------------------------------------------------------------------------------
# filename = 'example.txt'
# with open(filename, 'a') as f:
#     # content = f.read()  # Error: io.UnsupportedOperation: not readable
#     f.write('Hello World\n')
#     f.write('Hello World\n')
#     f.write('Hello World\n')
#     f.write('Hello World\n')


# Write Files
# -------------------------------------------------------------------------------------------
# filename = 'example.txt'
# with open(filename, 'w') as f:
#     f.write('hello world\n')
#     f.write('hello world\n')
#     f.write('hello world\n')
#     f.write('hello world\n')
#     f.write('hello world\n')
#     f.write('hello world\n')
