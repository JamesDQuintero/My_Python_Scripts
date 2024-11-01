print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You're at the cross road. Where do you want to go?")

import sys

while True:
    direction = input("Type \"left\" or \"right\". ").lower()

    if direction == "right":
        print("Fell into a hole. Game over. ")
        sys.exit(0)
        break

    elif direction == "left":
        print(
            "You've come to a lake. There is an island in the middle of the lake."
        )
        break

    else:
        print("Invalid input. Please try again.")

while True:
    action = input(
        "Type \"wait\" to wait for a boat. Type \"swim\" to swim across. "
    ).lower()

    if action == "swim":
        print("Got eaten by shark. Game over. ")
        sys.exit(0)
        break

    elif action == "wait":
        print("You see three doors.")
        break

    else:
        print("Invalid input. Please try again.")

while True:
    door = input("which door? Type \"red\", \"yellow\", or \"blue\". ").lower()

    if door == "red":
        print("Burned by fire. Game over. ")
        break
        sys.exit(0)

    elif door == "yellow":
        print(
            "CONGRATULATIONS! YOU MADE IT ALIVE! YOU FOUND THE TREASURE! YOU WIN!"
        )
        break

    elif door == "blue":
        print("Eaten by beasts. Game Over.")
        break
        sys.exit(0)

    else:
        print("Invalid input. Please try again.")
