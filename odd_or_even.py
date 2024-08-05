import random

user_score = 0
computer_score = 0
options = [1,2,3,4,5,6,7,8,9,10]
odd_or_even = ["odd","even","q"]

#Code for players choice 
while True:
    user_pick = input("pick odd or even or Q to Quit: ").lower()
    
    if user_pick == odd_or_even[2]:
        break
    
    if user_pick not in odd_or_even:
        print("choose a valid option")
        continue
    
    #making computers choice
    user_input = int(input("pick 1 to 10: "))
    random_number = random.randint(0,9)
    computer_pick = options[random_number]

    if user_input not in options:
        print("choose a valid option")
        continue

    print("computer pick\'s: ",computer_pick)
    
    #to check weather even or odd
    remainder = int(computer_pick + user_input) % 2 
    print("total is: ",int(computer_pick + user_input))
    if remainder == 0:
        check = "even" 
    else:
        check = "odd"

    print(check) 

    #Code for creating the scoring system
    if user_pick != check:
        print("You lost")
        computer_score += 1 

    else:
        print("you won")
        user_score += 1

#To check weather computer won or the player won
print("you have",user_score,"wins")
print("computer have",computer_score,"wins")

if user_score>computer_score:
    print("You have more point So you won.")
elif user_score == computer_score:
    print("Its a Draw!")
else:
    print ("Ahh! unfortunatly computer have more points than you so computer won")

# print("GoodBye!")


     
       
    
    