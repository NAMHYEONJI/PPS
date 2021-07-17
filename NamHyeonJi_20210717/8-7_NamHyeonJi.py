#이분탐색 알고리즘 사용
n = int(input())
a = list(sorted(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

def binary(num, a, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if num == a[m]:
        return 1
    elif num < a[m]:
        return binary(num, a, start, m-1)
    else:
        return binary(num, a, m+1, end)


for i in b:
    start = 0
    end = n-1
    print(binary(i, a, start, end))
        
        

    
    
