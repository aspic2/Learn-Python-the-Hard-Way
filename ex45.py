#You make a game.
#Currently gets from beginning to end, but is boring. Add more logic
'''Make a game with more than one way to reach the end.

Title: Making it through the day

Premise: Perform a series of daily actions, and have the character survive.

Objects

Characters:
    player
    antagonists?
        wife
        workplace bully

Scenes:
    Home
      Bedroom
      Kitchen
      Garage
    Public Trans
    Workplace
      Desk
      Lunchroom
    Gym
    Jail
    Death
'''

import random
from sys import exit


class Character(object):
    name = None
    health = 100


class Protagonist(Character):
    def __init__(self, name):
        self.health = 50
        #name = input("What is your name?\n> ")
        print("Hello, %s. You have been initialized." % name)


class Scene(object):
    def __init__(self):
        self.description = description
        self.been_here = False

    def enter_scene():
        pass


class Death(Scene):

    def enter_scene():
        print("You up?\nYa dead.")
        exit(0)


class Home(Scene):
    description = "Your home. Your hallway."
    been_here = False

    def enter_scene():
        print(Home.description)
        return Home.decision_time()

    def decision_time():
        decision = input("Eat (kitchen), go straight to work, or back to bed?")
        if "work" in decision or "out" in dicision:
            return Garage.enter_scene()

    #returns only home locations
    #return Bedroom
    #return Kitchen
    #return Garage


class Bedroom(Scene):
    description = ("This is your bedroom.",
    "You awake to a bean of sunrise on your face.",
    "Someone didn't close the blinds last night.",
    "You sit up to find your room a mess. Not out of the ordinary."
    ending = False

    def enter_scene():
        print(Bedroom.description)
        return Bedroom.decision_time()

    def decision_time():
        print("Add first logic branch here.")
        decision = input("What next?\n> ")
        return Home.enter_scene()

class Kitchen(Scene):
    description = ("You are starving!", "Why don't you make yourself something to eat?", "You will need your strength today.")
    been_here = False

    def enter_scene():
        for line in description:
            print(line)
        decision = input("Do you cook something or leave?\n> ")
        if "cook" in decision:
            Protagonist.health = 100
        else:
            return Home.enter_scene()


class Bed(Scene):
    description = "Time for Bed"

    def enter_scene():
        print(Bed.description)
        exit(0)


class Kitchen(Scene):
    description = "This is the kitchen."

    def enter_scene():
        print(Kitchen.description)
        return Kitchen.decision_time()

    def decision_time():
        print("Add logic here.")
        return Garage.enter_scene()


class Garage(Scene):
    description = 'This is the garage.'
    been_here = False

    def enter_scene():
        print(Garage.description)
        if Garage.been_here:
            print("Welcome Home")
            return Home.enter_scene()
        print("Time to head out!")
        Garage.been_here = True
        return PublicTrans.enter_scene()




class PublicTrans(Scene):
    description = "Everyone loves public transportation!"
    been_here = False

    def enter_scene():
        print(PublicTrans.description)
        return PublicTrans.decision_time()

    def decision_time():
        if PublicTrans.been_here:
            print("What a day it has been!")
            decision = input("Want to head home or to the gym?\n> ")
            return Bed.enter_scene()
        print("Add logic branch here.")
        decision = input("What next?\n> ")
        PublicTrans.been_here = True
        return Workplace.enter_scene()

    #return Home
    #return Gym
    #return Workplace


class Workplace(Scene):
    description = "This is your workplace."

    def enter_scene():
        print(Workplace.description)
        print("Workplace decisions. Do work or not. Eat lunch out or in cafeteria. etc.")
        return Workplace.decision_time()

    def decision_time():
        print("You are at your desk. You see 300 new emails in your inbox.")
        decision = input("Do you get to work or ignore your duties?\n> ")
        return PublicTrans.enter_scene()
    #return Desk
    #return Lunchroom



class Gameplay(object):
    def __init__(self, first_scene):
        self.first_scene = first_scene
        self.last_scene = Bed

    def play(self):
        print("-" * 50)
        print("ONE DAY AT A TIME")
        current_scene = self.first_scene
        final = self.last_scene
        while current_scene != final:
            current_scene = current_scene.enter_scene()



protag = Protagonist('Michael')

new_game = Gameplay(Bedroom)
new_game.play()
