print("Aryan's VIRTUAL BANK SYSTEM")
print()
print("Enter Numbers Only To Prevent Errors!!!")
print()
password_make = input("Make a new password for you: ")

wallet = 10000
deposit = 0
OnHand = 1000
history = []

print(f"In Bank your wallet: {wallet}")
print(f"Deposited in Bank: {deposit}")
print(f"Money in your hand: {OnHand}")
print()

while True:
    # Everything inside the loop is wrapped in a try block
    try:
        print("Chose an option: Deposit , Loan , withdraw , history")
        Enter = input("Enter your option: ")
        print()
        password = input("Enter your password: ")
        print()
    
        if password == password_make:
            if Enter.lower() == "deposit":
                print()
                depo = int(input("Enter value to deposit: "))
                if depo > OnHand:
                    print("You can only Add money in your hand not more than that")
                    print()
                elif depo < 0:
                    print("Invalid Amount")
                    print()
                elif depo <= OnHand:
                    print("Added to your bank wallet successfully")
                    OnHand = OnHand - depo
                    wallet = wallet + depo
                    print(f"In your hand amount is {OnHand} and in bank amount is {wallet}")
                    print()
                    history.append(f"Deposited Amount:${depo}")
                else:
                    print("Invalid option")
                    
            elif Enter.lower() == "loan":
                loan = int(input("Enter amount of loan: "))
                print()
              
                if loan <= 0:
                     print("Invalid amount")
                     print()
                elif loan > 0:
                     print("Loan Taken successfully")
                     OnHand = OnHand + loan
                     print(f"Amount in your hand ${OnHand}")
                     print()
                     history.append(f"Loan Taken:${loan}")
                else:
                    print("Invalid Amount") 
                    print()
                 
            
            elif Enter.lower() == "withdraw":
                withdraw = int(input("Enter amount to withdraw: "))
                if withdraw > wallet:
                    print("Insufficient amount to withdraw")
                    print()
                elif withdraw <= wallet and withdraw > 0:
                    OnHand = OnHand + withdraw
                    wallet = wallet - withdraw
                    print(f"Withdrawl succesful money OnHand is ${OnHand}")
                    print()
                    history.append(f"Amount Withdrawed:${withdraw}")
                elif withdraw <= 0:
                    print("Invalid Amount")
                    print()
            elif Enter.lower() == "history":
                print(history)
                break
                    
        else:
            print("Nice Try! But Incorrect Password")
            print()

    # If an error happens, it triggers this, stays inside the while loop, and restarts!
    except ValueError:
        print("Nice Try! But only numbers allowed")
        print()
        