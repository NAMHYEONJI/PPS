str = input()
alpha = [ 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]

cnt = 0
i = 0
while i < len(str):
    if (str[i:i+3] in alpha):
        i = i+3
    elif (str[i:i+2] in alpha):
        i = i+2
    else:
        i = i+1
    cnt = cnt+1
 
print(cnt)
    