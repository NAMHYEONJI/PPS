n = int(input())

li=[]
for i in range(n):
    li.append(input())


li = list(set(li))
# print(li)
len_li = []

for i in li:
    len_li.append((len(i), i))

sort_li = sorted(len_li)

for i in sort_li:
    print(i[1])
