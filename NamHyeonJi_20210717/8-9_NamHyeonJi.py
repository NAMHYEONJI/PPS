#브루트포스 알고리즘
li = [0]*9
sum = 0
for i in range(9):
    li[i] = int(input())
    sum += li[i]

br = True
for i in range(9):
    for j in range(i+1, 9):
        res = sum - (li[i]+li[j])
        if res == 100:
            a = i
            b = j
            br = False
            break
        if br == False:
            break

for i in range(9):
    if i == a or i == b:
        continue
    else:
        print(li[i])
        
