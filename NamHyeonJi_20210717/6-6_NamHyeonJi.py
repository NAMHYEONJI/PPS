n = int(input())

li = []
for i in range(n):
    num = input()
    li.append(num)


for i in range(n-1):
    for j in range(i+1, n):
        if len(li[i]) > len(li[j]):
            li[i], li[j] = li[j], li[i]

        elif len(li[i]) == len(li[j]):
            a=0
            b=0
            for x,y in zip(li[i],li[j]):
                if x.isdigit():
                    a+=int(x)
                if y.isdigit():
                    b+=int(y)
            if a > b:
                li[i],li[j] = li[j], li[i]

            elif a == b:
                for x,y in zip(li[i], li[j]):
                    if x > y:
                        li[i],li[j] = li[j], li[i]
                        break
                    elif x < y:
                        break


for i in li:
    print(i)