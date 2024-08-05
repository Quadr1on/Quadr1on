import random

user_score = 0
computer_score = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("type Rock/Paper/Scissors or Q for quit: ").lower()
    if user_input == "q":
        break
        
    if user_input not in options:
        print("choose a VAILD option.")
        continue

    random_number = random.randint(0,2)
    #rock = 0,paper = 1,scissor = 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("waoh!You won")
        user_score += 1
      
    elif user_input == "paper" and computer_pick == "rock":
        print("waoh!You won")
        user_score += 1
      
    elif user_input == "scissors" and computer_pick == "paper":
        print("waoh!You won")
        user_score += 1
        
    elif user_input == "scissors" and computer_pick == "scissors":
        print("No one won!")
    elif user_input == "rock" and computer_pick == "rock":
        print("No one won!")
    elif user_input == "paper"and computer_pick == "paper":
        print("No one won!")    
    else:
        print("ahh!Unfortunaly you lost")        
        computer_score += 1

    
print("You won", user_score,"times.")
print("computer won",computer_score,"times.")
print("Goodbye!")