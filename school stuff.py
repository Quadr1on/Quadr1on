#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''a = eval(input("enter no: "))

if a%10 == 5:
   print("the number ends with 5")
else:
   print("it doesn't end with 5")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''while True:
    a = eval(input("enter no: "))

    if a<0:
        a = a*-1
    
    print(a)'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''h = eval(input("enter height: "))
w = eval(input("enter weight: "))
bmi = w/h**2*10000
print(bmi)
if bmi<18.9:
    print("you are underweight")
elif bmi >= 18.9 and bmi<= 24.9:
    print("you are normal")
elif bmi >= 25 and bmi<= 29.9:
    print("you are overweight")
else:
    print("you are obese")'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''s = "good morning india"

print(s[2:15:2])'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''s = input("enter sentence: ")
a = d = l = 0
for i in s:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        d+=1
    else:
        l+=1

print("no of alphabet: ",a)
print("no of digit: ",d)
print("no of special characters: ",l)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''string = input("enter sentence: ").lower()
vowel = "aeiou"
a = 0 
for i in string:
    if i in vowel:
        a+=1

print(a)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''c = 0
a = eval(input("enter list: "))

for i in a:
    if i % 10 == 5:
        c+=1

print("Number of digits ending with 5 is:",c)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''txt = "apple banana cherry orange"
x = txt.split(" ")

print(x)'''

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

######################################################################
# THis is a code to convert decimal number to either Binary or octal
######################################################################

#this line takes options weather the user wants binary or octal
options = eval(input("1.octal\n2.binary\n"))

#This line converts to binary 
if options == 2:
    
    number = eval(input("Enter number to convert to binary:\n"))
    print("the binary equialant of this number is {:b}".format(number))

# And this convert to octal
elif options == 1:
    
    number = eval(input("Enter the number to convert to octal:\n"))
    print("the octal equialant of this number is {:o}".format(number))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
d = {}
for i in range(10):
    k = input("enter Employee name:")
    v = eval(input('Enter salary:'))
    d[k]=v
for k,v in d.items():
    if v >1000 :
        print(k,"have more than 1000 salary.")
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
a = {"adorn":20,"adithi":13}
b = {"akshay":16}
a.update(b)
print(a)
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
########################
#All the tuple functions
########################

tup = (2,3,45,56,45,70,6.9,3000,2910,838,520)

print(sorted(tup))
print(min(tup))
print(max(tup))
print(sum(tup))
print(tup.index(70))
print(tup.count(45))

'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
a = "adorn is the best"
print(a.split('e'))
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
d = {}
while True:
    print("Menu:")
    print("1.Add Data.")
    print("2.Display all element.")
    print("3.display one Element.")
    print("4.delete data.")
    print("5.update Dictionary.")
    c = eval(input("enter choice:"))
    if c == 1:
        i = int(input("item no:"))
        l = []
        n = input("enter name:")
        q = eval(input("enter quantity:"))
        p = eval(input("enter price:"))
        l.append(n)
        l.append(q)
        l.append(p)
        d[i]=l

    elif c == 2:
       print(d)

    elif c == 3:
        R = int(input("enter Item:"))
        f = 0
        for k,v in d.items():
            if k == R:
                print(d[k])
                f=1 
            if f == 0:
                print("no items")
    
    elif c == 4:
        d.pop()
        print("One Item removed",d)
    
    elif c == 5:

        i = int(input("enter item no:"))
        l = [] 
        h = input("enter Item name:")
        q = eval(input("enter quantity:"))
        p = eval(input("enter price:"))
        l.append(h)
        l.append(q)
        l.append(p)
        k[i]=l
        d.update(k)
    
    else:
        break
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''Practicing all the code before exam.'''
#1
'''print("hello")'''
#2
'''
r = eval(input("enter the radius of the cirle:"))
area = 3.14*r**2
print("area of the cirle is:",area)
'''
#3
'''
year = eval(input('enter year:'))
if year%4 == 0:
    print(year,"its a leap year.")
else:
    print(year,"its not a leap year.")
'''
#4
'''
p = eval(input("enter mark:"))
if p >= 90:
    G = "A"
elif p >= 75 and p<90:
    G = "B"
elif p>= 60 and p<75:
    G = "C"
else:
    G = "D"
print("Grade obtained:",G)
'''
#5
'''
n = eval(input("enter no"))
sum = 1
for i in range(1,n+1):
    sum += i
print(sum)
'''
#6
'''
p = eval(input("enter number:"))
for i in range(2,p):
    f = 0
    if p % i == 0:
        f = 1
if f == 0:
    print(p,"it is a prime number")
else:
    print(p,"not a prime no.")
'''
#7
'''
n = eval(input("enter range:"))
p = 1
pp = 0
c = 0
while n>0:
    print(c,end=",")
    pp = p 
    p = c
    c = p+pp
    n = n-1
'''
#8 
'''
L = 0
a = input("enter String:")
l = 0
d = 0
for i in a:
    if i.islower():
        l+=1
    elif i.isalpha():
        L+=1
    elif i.isdigit():
        d+=1
print("no of letters",L)
print("no of small letters",l)
print("no of digits",d)
'''
#9
'''
k = eval(input("enter number:"))
for i in range(2,k):
    f = 0
    if i%k == 0:
        f = 1
if f == 0:
    print(k,"is a prime number")
else:
    print(k,"is not prime number.")
'''
#10
'''
lst = eval(input("enter list:"))
n = len(lst)
mean = sum = 0
for i in range(0,n):
    sum+= lst[i]

mean = sum/n
print("mean =",mean)
'''
#11
'''
a = [1,2,3,4,4,5,6,]
a.append([2,4])
print(a)
a.extend([2,3])
print(a)
'''
#12
'''
lst = eval(input("enter list:"))
value = eval(input("enter the value you want to count:"))
freq = lst.count(value)
print(freq)
'''

