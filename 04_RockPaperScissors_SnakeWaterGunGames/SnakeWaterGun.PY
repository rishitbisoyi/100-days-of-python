import sys
import random

# RULES FUNCTION
def rules ():
    print("Rules of the game are as follows : ")
    print("SNAKE 🐍 beats WATER 🌊")
    print("WATER 🌊 beats GUN 🔫")
    print("GUN 🔫 beats SNAKE 🐍")
    print(" \n ")

# GAME FUNCTION
def game (matches,rounds):
  comp=["S🐍","W🌊","G🔫"]
  umw=0
  cmw=0
  for i in range (1,matches+1):
   urw=0
   crw=0
   print(f"STARTING MATCH {i}")
   print(" \n")
   rp=0
   while rp<rounds:
    user=(input("Press \"S\" for SNAKE(🐍)\nPress \"W\" for WATER(🌊)\nPress \"G\" for GUN(🔫) : ")).upper()
    if user not in ("S","W","G"):
        print("YOU HAVE ENTERED A WRONG CHOICE")
        continue
    if (user=="S"):
      user="S🐍"
    elif (user=="W"):
      user="W🌊"
    else:
      user="G🔫"
    cc=random.choice(comp)
    print(" \n")
    print(f"😎 YOU CHOSE : {user} and 🤖 BOT CHOSE : {cc}")
    if (cc==user):
        print("🤝 TIE 🤝")
        continue
    elif ((cc=="S🐍" and user=="W🌊") or (cc=="G🔫" and user=="S🐍") or (cc=="W🌊" and user=="G🔫")):
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
 print("||......WELCOME TO THE SNAKE🐍 ,WATER🌊 AND GUN🔫 GAME......||")
 print(" \n")
 rul=(input("If you want to know the rules press \"i\" (any other key to skip) : ")).upper()

 if (rul=="I"):
    rules()

 s=(input("Press \"Y\" to start the game (any other key to exit). ENJOY !! : ")).upper()
 if (s=="Y"):
    m=int(input("Enter number of matches to be played : "))
    print(" \n")
    r=int(input("Enter number of rounds per match : "))
    game(m,r)
 else:
   sys.exit()