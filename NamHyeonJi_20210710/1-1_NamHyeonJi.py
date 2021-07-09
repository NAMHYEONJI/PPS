#그냥 풀렸다...
a = list(map(int,input().split()))
check = 0
for i in range(7):
    if a[i] < a[i+1]:
        check += 1
    elif a[i] > a[i+1]:
        check -= 1


if check == 7:
    print("ascending")
elif check == -7:
    print("descending")
else:
    print("mixed")


