#input 대신 sys.stdin.readline을 사용
import sys
n = int(input())

for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
