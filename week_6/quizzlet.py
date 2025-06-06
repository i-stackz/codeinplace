def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    dict_length = len(translations)
    counter = 0

    for key in translations:
        value = translations[key]
        answer1 = input(f"What is the Spanish translation for {key}?")

        if answer1 == value:
            print(f"That is correct!\n")
            counter = counter + 1

        else:
            print(f"That is incorrect, the Spanish translation for {key} is {value}.\n")


    print(f"You got {str(counter)}/{str(dict_length)} words correct, come study again soon!")

if __name__ == '__main__':
    main()
