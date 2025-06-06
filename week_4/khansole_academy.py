import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    number1 = random.randint(10, 99);
    number2 = random.randint(10, 99);
    answer = number1 + number2;

    print(f"What is {number1} + {number2}?");
    useranswer = input("Your answer: ")
    useranswer = int(useranswer);
    #print(f"Your answer: {answer}");

    if useranswer == answer:
        print("Correct!");
    elif useranswer != answer:
        print("Incorrect.");
        print(f"The expected answer is {answer}");
    

    
    
if __name__ == '__main__':
    main()
