# Name: Balitog, Keturah Faye W.
# Section: Camia





def display_intro():

    print("===============================")
    print("    THREE-DOOR TREASURE HUNT"   )
    print("===============================")
    name = input("Enter your name: ")
    print(f"Player: {name}     Starting Points: 20")
    print(f"Welcome to the castle, {name}!")
    print("Choose your door: [1] Wooden  [2] Red  [3] Golden")

def show_door(name, player):

    choice = int(input(": "))


def explore_doors(choice, player, name):
    score = 20


    if choice == 1:
        print("You discovered a treasure chest!")
        print ("You earned 50 points!")
        score += 50


    elif choice == 2:
        print("You discovered the magical key!")
        print ("You earned 30 points!")
        score += 30

    elif choice == 3:
        print("Oh no! You awakened a dragon!")
        print ("You lost 20 points!")
        score -= 20

        print(f"Total Score: {score}")

def display_result(player, score, name, choice ):
    print("-------- GAME RESULTS --------")


    if score >= 70:
        player = "TREASURE MASTER"

    elif score >= 40:
        player = "BRAVE EXPLORER"
    elif score < 40:
        player = "BEGINNER ADVENTURER"


display_intro()






