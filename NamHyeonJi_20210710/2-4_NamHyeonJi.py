#뭔가 더 짧게도 풀 수 있을 거 같은데 잘 모르겠다
dial = input()

dial_len = len(dial)

time = 0

for i in range(dial_len):
    n = ord(dial[i])
    if 65<=n<=67:
        time += 3
    elif 68<=n<=70:
        time += 4
    elif 71<=n<=73:
        time += 5
    elif 74<=n<=76:
        time += 6
    elif 77<=n<=79:
        time += 7
    elif 80<=n<=83:
        time += 8
    elif 84<=n<=86:
        time += 9
    elif 87<=n<=90:
        time += 10
print(time)
