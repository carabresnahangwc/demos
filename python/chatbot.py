# --- Define your functions below! ---
def intro():
    print("Welcome to ChatBot!")
    print("All you have to do is respond to my prompts and hit enter!")
    name = input("What is you name?  ")
    return name

def hello(text):
    text.lower()
    if text == "hello" or text == "hi" or text == "yes":
        print("Salutations!")

# --- Put your main program below! ---
def main():
    name = intro()
    print("Hello, ", name)
    #greeting = input("(say hello back?)")
    #hello(greeting)
    while True:
        answer = input("What do you want to talk about?")
        print("That's cool!")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
