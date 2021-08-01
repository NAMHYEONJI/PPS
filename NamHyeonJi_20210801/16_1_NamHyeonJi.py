def divisorGame(n): 
    cnt = 0 

    while n!=1: 
        li = [] 
        for i in range(1, n): 
            if n%i == 0: 
                li.append(i) 
        n = n - li[0] 
        cnt += 1 
    if cnt % 2 ==0: 
        return False 
        
    else: 
        return True

print(divisorGame(3))