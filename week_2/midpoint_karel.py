from karel.stanfordkarel import *


"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        move()
        if front_is_blocked():
            turn_back()




def turn_back():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()

# NOTE: I am stuck trying to figure out how to have karel determine where the midpoint is. Right now she just loops around indefinitely.
