def main():
    number_list = load_numbers_from_file("numbers.txt")
    # TODO: your code here
    list_length = len(number_list)
    number = 0
    number = float(number)

    for i in number_list:
        number = float(i) + number

    average = get_average(number, list_length)

    print(f"Average: {average}")


def get_average(num1, num2):
    return num1 / num2



def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers


if __name__ == '__main__':
    main()

