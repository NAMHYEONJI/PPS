li = input().split('-') 
res = 0 

for i in li[0].split('+'): 
    res += int(i) 
    
for i in li[1:]: 
    for j in i.split('+'): 
        res -= int(j)
print(res)
