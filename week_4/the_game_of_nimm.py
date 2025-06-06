def main():
    """
    You should write your code here. 
    """
    number_of_stones = 20
    turn = 0

    while number_of_stones > 0:
        print(f"There are {number_of_stones} stones left.")
        if turn % 2 == 0:
            stones_to_remove = input("Player 1 would you like to remove 1 or 2 stones? ")
            while stones_to_remove not in ("1", "2"):
                stones_to_remove = input("Please enter 1 or 2: ")
            print()
                
        else:
            stones_to_remove = input("Player 2 would you like to remove 1 or 2 stones? ")
            while stones_to_remove not in ("1", "2"):
                stones_to_remove = input("Please enter 1 or 2: ")
            print()
                
        stones_to_remove = int(stones_to_remove)
        number_of_stones = number_of_stones - stones_to_remove
        turn += 1

        if number_of_stones == 0:
            if turn % 2 == 0:
                print("Player 1 wins!")
                break
            else:
                print("Player 2 wins!")
                break

if __name__ == '__main__':
    main()
