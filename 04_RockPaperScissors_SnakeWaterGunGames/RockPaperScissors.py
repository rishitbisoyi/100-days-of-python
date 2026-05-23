import sys
import random

# RULES FUNCTION
def rules ():
    print("Rules of the game are as follows : ")
    print("ROCK 🪨 SCISSORS ✂️")
    print("PAPER 📄 beats ROCK 🪨")
    print("SCISSORS ✂️ beats PAPER 📄")
    print(" \n ")

# GAME FUNCTION
def game (matches,rounds):
  comp=["R🪨","P📄","S✂️ "]
  umw=0
  cmw=0
  for i in range (1,matches+1):
   urw=0
   crw=0
   print()
   print(f"STARTING MATCH {i}")
   print()
   rp=0
   while rp<rounds:
    user=(input("Press \"R\" for Rock(🪨  )\nPress \"P\" for Paper(📄)\nPress \"S\" for Scissors(✂️ ) : ")).upper()
    if user not in ("R","P","S"):
        print("YOU HAVE ENTERED A WRONG CHOICE")
        continue
    if (user=="R"):
      user="R🪨"
    elif (user=="P"):
      user="P📄"
    else:
      user="S✂️ "
    cc=random.choice(comp)
    print(" \n")
    print(f"😎 YOU CHOSE : {user} and 🤖 BOT CHOSE : {cc}")
    if (cc==user):
        print("🤝 TIE 🤝")
        continue
    elif ((cc=="R🪨" and user=="S✂️ ") or (cc=="S✂️ " and user=="P📄") or (cc=="P📄" and user=="R🪨")):
        print("🤖 BOT WINS")
        crw+=1
        rp+=1
    else:
        print("😎 YOU WIN")
        urw+=1
        rp+=1
   print(" \n ")
   print("|....MATCH RESULTS....|")
   if (urw==crw):
    print("🤝 MATCH TIED 🤝")
   elif (urw>crw):
    print(f"🥳 YOU WIN THE MATCH {urw} : {crw}")   
    umw+=1 
   else:
    print(f"🤖 BOT WINS MATCH {crw} : {urw}")
    cmw+=1
   print("NUMBER OF MATCHES LEFT",(matches-i))
  print(" \n ")
  print("|.....SERIES RESULTS.....|")
  if umw==cmw:
    print(f"🤝 SERIES TIED WITH SCORE {umw} : {cmw} 🤝")
  elif umw>cmw:
    print(f"🥳 USER WINS THE SERIES WITH SCORE {umw} : {cmw} 🏆 CONGRATULATIONS !!!")
  else:
    print(f"🤖 BOT WINS THE SERIES WITH SCORE {cmw} : {umw} 🏆 BETTER LUCK NEXT TIME !!!")
  print(" \n ")

# START OF GAME
while True:
 print()
 print("||......WELCOME TO THE ROCK🪨 ,PAPER📄 AND SCISSORS✂️  GAME......||")
 print()
 rul=(input("If you want to know the rules press \"i\" (any other key to skip) : ")).upper()

 if (rul=="I"):
    rules()

 s=(input("Press \"Y\" to start the game (any other key to exit). ENJOY !! : ")).upper()
 if (s=="Y"):
    print()
    m=int(input("Enter number of matches to be played : "))
    print()
    r=int(input("Enter number of rounds per match : "))
    game(m,r)
 else:
   sys.exit()