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


    if count == 4 and len(In_pass) > 10:
        return "Strong_Password!"
    elif len(In_pass) >= 8 and len(In_pass) <= 10:
        return "Moderate_Password!"
    elif len(In_pass) < 8:
        return "Weak_Password!"

    if count == 3 and (len(In_pass) >= 8 and len(In_pass) <= 10):
        return "Moderate_Password!"
    elif len(In_pass) < 8:
        return "Weak_Password!"

    else:
        return "Weak_password!"


ranking = rank()
print(ranking)