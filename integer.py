#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Oct/18/2023
# This program allows for the user to input an integer and my program will output if it is positive, negative or 0.


def main():
    # Declaring variable and getting the user input.
    user_number = int(input("Enter an integer: "))

    # Using If condition for positive integers.
    if user_number > 0:
        print("{} is positive.".format(user_number))

    # Using Elif condition for negative integers.
    elif user_number < 0:
        print("{} is negative.".format(user_number))

    # Using Else condition for the integer 0.
    else:
        print("Your number is 0.")


if __name__ == "__main__":
    main()
