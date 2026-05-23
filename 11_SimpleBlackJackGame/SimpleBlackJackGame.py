import random

print(r''' ___   _      __    __    _       _    __    __    _    
| |_) | |    / /\  / /`  | |_/   | |  / /\  / /`  | |_/ 
|_|_) |_|__ /_/--\ \_\_, |_| \ \_|_| /_/--\ \_\_, |_| \ ''')
print("\nWELCOME TO THE BLACKJACK GAME\n")
number=[11,2,3,4,5,6,7,8,9,10,10,10,10]
start=(input("Press \"Y\" to start the game any other key to exit : ")).upper()
if start=="Y":
    play=True
    user_list=[]
    comp_list=[]
    while play:
        user_list.extend(random.choices(number,k=2))
        comp_list.append(random.choice(number))
        print(f"Your cards : {user_list} , Current score : {sum(user_list)}")
        print(f"Computer's first card : {comp_list}\n")
        user_done=False
        while not user_done:
            choice=(input("Press \"Y\" to conitnue and \"N\" to pass : ")).upper()
            if choice=="Y":
                user_list.append(random.choice(number))
                print(f"Your cards : {user_list} , Current score : {sum(user_list)}")
                if sum(user_list)>=21:
                    user_done=True
                continue
            else:
                user_done=True
        while sum(comp_list)<=21:
                comp_list.append(random.choice(number))
                if sum(comp_list)>21:
                    del comp_list[-1]
                    break
        if sum(user_list)>21:
            print(f"\nYour final cards : {user_list} , Final score : {sum(user_list)}")
            print("YOU LOSE")
        else:
            print(f"\nYour final cards : {user_list} , Final score : {sum(user_list)}")
            print(f"Computer's final cards : {comp_list} , Final score : {sum(comp_list)}\n")
            if sum(user_list)>sum(comp_list):
                print("YOU WIN")
            elif sum(user_list)<sum(comp_list):
                print("YOU LOSE")
            else:
                print("DRAW")
        again=(input("\nTo play again press \"Y\" , any other key to exit : ")).upper()
        if again=="Y":
            user_list.clear()
            comp_list.clear()
        else:
            play=False