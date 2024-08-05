#print("hello World")
#a = input("enter name:").capitalize()
import random
c = 0
c1 = 0
for i in range(100):
    l = ["adorn","adithi","akshay","manas","jaswant","shreeshanker"]
    rand = random.randint(0,5)
    a = l[rand]
    if a.lower() == "adorn":
        print(a,"is the best.")
        c+=1
    elif a == "adithi":
        print("lub u",a)
        c1+=1
    else:
        print(a,"sucks.")

print("no of adithi",c1)
print("no of adorn",c)