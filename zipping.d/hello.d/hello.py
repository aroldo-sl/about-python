from deps import greeting, click

def main():
    greeting.say_hello()
    print(click.__file__)
if __name__=="__main__":
    main()
