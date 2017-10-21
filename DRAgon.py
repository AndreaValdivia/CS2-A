import time
import random

# keyword 'def' tell python this is a function
# after 'def' is the name of the function
# to call this function we type the name followed by parenthesis ().
def display_intro():
    print('''You are in a land full of dragons. In front of you, you see four caves.
In one cave, the dragon is friendly and will share his treasure with you.
The other dragon is greedy and hungry, and will eat you on sight. The third dragon is
a cat dressed in a dragon costume, you can take him home. The final dragon is a magic dragon
will perform a show.''') # Multi-line string
    print()

# and - operator takes two boolean values.
# True and True -> True
# False and True -> False
# False and False -> False
# True and False -> False

# or - operator takes two boolean values.
# True and True -> True
# False and True -> True
# False and False -> False
# True and False -> True

# cave = 3, cave != 1 -> True
# cave = 3, cave != 2 -> True ---> True and True -> True, KEEP GOING
# cave = 2, cave != 1 -> True
# cave = 2, cave != 2 -> False ---> True and False -> False, STOP LOOP
def choose_cave():
    cave = ""
    while cave != "1" and cave != "2" and cave != "3" and cave != "4":
        print("Which cave will you enter? (1, 2, 3, or 4) ")
        cave = input()
    return cave # functions output

def check_cave(cave_chosen):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)
  if cave_chosen
