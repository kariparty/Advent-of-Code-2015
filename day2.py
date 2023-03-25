file = open('input_day2',"r")
content = file.readlines()

d = []
for f in content:
    c = f.split('x')
    for x in c:
        d.append(x.replace("\n", ""))

subList = [d[n:n+3] for n in range(0, len(d), 3)]


# Part 1

e = 0

for i in subList:
    x = int(i[0]) * int(i[1])
    y = int(i[1]) * int(i[2])
    z = int(i[0]) * int(i[2])
    f = 2 * (x + y + z) + min(x,y,z)
    e = e + f


# Part 2

import math
s = 0

for i in subList:
    for t in range(0, len(i)):
        i[t] = int(i[t])
    i.sort()
    r = 2 * (i[0] + i[1]) + (i[0] * i[1] * i[2])
    s = s + r

print(s)