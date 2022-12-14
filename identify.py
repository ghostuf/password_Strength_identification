import random
import string

In_pass = input("Enter a password to be ranked: ")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = string.punctuation


def rank():
    presence_lower = False
    presence_upper = False
    presence_number = False
    presence_symbols = False
    count = 0
    total = 0

    for i in range(0, len(In_pass)):
        for j in range(0, len(lower)):
            if In_pass[i] == lower[j]:
                presence_lower = True

    if presence_lower:
        count += 1
        total += count
        count = 0

    for i in range(0, len(In_pass)):
        for j in range(0, len(upper)):
            if In_pass[i] == upper[j]:
                presence_upper = True

    if presence_upper:
        count += 1
        total += count
        count = 0

    for i in range(0, len(In_pass)):
        for j in range(0, len(numbers)):
            if In_pass[i] == numbers[j]:
                presence_number = True

    if presence_number:
        count += 1
        total += count
        count = 0

    for i in range(0, len(In_pass)):
        for j in range(0, len(symbols)):
            if In_pass[i] == symbols[j]:
                presence_symbols = True

    if presence_symbols:
        count += 1
        total += count
        count = 0

    if total < 3 and len(In_pass) < 8:
        return "POOR PASSWORD!"
    elif total == 3 and (len(In_pass) >= 8 and len(In_pass) <= 10):
        return "MID PASSWORD!"
    elif total == 4 and (len(In_pass) > 10):
        return "STRONG PASSWORD!"
    else:
        return "Bruh"


ranking = rank()
print(ranking)
