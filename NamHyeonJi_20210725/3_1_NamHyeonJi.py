def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    a_cnt = 0
    l_cnt = 0
    check = 0
    for i in s:
        if i == 'A':
            a_cnt +=1
        elif i == 'L' and check == 0:
            check = 1
            l_cnt = 1
        elif i == 'L' and check == 1:
            l_cnt+=1
        else:
            check = 0

    if l_cnt == 3 or a_cnt == 2:
        return False
    else:
        return True
'''
s = "PPALLP"
print(checkRecord(s))
'''