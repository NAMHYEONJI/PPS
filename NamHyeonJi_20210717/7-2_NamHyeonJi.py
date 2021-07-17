m, n = map(int,input().split())

dic = {}
def num_to_word(x):
    if x =='0':
        return "zero"
    elif x =='1':
        return "one"
    elif x =='2':
        return "two"
    elif x =='3':
        return "three"
    elif x =='4':
        return "four"
    elif x =='5':
        return "five"
    elif x =='6':
        return "six"
    elif x =='7':
        return "seven"
    elif x =='8':
        return "eight"
    elif x =='9':
        return "nine"
        
for i in range(m, n+1):
    num = str(i)
    st = ''
    for j in range(len(num)):
        st = st + num_to_word(num[j])
    dic[st] = i

cnt = 1

for key, value in sorted(dic.items()):
    print(value, end=' ')
    if cnt % 10 == 0 :
        print("")
    cnt += 1

    