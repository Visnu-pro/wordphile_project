import random
from words_list import word_list
import time

#VARIABLE INITIALIZATIONS
word=random.choice(word_list).upper()
gameboard=list()
w=str()
haswon=False
dash_index=0
letter=str()
counter=5

#RANDOMIZING THE GAME BOARD
for ch in word:
    if random.randint(0,101) in range(0,34):
        w=ch
    else:
        w="_"
    gameboard.append(w)

#PRINTING THE INRODUCTION SCREEN
print("Welcome to WORDPHILE\n")
time.sleep(0.5)
print("You have 5 lives in total. When you guess a word wrong, you will lose 1 life. When you lose all your lives, you die.\n")
time.sleep(0.5)
print("Let the game begin!\n")

time.sleep(0.1)
for i in range(0,5):
    print(".....finding a word")
    time.sleep(1)

print("\n")
print(gameboard)

#THE MAIN PROCESSING PART OF THE GAME
while not haswon:
    u=input("\nEnter your guess: ").upper()
    print("\n")
    if len(u)==1:
        for cha in word:
            if u == cha:
                w_index= word.index(cha)
                if gameboard[w_index]==cha:
                    print("Your guess is already in the word. You now have ",counter," lives left.\n ")
                elif gameboard[w_index]=='_':
                    gameboard[w_index]=cha

        if u not in word:
            counter-=1
            print("You have guessed wrong. You now have ",counter," lives left\n")
    if counter==0:
        print("You are already dead.\n")
        time.sleep(1)
        print("The word is:",word)
        time.sleep(1)
        print("\n")
        print("Thank you for playing our game.\nHave a nice day!")
        time.sleep(0.5)
        break
    print(gameboard)
    if '_' not in gameboard:
        time.sleep(1)
        print("\n")
        print("Congratulations, you have won.")
        time.sleep(0.5)
        print("Have a nice day!")
        time.sleep(0.75)
        haswon=True

    if u==word:
        print("Congratulations, you have guessed it correctly.")
        time.sleep(0.5)
        print("Have a nice day!")
        time.sleep(0.75)
        haswon=True
