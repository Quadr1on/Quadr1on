def product(l1, l2):
    p = 0
    for i in l1:
        # print(i)
        for j in l2:
            # print(j)
            p += i * j
            # print(p)
            # print()

    return p


lst = [1, 2, 3, 4, 5, 6]
l1 = []
l2 = []
for i in lst:
    if i % 2 == 0:
        l1.append(i)
    else:
        l2.append(i)
print(l1)
print(l2)

print(product(l1,l2))
