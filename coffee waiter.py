# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# my programe creating a coffee shop waiter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import time

# welcoming and what is there name
print("welcome to the Starbucks")
name = input("what is ur name\n").capitalize()

# kicking out ben
if name == "Adithi" or name == "Jazz" or name == "Loki":
    evil = input("are you evil: ")
    if evil == "yes":
        good_deeds = eval(input("How many good deeds have u done today?\n"))
        if good_deeds >= 4:
            print("great u are welcome for today")
        else:
            print("You are not welcome here EVIL " + name + " get out!!!!!!")
            exit()
else:
    print("HEY!! " + name + " Welcome to the Starbucks")
# order taking and welcome

order = input(
    "what would you like to have:\n1.tea\n2.coffee\n3.latte\n4.espresso\n5.cold coffee\n=>"
).lower()

# price of the order
if order == "tea":
    price = 3
elif order == "coffee":
    price = 4
elif order == "latte":
    price = 6
elif order == "espresso":
    price = 8
elif order == "cold coffee":
    price = 10
else:
    print("sorry we dont have that here")


# how much wanted for the user
quantity = input("how much would u like to have?\n")
total = price * int(quantity)
print("ok ur order will be: $" + str(total))

print("ok " + name + " your " + quantity + " " + order + " will be ready soon")
time.sleep(60)

pay = input(f"your {order} is ready! how would you like to pay:")
if pay == "cash":
    print(f"here is your {order} thanks for buying from us\nVisit again.")
elif pay == "upi":
    print(f"here is your {order} thanks for buying from us\nVisit again.")

elif pay == "Adithi loves Adorn":
    print(
        f"your order is on the house!!\nhere is your {order} thanks for buying from us\nVisit again."
    )
