n, l = map(int, input().split())
li = list(map(int, (input().split())))

li.sort()

for i in li:
    if i <= l:
        l+=1

print(l)