#이렇게 풀어도 되는 것인가...
n = int(input())
first = int(input())

if first == 0:
    second = 1
else:
    second = 0

if n > 5:
    print("Love is open door")
else:
    for i in range(n-1):
        if i % 2 == 0:
            print(second)
        else:
            print(first)