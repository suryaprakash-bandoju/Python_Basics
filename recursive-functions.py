# # Factorial 

# def factorials(n):
#     if n == 0:
#         return 1
    
#     return n * factorials(n - 1)

# print(factorials(5))


# number = int(input())
# while number >= 10:
#     total = 0
#     while number > 0:
#         digit = number % 10
#         total += digit
#         number //= 10
#     number = total
# print(number)


def digit_sum(n):
    if n < 10:
        return n
    else:
        return 1 + ((n -1) % 9)

print(digit_sum(555))