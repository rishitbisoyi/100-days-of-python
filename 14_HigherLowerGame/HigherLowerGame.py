import sys
import random
import GameData

# Game
def game():
    print()
    print('''             88        88 88   ,ad8888ba,  88        88 88888888888 88888888ba   
             88        88 88  d8"'    `"8b 88        88 88          88      "8b  
             88        88 88 d8'           88        88 88          88      ,8P  
             88aaaaaaaa88 88 88            88aaaaaaaa88 88aaaaa     88aaaaaa8P'  
             88""""""""88 88 88      88888 88""""""""88 88"""""     88""""88'    
             88        88 88 Y8,        88 88        88 88          88    `8b    
             88        88 88  Y8a.    .a88 88        88 88          88     `8b   
             88        88 88   `"Y88888P"  88        88 88888888888 88      `8b\n''')
    print('''             88          ,ad8888ba,  I8,        8        ,8I 88888888888 88888888ba   
             88         d8"'    `"8b `8b       d8b       d8' 88          88      "8b  
             88        d8'        `8b "8,     ,8"8,     ,8"  88          88      ,8P  
             88        88          88  Y8     8P Y8     8P   88aaaaa     88aaaaaa8P'  
             88        88          88  `8b   d8' `8b   d8'   88"""""     88""""88'    
             88        Y8,        ,8P   `8a a8'   `8a a8'    88          88    `8b    
             88         Y8a.    .a8P     `8a8'     `8a8'     88          88     `8b   
             88888888888 `"Y8888Y"'       `8'       `8'      88888888888 88      `8b\n''')
    v='''\n            8b           d8          
           `8b         d8'          
           `8b       d8'           
           `8b     d8' ,adPPYba,  
           `8b   d8'  I8[    ""  
           `8b d8'    `"Y8ba,   
           `888'    aa    ]8I  
            `8'     `"YbbdP"\'\n'''

    r=random.randint(0,50)
    a=GameData.celebrities[r]
    score=0
    while True:
        r=random.randint(0,50)
        b=GameData.celebrities[r]
        if a==b:
            r=random.randint(0,50)
            b=GameData.celebrities[r]
        print(f"Compare A : {a["name"]}, a {a["profession"]}, from {a["country"]}")
        print(v)
        print(f"Against B : {b["name"]}, a {b["profession"]}, from {b["country"]}")
        opt=(input("Who has more followers? Type \"A\" or \"B\" : ")).upper()
        if a["followers"]>b["followers"]:
            ans="A"
        else:
            ans="B"
            a=b
        if opt==ans:
            score+=1
            print(f"\nYou are right!! Current score : {score}\n")
            continue
        else:
            print(f"\nSorry that's wrong. Final score : {score}\n")
            break
    choice=(input("Press \"Y\" to play again. Any other key to exit : ")).upper()
    if choice=="Y":
        game()

# Starting of the game
print("WELCOME TO THE HIGHER LOWER GAME")
play=(input("Press \"Y\" to play. Any other key to exit : ")).upper()
if play=="Y":
    game()
sys.exit()
