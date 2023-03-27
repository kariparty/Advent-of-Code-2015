file = open('input_day3',"r")
content = file.readlines()

lst = []
t = []

for letter in content[0]:
    lst.append(letter)

# Part 1

point = [[0],[0]]

for r in lst:
    if r == '^':
        up = [[0],[1]]
        point = [[point[i][j] + up[i][j]  for j in range(len(point[0]))] for i in range(len(point))]
    if r == '>':
        right = [[1],[0]]
        point = [[point[i][j] + right[i][j]  for j in range(len(point[0]))] for i in range(len(point))]
    if r == 'v':
        down = [[0],[-1]]
        point = [[point[i][j] + down[i][j]  for j in range(len(point[0]))] for i in range(len(point))]
    if r == '<':
        left = [[-1],[0]]
        point = [[point[i][j] + left[i][j]  for j in range(len(point[0]))] for i in range(len(point))]
    t.append(point)

l1 = []
count = 0

for item in t:
    if item not in l1:
        count += 1
        l1.append(item)
 
print(count) #Part 1 answer

# Part 2

s = []
count = 0
robopoint = [[0],[0]]
santapoint = [[0],[0]]

for r in lst:
    count = count + 1
    if count%2 == 0:
        if r == '^':
            up = [[0],[1]]
            robopoint = [[robopoint[i][j] + up[i][j]  for j in range(len(robopoint[0]))] for i in range(len(robopoint))]
        if r == '>':
            right = [[1],[0]]
            robopoint = [[robopoint[i][j] + right[i][j]  for j in range(len(robopoint[0]))] for i in range(len(robopoint))]
        if r == 'v':
            down = [[0],[-1]]
            robopoint = [[robopoint[i][j] + down[i][j]  for j in range(len(robopoint[0]))] for i in range(len(robopoint))]
        if r == '<':
            left = [[-1],[0]]
            robopoint = [[robopoint[i][j] + left[i][j]  for j in range(len(robopoint[0]))] for i in range(len(robopoint))]
        s.append(robopoint)
    else:
        if r == '^':
            up = [[0],[1]]
            santapoint = [[santapoint[i][j] + up[i][j]  for j in range(len(santapoint[0]))] for i in range(len(santapoint))]
        if r == '>':
            right = [[1],[0]]
            santapoint = [[santapoint[i][j] + right[i][j]  for j in range(len(santapoint[0]))] for i in range(len(santapoint))]
        if r == 'v':
            down = [[0],[-1]]
            santapoint = [[santapoint[i][j] + down[i][j]  for j in range(len(santapoint[0]))] for i in range(len(santapoint))]
        if r == '<':
            left = [[-1],[0]]
            santapoint = [[santapoint[i][j] + left[i][j]  for j in range(len(santapoint[0]))] for i in range(len(santapoint))]
        s.append(santapoint)

l1 = []
count = 0

for item in s:
    if item not in l1:
        count += 1
        l1.append(item)
 
print(count) #Part 2 answer