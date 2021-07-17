n = input()
li = []
for i in range(len(n)):
    li.append(n[i])
li.sort(reverse=True)
for i in li:
    print(i, end='')
