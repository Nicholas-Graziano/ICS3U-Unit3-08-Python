#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if a number is negative or positive

def main():
    # this program checks if the number is a negative or positive

    # input
    year = print("Enter year")
    year_as_string = input("enter a year: ")
    try:
        year = int(year_as_string)
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("This is a leap year")
            else:
                print("This is not a leap year")
        else:
            print("This is not a leap year")
    except Exception:
        print("This is not a year")


if __name__ == "__main__":
    main()
