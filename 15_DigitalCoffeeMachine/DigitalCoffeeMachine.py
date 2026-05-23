import sys
import MoneyCalc

# Report 
water=800
milk=800
coffee=200
tmoney=2000

# Main interface
while True:
    print("\nMENU :-\nESPRESSO - ₹250\nLATTE - ₹300\nCAPPUCCINO - ₹270\n")
    order=(input("\nWhat would you like (espresso/latte/cappuccino) : ")).upper()
    if order=="OFF":
        sys.exit()
    elif order=="REPORT":
        print(f"\nCoffee powder = {coffee} g\nWater = {water} ml\nMilk = {milk} ml\nMoney = ₹{tmoney}")
    elif order=="ESPRESSO":
        if water>=50 and coffee>=18:
            bill=250
            print(f"\nYour total bill is ₹{bill}")
            MoneyCalc.Billing(bill)
            water-=50
            coffee-=18
            print("Here is your espresso. Enjoy!")
        else:
            if water<50:
                print("\nSorry there is not enough water.")
            if coffee<18:
                print("\nSorry there is not enough coffee powder.")
    elif order=="LATTE":
        if water>=200 and coffee>=24 and milk>=150:
            bill=300
            print(f"\nYour total bill is ₹{bill}")
            MoneyCalc.Billing(bill)
            water-=200
            coffee-=24
            milk-=150
            print("Here is your latte. Enjoy!")
        else:
            if water<200:
                print("\nSorry there is not enough water.")
            if coffee<24:
                print("\nSorry there is not enough coffee powder.")
            if milk<150:
                print("\nSorry there is not enough milk.")
    elif order=="CAPPUCCINO":
        if water>=250 and coffee>=24 and milk>=100:
            bill=270
            print(f"\nYour total bill is ₹{bill}")
            MoneyCalc.Billing(bill)
            water-=250
            coffee-=24
            milk-=100
            print("Here is your cappuccino. Enjoy!")
        else:
            if water<250:
                print("\nSorry there is not enough water.")
            if coffee<24:
                print("\nSorry there is not enough coffee powder.")
            if milk<100:
                print("Sorry there is not enough milk.")