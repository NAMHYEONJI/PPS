n = int(input())
def group_word(x):
    li=[]

    li.append(word[0])
    for i in range(1,len(word)):
        if word[i-1] != word[i]:
            li.append(word[i])

    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i] == li[j]:
                return False
    return True
cnt = 0
for i in range(n):
    word = input()
    if group_word(word):
        cnt+=1

print(cnt)