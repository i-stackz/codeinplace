import random

NUM_PAIRS = 3

def main():

    """
    You should write your code here. Make sure to delete 
    the 'pass' line before starting to write your own code.
    """

    # Milestone #1
    truth = []
    for number in range(NUM_PAIRS):
        truth.append(number)
        truth.append(number)

    #print(truth)

    # Milestone #2
    random.shuffle(truth)
    
    #print(truth)

    # Milestone #3
    myList = []

    for number in range(len(truth)):
        myList.append("*")

    """ 1st try
    print(myList)

    # Milestone #4
    userIndex1 = get_valid_index()
    userIndex2 = get_valid_index()

    # logic
    if userIndex1 == userIndex2:
        print("You entered the same index twice. Try again.")

    # Milestone #5

    if truth[userIndex1] == userIndex1 and truth[userIndex2] == userIndex2:
        print("Match!")
        myList[userIndex1] = userIndex1
        myList[userIndex2] = userIndex2
        clear_terminal()
    else:
        print(f"Value at index {userIndex1} is {truth[userIndex1]}")
        print(f"Value at index {userIndex2} is {truth[userIndex2]}")
        print("No match. Try again.")
        input("Press Enter to continue...")
    """

    # Milestone #6
    counter = 0

    while counter != 3:
        print(myList)
        
        userIndex1 = get_valid_index()
        userIndex2 = get_valid_index()

        if userIndex1 == userIndex2:
            print("You entered the same index twice. Try again.")

        if truth[userIndex1] == truth[userIndex2]:
            print("Match!")
            counter = counter + 1
            myList[userIndex1] = truth[userIndex1]
            myList[userIndex2] = truth[userIndex2]
            clear_terminal()
        else:
            print(f"Value at index {userIndex1} is {truth[userIndex1]}")
            print(f"Value at index {userIndex2} is {truth[userIndex2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")

    print(myList)
    print("Congratulations! You won!")

# custom fucntion
def get_valid_index():
    while True:
        index = input(f"Enter an index: ")

        try:
            index = int(index)

            if index < 0 or index > 5:
                print("Invalid index. Try again.")
            else:
                return index
        except ValueError:
            print("Not a number. Try again.")

def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()
