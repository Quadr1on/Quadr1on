# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is A Code to Convert Alphabets to Numbers
#                  By Adorn
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A   B   C   D   E   F   G   H   I   J   K   L   M
# 1   2   3   4   5   6   7   8   9   10  11  12  13

# N   O   P   Q   R   S   T   U   V   W   X   Y   Z
# 14  15  16  17  18  19  20  21  22  23  24  25  26

aln = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

sent = input("enter sentence: ").lower()
for i in sent:
    if i == " ":
        print(" ", end="")
    elif i in aln:
        print(aln[i], end=",")
    else:
        print(i, end=",")
