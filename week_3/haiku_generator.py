from ai import call_gpt

def main():
    # TODO: your code here
    name = input("Enter your name: ");
    topic = input("Enter a topic: ");

    response = call_gpt(f"Please create a 3 line haiku. The haiku should be three lines long. The first line should have 5 syllables, the second 7 syllables, and the third line 5 syllables. Use the name given and base the haiku off of the topic given. the name is {name} and the topic is {topic}");
    
    print("Creating your haiku...");
    print(f"{response}");


if __name__ == "__main__":
    main()

# note this lesson had a chatgpt api key already generated and plugged in for us.
