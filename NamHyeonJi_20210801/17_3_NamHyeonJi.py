n = int(input())

dp = [0] * (n+1)
c = [0] + list(map(int, input().split()))
dp[1] = c[1]
for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + c[j]:
            dp[i] = dp[i-j] + c[j]
print(dp[n])