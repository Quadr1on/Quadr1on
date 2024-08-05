# remove ''' from the begining and the end of the code

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""print("hello world")"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""name = "Adorn S George"
age = 16
actual_age = 16.69

print(age)
print(name)

print(type(name))
print(type(actual_age))"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
a = eval(input("enter a number: "))

if 20>a:
    print("heck ya that is absolutly right")
else:
    print("no burh that is worng are u a Kiddo!!" )
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
name = input("what is your name\n")
if name == "adithi" or name == "akshay" or name == "loki":
    evil = input("are you evil: ")
    if evil == "yes":
        good_deeds = int(input("how many good deeds have to done today: "))
        if good_deeds >= 4 :
                print("great u are welcome for today")
        else:  
                print("HEY!!! You are not welcome here EVIL "+ name + " get out!!!!!!") 
        
    else: 
        print("ohh so u are not evil! Come on in.")

else:
    print("welcome",name,"to the store")
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""print("welcome to here")
name = input("what is your name\n")

if name == "ben":
   print("get out of here")
else:
   print("come on in!")"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
a = "fuck my life"
alen = len(a)
print(alen)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""print("computerScience".split("er"))"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#calculator

while True:
    frist_number = eval(input("enter no: "))
    sign = input("enter the sign(+,-,/,*): ")
    second_number = eval(input("enter no: "))


    if sign == "+":
        print("Output:",frist_number + second_number)
    elif sign == "-":
        print("Output:",frist_number - second_number)
    elif sign == "/":
        print("Output:",frist_number / second_number)
    elif sign == "*":
        print("Output:",frist_number * second_number)
    else:
        print("enter valid input")

"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# basics of funtion

"""def noob_coder():
    print("dont waste your life coding, do something travel,eat,have fun.")

noob_coder()"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""def name(fname):
    print(str(fname).capitalize(),"george")

name("adorn")"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""name = input("enter your name:").capitalize()
age = int(input("Enter your age: "))
point = 0

if age <= 4:
    print("HEY,Bro u are just born u are not allowed.")
    exit()
elif age == 16:
    print("You are the same age a the writer of the code")
    print("but you are not allowed!")
    point += 1"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""months = {
    "Jan" : "January lol",
    "Feb" : "February odd one",
    "Mar" : "March My cruh Bday",
    "Apr" : "April U are Not special",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "Augest",
    "Sep" : "September",
    "Oct" : "october",
    "Nov" : "November",
    "Dec" : "December",
} 
Moth = input("enter Birth Month: ").capitalize()
print(months[Moth])"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""a = "tim|adkdsm"
x = a.split("|")
a1,a2 = x
print(a1)
print(a2)"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Shree = 'padipi'
if Shree == "padipi":
    print("True")
else:
    print("crow should fly upside down.")
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
A = [1,69,24,43,25,36,49,7,420,50]
for i in A:
    if i%5 == 0 or i%7 == 0:
        print(i)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
a,b = 12,13
c,b = a*2,a//2
print(a,b,c)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
x,y = 20,50
y,x,y = x,y-10,x+10
print(x,y)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FIFAWCbbCOM
"""text = "FifaWC@com"
L = len(text)
ntext = ""
for i in range(0,L):
    if text[i].isupper():
        ntext = ntext +text[i].lower()            
    elif text[i].isalpha():
        ntext = ntext +text[i].upper()      
    else:
        ntext = ntext+"bb"
print(ntext)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
sheep_count = 1
while sheep_count<100:
    print("%isheep%i",sheep_count)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
for i in range(0,10):
    print("adorn Is a noob")

"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
name = input("enter name:")
a = eval(input("enter age: "))
s = input("enter your gender: ") 

def info(name,age,sex):
    print("Name:",name)
    print("Age:",age)
    print("Gender:",sex)

info(name,a,s)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def execute(p,q = 30):
    temp = p+q
    q += temp
    print("",temp,"","",q)

a = 150
b = 100
execute(a)
print("",a,"","",b)
execute(a,b)
print("",a,"","",b)
# 180    210
# 150    100
# 250    350
# 150    100
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#calculator using function.

def add(a,b):
    c = a+b
    print(c)

def minus(a,b):
    c = a-b
    print(c)

def into(a,b):
    c = a*b
    print(c)

def div(a,b):
    c = a/b
    print(c)

def exp(a,b):
    c = a**b
    print(c)

while True:
    a = eval(input("enter number: "))
    x = input("enter +,-,/,*,**\n")
    
    if x == "**":
        b = eval(input("enter power:"))
    else:
        b = eval(input("enter number: "))

    if x == "+":
        add(a,b)

    elif x == "-":    
        minus(a,b)

    elif x == "*":
        into(a,b)
    
    elif x == "/":
        div(a,b)

    elif x == "**":
        exp(a,b)

    con = input("do you want to continue y/n: ")
    if con == "y":
        continue 
    else:
        break 

"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
with open("name.txt","w+") as f:
    a = input("enter name: ")
    s = f.write(a)
"""
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
import pickle

with open("car.dat","wb") as f:
     for i in range(3):
        l = input("enter car:")
        pickle.dump(l,f)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
try:
    f = open("car.dat","rb")

    color = input("enter color:")
    while True:
        l = pickle.load(f)
        if l[2]==color:
            print(l)

except:
    pass
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def spellwords():
    f = open("jk.txt","r")
    a = f.read()
    x = 0 
    while a:
        
        l = a.split()
        for i in l:
            if len(i)>4:
                print(i)

        break

spellwords()
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
try:
    while True:
        def fxn():
            print("Adorn")
            fxn()
        fxn()
except:
    pass 
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from itertools import combinations
a = [1,2,3,4]
cob = combinations(a,3 )
print(list(cob))
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
for i in range(100+1):
    
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i %3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)
 """
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import pickle
f = open("chand.dat","wb")
s ="good morning bitch!!!"
pickle.dump(s,f)
f.close()
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import pickle
f = open("chand.dat","rb")
while True:
    try:
        x = pickle.load(f)
        print(x)
    except:
        f.close()
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import os
f = open("jk.txt","r")
f1 = open("story.txt","w")
s = f.read()
for i in s:
    f1.write(i)

f.close()
f1.close()
os.remove("jk.txt")
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import csv
f = open ("jcheking.csv","w",newline="")
for rec in range(2):
    c = csv.writer(f)
    eno =input("enter emploee number:")
    ename = input("enter emploee name")
    sal =input("enter salary: ")
    l = [eno,ename,sal]
    x= [l]
    c.writerows(x)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
class item():
    def __init__(self ,name:str, price:int, quantity:int):
        
        assert price>=0, f"the price must me greater than 0"
        assert quantity>=0, f"the quantity must me greater than 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price*self.quantity

item1 = item("coffee",150,100)
item2 = item("masala",85,100)

print(item1.total_value())
print(item2.total_value())
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import matplotlib.pyplot as plt
import numpy as np



y = np.array([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16284])

plt.plot(y, marker ="o")
plt.show()
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
for i in range(20):
    c = 2**i
    l =[]
    l.append(c)
    
print(l)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def evenSum():
    l = eval(input("enter list: "))
    x = []
    for i in l:
        if i%2 == 0:
            x.append(i)   
        sum = i + i

    print("these are the Even Numbers:",x)
    print('sumis:',sum)




evenSum()
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def add():
    global d
    n = eval(input("enter how many students do u want to add: "))
    d={}
    for i in range(n):
        a = input("enter name:")
        per = eval(input("enter percentage: "))
        d[a]=per
    print(d)

def delete():
    rem = input("enter which name u want to remove:")
    del d[rem]
    print(d)

add()
delete()
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
f = open("lines.txt",'r')
f1 = open("newlines.txt",'w')
x = f.readlines()
for i in x:
    if 'a' in i:
        f1.write(i)
f.close()
f1.close()

f1 = open("newlines.txt",'r')
x = f1.read()
print(x)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import random
#Create a Greeting
print("Welcome to Hangman")
name = input("enter your name: ")
print("welcome",name+'\n You will be give a word at random from the word list\nthen you have to take a guess about the any one letter in the word')

points = 0
def randWord():
    global Randword
    words = ['hacking','word','address','fuck','cancer','business','capital']
    Rselector = random.randint(0,6)
    Randword = words[Rselector]

randWord()

l=[]
for i in Randword:
   l.append('_')
print(l) 

while True:
    U_input = input('You have to Guess A letter in the word: ').lower()
    if U_input in Randword:
        print('wow you got it, the letter is in the Word\nThe word is:',Randword)
        points += 1
        c = input("Do you want to continue?(Y/N): ")
        if c == 'y':
            randWord()
            continue
        else:
            print("Your points are:",points)
            break

    else:
        print('the letter is not in the word')
        continue
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
my_dict = {"name": "Aman", "age": 26}
my_dict['age'] = 27
my_dict['address'] = "Delhi"
print(my_dict.items())
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def prime():
    n=int(input("Enter number to check :: "))
    for i in range (2, n):
        if n%i==0:
            print("Number is not prime \n")
            break
        else:
            print("Number is prime \n")

prime()
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def rev(n):
    rev = 0
    rem = 0 
    while n >0 :
        rem = n %10
        rev = rev * 10 + rem
        n = n//10
    return rev

print(rev(1234))
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
tuple1 = (11, 22, 33, 44, 55 ,66)
list1 =list(tuple1)
new_list = []
for i in list1:
    if i%2==0:
        new_list.append(i)
        new_tuple = tuple(new_list)
    print(new_tuple)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
f = open("lines.txt",'r')
c = 0
s = f.readlines()
for i in range(len(s)):
    if s[i][0].lower() not in 'aeiou':
        c += 1
print(f'no of lines not starting with vowels are:{c}')
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
def display(str):
    m = ''
    for i in range(0,len(str)):
        if str[i].islower():
            m += str[i].upper()

        elif str[i].isupper():
            m+= str[i].lower()
        else:
            if i%2 == 0:
                m+= str[i-1]
            else:
                m+='#'
    print(m)

display('Fun@World2.0')

print(0%2)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~
# Binary Search Algorithm
# ~~~~~~~~~~~~~~~~~~~~~~~
"""

l = []
for i in range(1,100000000):
    l.append(i)
# print(l)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Target found, return the index
        elif mid_value < target:
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half

    return -1  # Target not found in the array

# Example usage:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 50000000

result = binary_search(l, target_value)

if result != -1:
    print(f'Target {target_value} found at index {result}')
else:
    print(f'Target {target_value} not found in the array')
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~
# Bubble Sort Algorithm
# ~~~~~~~~~~~~~~~~~~~~~~
"""
import random

l = []
for i in range(10000):
    x = random.randint(0,10000)
    l.append(x)

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
unsorted_array = [64, 34, 25, 12, 22, 11, 90,69,2,400,53,293]

# print("Unsorted array:", l)

# Applying bubble sort to the array
bubble_sort(l)

print("Sorted array:", l)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import random

# l = []
# for i in range(1000000):
#     x = random.randint(0,10000)
#     l.append(x)
# print(l)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursive call on the left half
        merge_sort(right_half)  # Recursive call on the right half

        # Merge the sorted halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in the left and right halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
unsorted_array = [64, 34, 25, 12, 22, 11, 90,500,700,794,65968,3948288,32,3984,23,2323,1111]

# print("Unsorted array:", l)

# Applying mergesort to the array
merge_sort(unsorted_array)

print("Sorted array:", unsorted_array)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
l = []
for i in range(1,100000000):
    l.append(i)
# print(l)

for i in range(len(l)):
    if l[i] == 3492:
        print(i)
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PreBoard-2 Practice
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
print(3 - 2**2**3 + 99 / 11)

pride = "#G20 Presidency"
print(pride[-2:0:-2])


PLACES = {1: "Delhi", 2: "London", 3: "Paris", 4: "New York", 5: "Doha"}


def countNow(PLACES):
    for i in PLACES.values():
        if len(i) > 5:
            print(i.upper())


# countNow(PLACES)


def lenWords(string):
    spl = stri.split()
    l = []
    for i in spl:
        l.append(len(i))

    print(tuple(l))


stri = "Come let us have some fun"
lenWords(stri)

travel = []
NList=[["New York", "U.S.A.", 11734],
["Naypyidaw", "Myanmar", 3219],
["Dubai", "UAE", 2194],
["London", "England", 6693],
["Gangtok", "India", 1580],
["Columbo", "Sri Lanka", 3405]]

def push_element(NList):
    for i in NList:
        l = []
        if i[2] < 3500:
            l.append(i[0])
            l.append(i[1])
            travel.append(l)
    # print(travel)
push_element(NList)

def display(NList):
    for i in range(len(NList)-1,-1,-1):
        print(NList[i])

# display(travel)

def pop(travel):
    while True:
        if len(travel) == 0:
            print('stack empty')
            break
        else:
            for i in range(len(travel)):
                print(travel.pop())
                print(len(travel))

pop(travel)

l = [
    ["Gurdas", "99999999999", "Goa"],
    ["Julee", "8888888888", "Mumbai"],
    ["Murugan", "77777777777", "Cochin"],
    ["Ashmit", "1010101010", "Goa"],
]

status = []
def push(List):
    for i in List:
        x = []
        if i[2] == 'Goa':
            x.append(i[0])
            x.append(i[1])
            status.append(x)
    print(status)
push(l)   

def pop(status):
    while True:
        if len(status) == 0:
            print('stack empty')
            break
        else:
            for i in range(len(status)):
                print(status.pop())

pop(status)

def index_list(l):
    x = []
    for i in range(len(l)):
        if l[i] != 0:
            x.append(i)
    print(x)

l = [21,0,32,34,332,0,23,30,20,00,0,0,23]
index_list(l)
output=> [0,2,3,4,6,7,8,12]

Ditem={"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25}
stack = []
def push(item):
    c = 0
    for k,v in item.items():
        if v >75:
            stack.append(k)
            c +=1

    print(stack)
    print(f'the count of element in the stack is {c}')

push(Ditem)

print(True or not True and False)
print(3%5)

x = eval(input('enter password:'))
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
#inverse of a matix
import numpy as np

def inverse_matrix(matrix):
    try:
        # Use np.linalg.inv to calculate the inverse of the matrix
        inverse = np.linalg.inv(matrix)
        return inverse
    except np.linalg.LinAlgError:
        # If the matrix is singular or not invertible, handle the exception
        print("The matrix is singular and cannot be inverted.")

# Example matrix
matrix = np.array([[2,3,1],[-3,2,1],[5,-4,-2]])

# Call the function to get the inverse
inverse_result = inverse_matrix(matrix)

# Print the result
print("Original matrix:")
print(matrix)
print("Inverse matrix:")
print(inverse_result)
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def EvenSum(NUMBERS):
    su = 0
    for i in NUMBERS:
        if i%2 == 0:
            su = su + i 

    print(su)       
    
li = [1,2,3,4,5,6,7,89,9,8,0,54,33,69]
EvenSum(li)