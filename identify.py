import random
import string

In_pass = input("Enter a password to be ranked: ")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = string.punctuation


def rank():

    count = 0

    for i in range(len(In_pass)):
        if In_pass[i] in lower:
            count += 1
            break

    for i in range(len(In_pass)):
        if In_pass[i] in upper:
            count += 1
            break

    for i in range(len(In_pass)):
        if In_pass[i] in numbers:
            count += 1
            break

    for i in range(len(In_pass)):
        if In_pass[i] in symbols:
            count += 1
            break

    if count < 3:
        if len(In_pass) < 8:
            return "Weak Password!"
        else:
            return "Weak Password!"

    if count == 3:
        if (len(In_pass) >= 8 and len(In_pass) <= 10):
            return "Moderate Password!"
        else:
            return "Moderate Password!"

    if count == 4:
        if len(In_pass) > 10:
            return "Strong Password!"
        else:
            return "Strong Password!"


ranking = rank()
print(ranking)