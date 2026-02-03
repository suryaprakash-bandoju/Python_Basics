# Learn about Input and Data Conversion
# ---------------------------------------------------------------------

num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

total = num_1 + num_2
div = num_1 / num_2
sub = num_1 - num_2
mul = num_1 * num_2
mod = num_1 % num_2
results = {
    'Addition': total,
    'Division': div,
    'Subtraction': sub,
    'Multiplication': mul,
    'Modulus': mod
}
for i,j in results.items():
    print(f"{i}: {j}")