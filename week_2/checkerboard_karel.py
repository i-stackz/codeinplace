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
    while front_is_clear() and facing_east():
        if no_beepers_present():
            put_beeper()
            move()
            if front_is_blocked() and facing_east():
                turn_left()
                move()
                turn_left()

                while facing_west() and front_is_clear():
                    if no_beepers_present():
                        put_beeper()
                        move()
                        if facing_west() and front_is_blocked():
                            turn_right()
                            if facing_north() and front_is_blocked():
                                turn_left()
                                turn_left()
                                while facing_south() and front_is_clear():
                                    move()
                                if facing_south() and front_is_blocked():
                                    turn_left()
                            else:
                                move()
                                if facing_north() and front_is_clear():
                                    turn_right()
                        else:
                            move()
            else:
                move()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()

# NOTE: she successfully passes the first level (6x6), however she seems to fail at the layout of the other levels (3x5 and 3x1)... 
