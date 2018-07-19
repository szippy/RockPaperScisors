#7/16/18
#play rock paper scisors against the AI or a person

import sys
import random
import getpass
#Rock Paper Scisors
def takeInput():
    string = ''
    out = 0
    flag = True
    while flag:
    #rock = 1, paper = 2, scisors = 3
        string = getpass.getpass("\nEnter 'rock', 'paper' or 'scisors'\n")
        string = string.lower()
        if string == "rock":
            out = 1
            flag = False
        elif string == "paper":
            out = 2
            flag = False
        elif string == "scisors":
            out = 3
            flag = False
        else:
            print("\nPlease enter 'rock', 'paper' or 'scisors'\n")

    return out

def hasWon(player1, player2):
    #rock = 1, paper = 2, scisors = 3
    if player1 == 1 and player2 == 3:
        return True
    elif player1 == 2 and player2 == 1:
        return True
    elif player1 == 3 and player2 == 2:
        return True

    return False

def onePlayer():
    print("\nOne Player\n")
    flag = True
    while flag:
        player2 = 0
        player1 = 0
        player2 = random.randint(1,4)

        player1 = takeInput()
        if not (player1 == player2):
            flag = False
        else:
            print ("\nIt's a tie! Try again!\n")

    if hasWon(player1, player2):
        print("\nYou have Won!\n")
    elif not(hasWon(player1, player2)):
        print("\nI Won!\n")

def twoPlayer():
    print("\nTwo Player\n")
    player1 = 0
    player2 = 0

    print("\nPlayer 1 \n")
    player1 = takeInput()
    print("\nPlayer 2 \n")
    player2 = takeInput()


    if hasWon(player1, player2):
        print("\nPlayer 1 has Won!\n")
    elif not(hasWon(player1, player2)):
        print("\nPlayer 2 has Won!\n")


flag = True
while flag:
    print("Welcome to Rock Paper Scisors\n")

    print("type 'Exit' to exit the program\n")
    print("Type '1' to play one player, or '2' to play 2 player\n")
    string = input("Please enter your choice\n")
    string = string.lower()

    if string == 'exit':
        print("\n Thank you for playing Rock Paper Scisors\n")
        sys.exit()
    elif string == '1':
        onePlayer()
    elif string == '2':
        twoPlayer()
