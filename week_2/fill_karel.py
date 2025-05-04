from karel.stanfordkarel import *


"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while left_is_clear():
        move_to_wall()
        reset_to_next_row()
    move_to_wall()

   
def move_to_wall():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
        clear_corner()

def clear_corner():
    if no_beepers_present():
        put_beeper()

def turn_around():
    for i in range(2):
        turn_left()

def reset_to_next_row():
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
