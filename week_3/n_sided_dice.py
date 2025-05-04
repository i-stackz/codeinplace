import random

def main():
    dice_sides = input("How many sides does your dice have? ");
    your_roll = random.randint(1, int(dice_sides));
    print(f"Your roll is {your_roll}");

if __name__ == '__main__':
    main()
