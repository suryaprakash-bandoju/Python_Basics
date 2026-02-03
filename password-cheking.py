# Taking inputs from User
username = input("Enter username: ")
passward = input("Enter password: ")

# Checking security
symbols = "~!@#$%^&*()_+=-[]{};:|\/.,<>"
check_length = False
check_spaces = False
check_digit = False
check_lower = False
check_upper = False
check_special = False

# Checking length
if len(passward) >= 8:
    check_length = True

# Cheking Spaces
if " " not in passward:
    check_spaces = True

for char in passward:

# Checking Upper Case
    if char.isupper():
        check_upper = True
# Checking Lower Case
    if char.islower():
        check_lower = True
# Cheking Digit
    if char.isdigit():
        check_digit = True
# Cheking Symbols
    if char in symbols:
        check_special = True

checks = [
    check_special,
    check_digit,
    check_length,
    check_lower,
    check_spaces,
    check_upper,
]

# Printing the Result

if all(checks):
    print("Account Created Successfully.")

else:
    print("Account is not Secure.")

    if not check_length:
        print("Use at least 8 characters.")

    if not check_spaces:
        print("Don't use Spaces.")

    if not check_digit:
        print("use at least 1 digit.")

    if not check_lower:
        print("use at least 1 lower letter.")

    if not check_upper:
        print("use at least 1 upper letter.")

    if not check_special:
        print(f"use at least 1 speacial character - {symbols}.")