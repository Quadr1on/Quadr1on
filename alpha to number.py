# This is A Code to Convert Alphabets to Numbers
#                  By Adorn
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A   B   C   D   E   F   G   H   I   J   K   L   M
# 1   2   3   4   5   6   7   8   9   10  11  12  13

# N   O   P   Q   R   S   T   U   V   W   X   Y   Z
# 14  15  16  17  18  19  20  21  22  23  24  25  26

sent = input("enter sentence: ").lower()

# this is where alpbhets convert to numeric
for i in sent:
    if i == " ":
        print(end=" ")
    elif i == "a":
        print(1, end=",")
    elif i == "b":
        print(2, end=",")
    elif i == "c":
        print(3, end=",")
    elif i == "d":
        print(4, end=",")
    elif i == "e":
        print(5, end=",")
    elif i == "f":
        print(6, end=",")
    elif i == "g":
        print(7, end=",")
    elif i == "h":
        print(8, end=",")
    elif i == "i":
        print(9, end=",")
    elif i == "j":
        print(10, end=",")
    elif i == "k":
        print(11, end=",")
    elif i == "l":
        print(12, end=",")
    elif i == "m":
        print(13, end=",")
    elif i == "n":
        print(14, end=",")
    elif i == "o":
        print(15, end=",")
    elif i == "p":
        print(16, end=",")
    elif i == "q":
        print(17, end=",")
    elif i == "r":
        print(18, end=",")
    elif i == "s":
        print(19, end=",")
    elif i == "t":
        print(20, end=",")
    elif i == "u":
        print(21, end=",")
    elif i == "v":
        print(22, end=",")
    elif i == "w":
        print(23, end=",")
    elif i == "x":
        print(24, end=",")
    elif i == "y":
        print(25, end=",")
    elif i == "z":
        print(26, end=",")
