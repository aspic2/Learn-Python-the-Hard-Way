#centralize the quiz functions and just import appropriate dicts
#revisit commandline arguments. find way to input dictionaries from there
'''functions/processes for this script:
    import dict(s)
    function: make list from dicts
        return list or Error
    function: pull random question from list
        return question or Error
    function: request input from user
        return input or Error
    function: evaluate user input and question
        increment points or move on
    function: exit game
        at end of turns or when user prompts exit
'''


from ex37 import full_dict
import random
from sys import exit


session_dict = full_dict

def listmaker(source_dict):
    newlist = []
    for key in source_dict:
        newlist.append(key)
    return newlist

sessionlist = listmaker(session_dict)

question = None

def questionmaker(x):
    global question
    question = random.choice(x)
    print(question)
    return question


def finished(explanation):
    print(explanation, "\nThanks for playing!")
    exit(0)

def answerfunction():
    answer = input("> ")
    if answer == 'Q' or answer == 'q':
        finished("Closing program...")
    else:
        return answer


def quizzical(scoring):
    print("Time to test your knowledge!")
    print("Follow the prompts on the screen or type 'q' to quit.")
    turns = input("How many turns would you like?\n> ")
    if turns == 'Q' or turns == 'q':
        finished("User quit")
    else:
        try:
            turns = int(turns)
        except Exception as e:
            print("Please enter a whole number.")
#is there a way to get this value to reflect the original?
            quizzical(False)
    points = 0
    gameround = 1
    while gameround <= turns:
        print("-" * 15, "\n\nRound %d" % gameround)
        print("Please define the following value or command:")
        questionmaker(sessionlist)
        answerfunction()
        if scoring == True:
            if answer == question:
                points += 1
                print("That is correct! Nice work!")
            else:
                print("Sorry, that is incorrect.")
        else:
            print("Here is the correct answer:")
            print(session_dict[question])
        gameround += 1
        print("\nHere's your standing:\n%d turns\n%d points" % (turns, points))
    finished("\n\nFinished all rounds!")

if __name__ == '__main__':
    quizzical(False)
