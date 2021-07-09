#원래 이렇게 복잡하게 푸는게 맞는 것인가...
def vowel_check(x):
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' :
        return True


def password(x):
    pw_len = len(x)
    li = [0] * pw_len
    vo_cnt = 0
    con_cnt = 0
    for i in range(pw_len-1):
        if x[i] == x[i+1] and x[i] != 'e' and x[i] != 'o':
            return False
        elif vowel_check(x[i]) :
            li[i] = 1
            vo_cnt += 1
        else:
            li[i] = -1
            
    if vowel_check(x[pw_len-1]):
        li[pw_len-1] = 1
        vo_cnt += 1
    else:
        li[pw_len-1] = -1
        
    if vo_cnt == 0:
        return False
    
    for i in range(pw_len-2):
        if li[i] == li[i+1] and li[i+1] == li[i+2]:
            return False
    else:
        return True

pw = input()
while pw != 'end':
    if password(pw):
        print("<", end='')
        print(pw, end='')
        print("> is acceptable.")
    else:
        print("<", end='')
        print(pw, end='')
        print("> is not acceptable.")
    pw = input()
