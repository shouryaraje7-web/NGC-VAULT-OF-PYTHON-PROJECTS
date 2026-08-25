import random
print("NextGenCoder's simple Rock Paper Scissors game")
print()
print("User should type Rock or Scissors or Paper in capital only")
print()

run = True
while run == True:
    
    Game = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(Game)


    choice = input("User's Choice: ")
    if choice == "Rock" or choice == "Paper" or choice == "Scissors":
        print(f"Computer's choice: {computer_choice}")
        print()
    
    else:
        print("Error: Incorrect Choice" ) 
        print()
        
        