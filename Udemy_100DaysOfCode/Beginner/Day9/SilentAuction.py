import os
choice = "yes"
auction = {}
while(choice == "yes"):
    os.system('cls')
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: Rs."))
    choice = input("Are there more bidders? yes, no -> ").lower()
    auction[bid]=name
print(f"The winner of the silent auction is {auction[max(auction.keys())]} with a bid of Rs.{max(auction.keys())}")