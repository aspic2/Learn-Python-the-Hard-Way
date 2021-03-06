#Gothons from Planet Percal #25.
#Finished game with quit function and error handling.

'''
Aliens have invaded a space ship and our hero has to go through a
 maze of rooms defeating them so he can escape into an escape pod to
 the planet below. The game will be more like a Zork or Adventure type
 game with text outputs and funny ways to die. The game will involve
 an engine that runs a map full of rooms or scenes. Each room will
 print its own description when the player enters it and then tell the
 engine what room to run next out of the map.
 '''

from sys import exit
import random

class Scene(object):

    def __init__(self):
        self.completed = False
        self.description = None

    def enter(self):
        print(self.description)


class Death(Scene):

    description = "Death is always right around the corner. \
    \nLooks like it finally caught up with you.\n\n[You died]"

    def enter():
        print(Death.description)
        return exit(0)


class Quit(Scene):

    description = "User quit.\nchicken..."
    def enter():
        print(Quit.description)
        return exit(0)


class CentralCorridor(Scene):

    description = ("This is the Central Corridor.",
    "You find yourself in an unfamiliar dark hallway, and your head hurts.",
    "You look around to get your bearings. You realize you are on an alien ship.",
    "Judging by the view out the window, it is headed for planet Percal #25, home of the Gothons.",
    "You need to get out of here, and quick. There's no escape once you reach the planet.",
    "These ships typically have escape pods, so you'll need to find one to get away.",
    "Additionally, you will need to clear the ship of Gothons so they don't chase you down.\n\n")

    def enter():
        for line in CentralCorridor.description:
            print(line)
        step1 = input("Do you head forward through the hall or back away into a corner?\n> ")
        if step1 == 'q' or step1 == 'quit':
            return 'quit'
        elif 'forward' in step1:
            print("As you proceed forward, you run into your first Gothon.")
            step2 = input("You can fight, run, or outdance it. Which do you choose?\n> ")
            if step2 == 'q' or step2 =='quit':
                return 'quit'
            elif 'outdance' in step2:
                print("That Gothon was no match for your moves.")
                print("You proceed to the Laser Weapons Armory.\n\n\n")
                return 'lwa'
            else:
                print("That was a bad idea.")
                print("This Gothon was all state in high school at track and boxing.")
                print("He destroys you, broh.\n\n")
                return 'death'
        else:
            print("You stall and stall. Eventually you land on Percal #25.")
            print("The Gothons disembark the ship and find you cowering in a corner.")
            print("They rip you to shreds.\n\n")
            return 'death'


class LaserWeaponArmory(Scene):

    description = "This is the Laser Weapon Armory.", \
    "To your surprise, there are more than laser weapons in here.",\
    "You find a pretty cool bomb that you think can take out the whole ship.",\
    "You hatch a plan to time it to detonate after some minutes, which should give you enough time to escape."

    def enter():
        for line in LaserWeaponArmory.description:
            print(line)
        print("\nThe bomb has a keypad lock on it.",\
        "Can you guess the one digit code keeping it locked?",\
        "(Gothons are not very good at weapons security.)")
        # why not make correct_code a string and get rid of try/except block?
        correct_code = random.randint(0,10)
        print("Hint: it might be [%d]" % correct_code)
        tries = 0
        while tries < 5:
            guess = input("Enter a number\n> ")
            if guess == 'q' or guess == 'quit':
                return 'quit'
            try:
                guess = int(guess)
            except ValueError:
                print("Nice going, funny guy. You broke the keypad.\n\n")
                return 'death'
            if guess != correct_code:
                print("\a\a\a\aBZZZZDT!")
                tries += 1
                print("Try again. %d more chances." % (5 - tries))
            else:
                print("Nice. You have 10 minutes on the clock.")
                print("Take that bomb to the Bridge and blow this ship to smithereens!\n\n\n")
                return 'bridge'
        print("Out of chances. The bomb has engaged with 5 seconds on the clock.")
        print("Realizing you can't outrun it, you stand there with a sad look on your face and await your fate.\n\n")
        return 'death'


class TheBridge(Scene):

    description = "This is The Bridge.",\
    "There are several Gothons guarding it, too many to outdance, even for you.",\
    "You try to sneak up on them, but they hear you and point their guns at you."

    def enter():
        for line in TheBridge.description:
            print(line)
        step1 = input("Do you give up or try to outsmart them?\n> ")
        if step1 == 'q' or step1 == 'quit':
            return 'quit'
        elif 'outsmart' in step1:
            print("'Smart' thinking! You point your gun at the bomb.", \
            "They know what that means and they slowly back away from you.", \
            "Two more come by, see what's going on, and sneak away as though they were never here.", \
            "You have set the bomb and now need to get out of here.\n\n\n")
            return 'ep'
        else:
            print("You sniveling worm. After all this work, you give up? Death ensues.\n\n")
            return 'death'


class EscapePod(Scene):

    description = "This is the Escape Pod Room. Pick one and go!"

    def enter():
        print(EscapePod.description)
        step1 = input("There are three pods here. Do you want pod 1, 2, or 3?\n> ")
        #removed code: correct_pod = random.randint(1,3)
        if step1 == 'q' or step1 == 'quit':
            return 'quit'
        elif step1 == '1' or step1 == '2' or step1 == '3':
            return 'youwin'
        else:
            print("You really should listen to me more...\n\n\n")
            return 'death'


class YouWin(Scene):

    description = "Nice work! You picked a good pod and you blast out into space.", "A few seconds go by and you feel a shockwave.", "The Gothon ship ignites like a sun.", "You sit back, relax, and catch some Z's as you head home.", "\n[end of game]"

    def enter():
        for line in YouWin.description:
            print(line)
        return exit(0)


class Map(object):

    scenes = {
    'cc': CentralCorridor,
    'ep': EscapePod,
    'bridge': TheBridge,
    'lwa': LaserWeaponArmory,
    'death': Death,
    'youwin': YouWin,
    'quit': Quit
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        Map.scenes[scene_name]

    def opening_scene(self):
        Map.scenes['cc']


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        print("-" * 50)
        print("GOTHONS FROM PLANET PERCAL #25")
        start = self.scene_map.scenes['cc']
        final = self.scene_map.scenes['youwin']

        while start != final:
            start = self.scene_map.scenes[start.enter()]

        self.scene_map.scenes[final.enter()]



start_map = Map('cc')
new_game = Engine(start_map)
new_game.play()
