"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
from random import randint
import base64


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """

    if num % 2 == 0:
        print("even!")
    else:
        print("odd!")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """

    number = randint(1, 9)

    while True:
        guess = raw_input("Guess: ")

        if guess == "exit":
            break
        else:
            guess = int(guess)

            if guess == number:
                print("You got it.")
                break
            elif guess > number:
                print("Too high")
            elif guess < number:
                print("Too low")    



def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """

    print(string == string[::-1])


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """

    username_encrypted = base64.b64encode(bytes(username))
    password_encrypted = base64.b64encode(bytes(password))

    with open(filename, "w") as f:
        f.write(username_encrypted + "\n")
        f.write(password_encrypted + "\n")


def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f = open(filename, "r")
    lines = f.readlines()
    read_user = lines[0][:-1]
    read_pass = lines[1][:-1]

    if password == None:    
        print("Username: " + base64.b64decode(bytes(read_user)))
        print("Password: " + base64.b64decode(bytes(read_pass)))
    else:
        username_encrypted = read_user
        password_encrypted = base64.b64encode(bytes(password))

        print("Username: " + base64.b64decode(bytes(read_user)))
        print("Password: " + password)

if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
