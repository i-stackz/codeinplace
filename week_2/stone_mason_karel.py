from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    build_column()
    cross_over()
    build_opposite()
    cross_over()
    build_column()
    cross_over()
    build_opposite()
    

def build_column():
    if facing_east():
        turn_left()
        put_beeper()
        move()
        put_beeper()
        move()
        put_beeper()
        move()
        put_beeper()
        move()
        put_beeper()
        turn_right()

def build_opposite():
    if not_facing_north():
        turn_right()
        put_beeper()
        move()
        put_beeper()
        move()
        put_beeper()
        move()
        put_beeper()
        move()
        put_beeper()
        turn_left()

    
    if facing_north():
        turn_right()

def cross_over():
    if facing_east() and front_is_clear():
        for i in range(4):
            move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
