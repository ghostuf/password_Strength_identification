import random
import string
import time


def rank(psw):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = string.punctuation

    count = 0

    for i in range(len(psw)):
        if psw[i] in lower:
            count += 1
            break

    for i in range(len(psw)):
        if psw[i] in upper:
            count += 1
            break

    for i in range(len(psw)):
        if psw[i] in numbers:
            count += 1
            break

    for i in range(len(psw)):
        if psw[i] in symbols:
            count += 1
            break

    if count == 4 and (len(psw) > 10):
        return " Strong_Password!"
    elif count == 3 and (len(psw) >= 8 and len(psw) >= 10):
        return "Moderate_Password!"
    elif count < 3 and len(psw) < 8:
        return "Weak_Password!"

    if count == 3 and (len(psw) >= 8 and len(psw) >= 10):
        return "Moderate_Password!"
    elif count < 3 and len(psw) < 8:
        return "Weak_Password!"

    else:
        return "Weak_Password!"


def option1():
    while True:
        print('#' * 80)
        print("\nWould you like to use a custom file or a premade file?[C/P], press F to exit!")

        ans = input("Your answer:")
        if ans.lower() == "c" or ans.lower() == "p":
            if ans.lower() == "c":
                print("Enter the path of file:")
                try:
                    fp = input("path *must be accurate and a text file!*: ")

                    with open(fp, "r") as file:
                        a = file.read().split()

                        for i in a:
                            ur_pw = i.split(",")
                            user = ur_pw[0]
                            passw = ur_pw[1]
                            strength = rank(passw)

                            with open("check.txt", "a")as f1:
                                f1.write(user + " - " + passw + " - " + strength + "\n")
                        print("Strengths successfully identified and stored in 'check.txt'!")

                except FileNotFoundError:
                    print("No such file found!")
                    continue
                break

            elif ans.lower() == "p":
                with open("Uspw.txt", "r") as file1:
                    a = file1.read().split()

                    for i in a:
                        us_pw = i.split(",")
                        username = us_pw[0]
                        password = us_pw[1]
                        strength1 = rank(password)

                        with open("check.txt", "a") as f2:
                            f2.write(username + " - " + password + " -"  + strength1 + "\n")
                    print("Strengths successfully identified and stored in 'check.txt'!")

                break

        elif ans.lower() == "f":
            break
        else:
            print("Please Choose among 'c' and 'p'")
            pass


def option2():
    def generate():
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = string.punctuation

        l1 = "".join(random.sample(lower, 3))
        l2 = "".join(random.sample(upper, 3))
        l3 = "".join(random.sample(numbers, 3))
        l4 = "".join(random.sample(symbols, 3))
        total = l1 + l2 + l3 + l4
        password = total

        return password

    while True:
        print("Would you like to generate a new password?[y/n]: or press F to exit")
        say = input("choice[y/n]: ")
        if say.lower() == "y" or say.lower() == "n":
            if say.lower() == "y":
                name = input("Enter new username: ")
                print("--Computing new password--")
                newpass = generate()
                time.sleep(2)
                print("{}, We have created your new Strong strength password!\n New_Password: {}".format(name, newpass))
                print("Would you like to save it in the rankings file?[y/n]: ")
                say1 = input("Ans:")
                while True:
                    if say1.lower() == "y" or say1.lower() == "n" or say1.lower() == "f":
                        if say1.lower() == "y":
                            ranking = rank(newpass)
                            with open("check.txt", "a") as file:
                                file.write(name + " - " + newpass + " - " + ranking)
                                print("Successfully saved!")
                                break
                        else:
                            print("Well use it somewhere!")
                            break

                    if say1.lower() == "f":
                        break

                    else:
                        print("Enter a valid response 'y' or 'n'")
                        pass
            else:
                break

        elif say.lower() == "f":
            break

        else:
            print("Enter either 'y' or 'n'")


def main():
    print('Welcome to my password ranking program')
    while True:
        print('*' * 40)
        print('Please select one of 3 options')
        print('1. Rank password from an existing file\n2. Generate a strong password \n3. exit the program')
        print('*' * 40)
        try:
            inp = int(input("Enter your option here:"))
            if inp == 1:
                option1()

            elif inp == 2:
                option2()

            elif inp == 3:
                break
            else:
                print("Choose a valid Option!")
                pass
        except ValueError:
            print("Choose a valid Option!")
            pass

main()
print("Thanks for using this program.")