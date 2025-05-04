"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    # your code here
    first = input("Enter first number: ")
    second = input("Enter second number: ")
    total = int(first) * int(second)
    print(total)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
