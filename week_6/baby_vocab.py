def main():
    words = load_words_from_file("words.txt")
    # TODO: your code here :)


    # method of removing duplicates from a list. source: https://www.w3schools.com/python/python_howto_remove_duplicates.asp
    new_list = list(dict.fromkeys(words))

    for word in new_list:
        print(f"{word}" + "\t : " + ("x" * words.count(word)))



    ''' 
    # complex solution NOTE: ChatGPT showed me how to do it using two for loops and a boolean flag
    words_len = len(words)
    new_list = []

    for index in range(words_len):
        word_check = False
        new_list_len = len(new_list)

        for index1 in range(new_list_len):
            if words[index] == new_list[index1]:
                word_check = True
                break
        
        if word_check == False:
            new_list.append(words[index])
            
    list_len = len(new_list)

    for index2 in range(list_len):
        print(f"{new_list[index2]}" + "\t : " + ("x" * words.count(new_list[index2])))
    '''

        
    """ 
    # simple solution NOTE: ChatGPT showed me the set function
    for i in set(words):
        count = words.count(i)
        print(f"{i}" + "\t : " + ("x" * count))
    """


def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words


if __name__ == '__main__':
    main()

