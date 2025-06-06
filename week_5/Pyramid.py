from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base




def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Start at the bottom of the canvas
    bottom_y = CANVAS_HEIGHT
    top_y = bottom_y - BRICK_HEIGHT

    counter = BRICKS_IN_BASE  # Bricks in current row

    while counter >= 1:
        # Compute total width of current row of bricks
        row_width = counter * BRICK_WIDTH

        # Center the row horizontally
        left_x = (CANVAS_WIDTH - row_width) // 2
        right_x = left_x + BRICK_WIDTH

        for i in range(counter):
            canvas.create_rectangle(
                left_x,
                top_y,
                right_x,
                bottom_y,
                "yellow",
                "black"
            )
            left_x = right_x
            right_x = right_x + BRICK_WIDTH

        # Prepare for next layer (up one level, one fewer brick)
        counter -= 1
        bottom_y = top_y
        top_y -= BRICK_HEIGHT


# NOTE: needed the help of ChatGPT for the last brick my code always finished the pyramid with two bricks at the top...

""" my code
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here
    
    # variables
    center = CANVAS_WIDTH // 4
    left_x = center - 60  # x1
    starting_brick = left_x
    top_y = CANVAS_HEIGHT - BRICK_HEIGHT # y1
    right_x = left_x + BRICK_WIDTH # x2
    bottom_y = CANVAS_HEIGHT # y2

    
    counter = BRICKS_IN_BASE

    while counter >= 1:
        layer = (BRICKS_IN_BASE - counter) // 2
        left_x = starting_brick + layer * BRICK_WIDTH
        right_x = left_x + BRICK_WIDTH

        for i in range(counter):
            canvas.create_rectangle(
                left_x,
                top_y,
                right_x,
                bottom_y,
                "yellow",
                "black"
            )
            left_x = right_x
            right_x = right_x + BRICK_WIDTH
        counter = counter - 2
        bottom_y = top_y
        top_y = top_y - BRICK_HEIGHT
        


    canvas.create_rectangle(
        left_x,
        top_y,
        right_x,
        bottom_y,
        "yellow",
        "black"
    )

    left_x = right_x
    right_x = right_x + BRICK_WIDTH

    canvas.create_rectangle(
        left_x,
        top_y,
        right_x,
        bottom_y,
        'yellow',
        'black'
    )
    
    for i in range(BRICKS_IN_BASE):
        canvas.create_rectangle(
            left_x,
            top_y,
            right_x,
            bottom_y,
            "yellow",
            "black"
        )

        left_x = right_x
        right_x = right_x + BRICK_WIDTH

    left_x = 120
    top_y =  286 - 12
    right_x = 150
    bottom_y = 286

    for i in range(BRICKS_IN_BASE - 2):
        canvas.create_rectangle(
            left_x,
            top_y,
            right_x,
            bottom_y,
            "yellow",
            "black"
        )

        left_x = right_x
        right_x = right_x + BRICK_WIDTH

    def get_coords():
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()

        print(f"y = {y} x = {x}")

    while True:
        get_coords()
"""

if __name__ == '__main__':
    main()
