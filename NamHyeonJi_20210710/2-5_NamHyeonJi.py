#이것도 더 짧게 풀 수 있을 거 같은데 모르겠다
word = input()
word = word.upper()

dic ={}

for i in range(len(word)):
    if word[i] != '0':
        alpha = word[i]
        cnt = word.count(word[i])
        word = word.replace(word[i], "0")
        dic[alpha] = cnt

max = 0
check = 0 
for k, v in dic.items():
    if v > max :
        max = v
        key = k
        check = 0
    elif v == max:
        check = 1

if check == 1:
    print("?")
else:
    print(key)
    

