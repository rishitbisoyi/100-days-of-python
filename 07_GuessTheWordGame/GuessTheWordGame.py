import sys
import random

# 7 letter word
def letters_7():
    seven_letter_words=["abalone", "balloon", "cabinet", "dolphin", "eclipse", "florist", "giraffe","harmony", "jasmine", "kaleido", "lobster", "mystery", "nuclear", "octopus","penguin", "quartet", "rainbow", "sapphire", "tornado", "umbrella", "volcano","whisper", "zeppelin", "bicycle", "champion"]
    word=(random.choice(seven_letter_words)).upper()
    word_to_print="_______"
    lives=5
    while lives>0:
        guessed_letter=(input(f"Word to guess : {word_to_print}\nGuess a letter : ")).upper()
        if guessed_letter in word:
            for i in range(len(word)):
                if word[i]==guessed_letter:
                    word_to_print=word_to_print[:i]+guessed_letter+word_to_print[i+1:]
            if word_to_print==word:
                print(f"You have guessed {word} correctly")
                return
        else:
            lives-=1
        print(f"{lives}/5 lives left")

# 8 letter word
def letters_8():
    eight_letter_words=["absolute", "bachelor", "calendar", "dinosaur", "elephant", "firework","gymnasium", "hospital", "illusion", "jellyfish", "kangaroo", "lighthouse","mountain", "notebook", "overcoat", "paradigm", "question", "reindeer","sunshine", "triangle", "universe", "velocity", "wildlife", "yearbook","zucchini", "aeroplane"]
    word=(random.choice(eight_letter_words)).upper()
    word_to_print="________"
    lives=6
    while lives>0:
        guessed_letter=(input(f"Word to guess : {word_to_print}\nGuess a letter : ")).upper()
        if guessed_letter in word:
            for i in range(len(word)):
                if word[i]==guessed_letter:
                    word_to_print=word_to_print[:i]+guessed_letter+word_to_print[i+1:]
            if word_to_print==word:
                print(f"You have guessed {word} correctly")
                return
        print(f"{lives}/6 lives left")

# 9 letter word
def letters_9():
    nine_letter_words=["adventure", "beautiful", "chocolate", "dangerous", "education", "framework","guerrilla", "happiness", "important", "jellybean", "knowledge", "landscape","mushroom", "nightmare", "obsession", "pumpkin", "quicksand", "rectangle","snowboard", "telephone", "umbrella", "vibrato", "wonderful", "xylograph","yellowish", "zoologist"]
    word=(random.choice(nine_letter_words)).upper()
    word_to_print="_________"
    lives=7
    while lives>0:
        guessed_letter=(input(f"Word to guess : {word_to_print}\nGuess a letter : ")).upper()
        if guessed_letter in word:
            for i in range(len(word)):
                if word[i]==guessed_letter:
                    word_to_print=word_to_print[:i]+guessed_letter+word_to_print[i+1:]
            if word_to_print==word:
                print(f"You have guessed {word} correctly")
                return
        else:
            lives-=1
        print(f"{lives}/7 lives left")

# Game
def game():
    number_of_letters=int(input("Enter the number of letter you want to play the game with (choose from 7 , 8 or 9 only) : "))
    if number_of_letters==7:
        letters_7()
    elif number_of_letters==8:
        letters_8()
    elif number_of_letters==9:
        letters_9()
    else:
        print("Invalid number of letters entered")
        return

# Start of game 
while True:
    print("WELCOME TO THE WORD GUESSING GAME")
    rules=(input(("To know the rules press \"R\" any other key to continue : "))).upper()
    if rules=="R":
        print("1.You have to select the number of letter in a word,available options are 7,8 and 9 letter words")
        print("2.Guess the letters one by one and if you guess one letter wrong you lose one life")
        print("3.Guess the word correctly before your lives run out to win the game")
    print("Hope you enjoy the game !!!")
    start=(input("Press \"Y\" to start the game any other key to exit : ")).upper()
    if start=="Y":
        game()
        start=(input("Press \"Y\" to play again any other key to exit : ")).upper()
        if start=="Y":
            continue
        sys.exit()
    sys.exit()