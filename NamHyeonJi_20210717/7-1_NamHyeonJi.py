n = int(input())
li = []
for i in range(n):
    age, name = map(str,input().split())
    li.append((int(age), name))

li.sort(key = lambda item: (item[0]))

for i in range(n):
    print(li[i][0], li[i][1])