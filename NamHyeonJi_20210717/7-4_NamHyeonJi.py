s = input()
li = ['']*len(s)

for i in range(len(s)):
    li[i] = s[i:]

li.sort()

for i in li:
    print(i)