#좋은날0, 싫은날1
#00,01,10,11
# n, yest= map(int, input().split())
# a,b,c,d = map(float, input().split())
#잘못 접근해서 시간이 좀 많이 걸렸다,,,
n = 2
yest = 1
a,b,c,d = 0.70, 0.30, 0.50, 0.50


if yest == 0:
    ha = a
    unha = b
elif yest == 1:
    ha = c
    unha = d

for i in range(n-1):
    tem = ha*a + unha*c
    unha = ha*b + unha*d
    ha = tem
    
print(round(ha*1000), round(unha*1000))