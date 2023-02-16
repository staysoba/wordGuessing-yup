import random 

def main():
    file = open("wordlist", "r")
    allthelinesinthefile = file.readlines()
    file.close()

    words = ["process", "thread", "forks", "signal"] 

    selectedword = allthelinesinthefile[random.randint(0, len(allthelinesinthefile) - 1)] .strip()
    selectedword ="process"
    attempts = 2
    truthTracker = False
    winingTracker = False

    # creating our mask, its goona be as long as our selectedWord

    mask = []

    for char in selectedword:
        mask.append(False)

    # game loop, it will not end until number of guesss are 0 or game is won.
    while attempts != 0 and not winingTracker:
        # printing attempts left
        print("you have {} attempts left" .format(attempts))
        for index, char in enumerate(selectedword):
            if mask [index]:
                print(char, end=" ")
            else:
                print("_", end= " ")
        print()

    # guessing the character
        userInput = input("guess a character > ")

        if len(userInput) > 1 or not userInput.isalpha():
            # print("you gave a bad input, you bad bad person")
            continue
            

    # for checking if they guess a charcater incorrectly
        for index, char in enumerate(selectedword):
            if userInput == char:
                mask[index] = True
                truthTracker = True
                # TODO gotta add code.
    # check if each itme in the hidden word is true or
        for item in mask:
            print(item)
            if not item:
                winingTracker = False
                # print("setting win tracker to false, then breaking out")
                break
                # print("did you break out") # will not work or print because its after the breaking point code, the "break" will not allow it to print because it loops back up
            else:
                winingTracker = True
                print("set winning tracker to true")

        if not truthTracker:
            attempts = attempts - 1

    # printing if we won or not
    if winingTracker:
        print("you won")
    else:
        print("you lost")


    name = ""
    while not name.isalpha():
        print("enter name to be on the highscore list")
        name = input("enter > ")

        if not name.isalpha():
            print("you gave teh name in a bad input")

    file = open("saved", "a")
    file.write("{},{}".format(name, scoreCurrent))
    file.close()
main()
            

        



   

