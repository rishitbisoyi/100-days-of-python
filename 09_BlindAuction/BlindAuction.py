import os

#  Start
print('''+-+-+-+-+-+ +-+-+-+-+-+-+-+
|B|L|I|N|D| |A|U|C|T|I|O|N|
+-+-+-+-+-+ +-+-+-+-+-+-+-+''')
print("\nWELCOME TO THE BLIND AUCTION")
print("\nENTER THE NAME OF THE BIDDER AND THE AMOUNT")

#  Auction input process
bidding=True
auction={}
while bidding:
    name_bidder=input(("Enter the name of the bidder : "))
    value_bidder=int(input("Enter the bidding amount : ₹"))
    auction[name_bidder]=value_bidder
    choice=input("Enter \"Y\" to enter another bidder \"N\" to exit the entries and print the result of the auction : ")
    if choice.upper()=="Y":
        os.system("cls")
    else:
        bidding=False

#  Auction result
max_name=max(auction,key=auction.get)
print(f"{max_name.upper()} wins the auction by bidding the most which is ₹{auction[max_name]}")