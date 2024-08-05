f = open('lines.txt','r')
s = f.read()
x = s.split()
l = []
for i in x:
    if i.lower() == 'he':
        l.append('she')
    elif i.lower() == 'she':
        l.append('he')
    else:
        l.append(i)

for i in l:
    print(i,end=' ')

