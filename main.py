# Find the ones, tens, hundreds and thousands digits in Python

number = 3217

# ✅ Get ones, tens, hundreds and thousands

ones = number % 10
print(ones)  # 👉️ 7

tens = (number % 100) // 10
print(tens)  # 👉️ 1

hundreds = (number % 1000) // 100
print(hundreds)  # 👉️ 2

thousands = number // 1000
print(thousands)  # 👉️ 3

# -----------------------------------------------------

# ✅ Get ones, tens, hundreds and thousands in a list

result = [int(digit) for digit in str(number)[::-1]]
print(result)  # 👉️ [7, 1, 2, 3]