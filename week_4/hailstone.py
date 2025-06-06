"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    # your code here
    n = input("Enter a number: ")
    n = int(n)

    while n != 1:
        if n % 2 == 0:
            print(f"{n} is even, so I take half: {(n // 2)}")
            n = n // 2
        else:
            print(f"{n} is odd, so I make 3n + 1: {((3 * n) + 1)}")
            n = (3 * n) + 1

if __name__ == "__main__":
    main()
