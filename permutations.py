def Permutation(n,r): 
#calculating n!
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
#calculating (n-r)!
    factr = 1
    x = n-r
    for i in range(1,x+1):
        factr *= i

    nPr = fact/factr
    print(nPr)
    
n = eval(input('enter n:'))
r = eval(input('enter r:'))

Permutation(n,r)

