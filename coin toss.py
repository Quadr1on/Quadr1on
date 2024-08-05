import random
 
name = input("Enter your name: ")
user = 0
comp = 0
options = ["heads","tails"]

while True:

    us_input = input("Pick Heads or Tails, or Q to quit: ").lower()
    if us_input == "q":
        break
    
    if us_input not in options:
        print("choose a vaild input")
        continue

    comp_pick = 0
    if us_input == "heads":
        comp_pick = "tails"

    else:
        comp_pick = "heads"

    random_number = random.randint(0,1)
    toss = options[random_number]

    if toss == "heads" and us_input == "heads":
        print("it is",toss)
        print(name,"won the toss, 1 point added to you")
        print("computer lost")
        user += 1

    elif toss == "heads" and us_input == "tails":
        print("it is",toss)
        print("Computer won the toss, 1 point added to you")
        print(name,"Lost")
        comp +=1
    elif toss == "tails" and us_input == "tails":
        print("it is",toss)
        print(name,"won the toss, 1 point added to you")
        print("computer lost")
        user +=1
    elif toss == "tails" and us_input == "heads":
        print("it is",toss)
        print("Computer won the toss, 1 point added to you")
        print(name,"Lost")
        comp +=1

print("you have",user,"wins")
print("computer have",comp,"wins")

if user>comp:
    print("You have more point So you won.")
elif user == comp:
    print("Its a Draw!")
else:
    print ("Ahh! unfortunatly computer have more points than you so computer won")

print("GoodBye!")