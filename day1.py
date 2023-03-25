file = open('input_day1',"r")
content = file.readlines()

z = []
t = 0
b = 0

for f in content[0]:
    z.append(f)
    
for s in z:
    if s == '(':
        t = t + 1
    else:
        t = t - 1
    b = b + 1
    if t == -1:
        print(b) #Part 2

print(t) #Part 1