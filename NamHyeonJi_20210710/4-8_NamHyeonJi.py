#시간을 초과해서 어떻게 바꿀까 고민을 좀 했다
a, b, c = map(int, input().split())
if b >= c:
    print("-1")
else:
    print(int(a/(c-b)+1))