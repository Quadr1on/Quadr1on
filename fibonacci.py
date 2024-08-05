n = eval(input("enter range:"))
c = 0
p = 1
pp = 0
for i in range(n):
    print(c,end=',')
    pp = p
    p = c 
    c = p+pp
