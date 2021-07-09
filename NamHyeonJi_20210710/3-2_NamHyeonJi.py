str = input()
cnt = 0
for i in range(len(str)):
    print(str[i], end="")
    cnt += 1
    if cnt == 10:
        cnt = 0
        print("")