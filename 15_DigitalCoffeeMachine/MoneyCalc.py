# Billing and money management
import DigitalCoffeeMachine

def Billing(bill):
    def Calc():
        print("\nEnter the notes (10/20/50/100/200/500)");
        money1=(int(input("Enter no. of tens = ")))*10
        money1+=(int(input("Enter no. of twenties = ")))*20
        money1+=(int(input("Enter no. of fifties = ")))*50
        money1+=(int(input("Enter no. of hundreds = ")))*100
        money1+=(int(input("Enter no. of two hundreds = ")))*200 
        money1+=(int(input("Enter no. of five hundreds = ")))*500
        return money1

    money=Calc()
    while money<bill:
        print(f"\nPlease enter more ₹{bill-money}.")
        money+=Calc()
    DigitalCoffeeMachine.tmoney+=money
    if money>=bill:
        print(f"\nYour change is ₹{money-bill}.")
    DigitalCoffeeMachine.tmoney-=(money-bill)