def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    num = str(num)
    cnt = 0

    while len(num) != 1:
        for i in num:
            cnt += int(i)
        num = str(cnt)
        cnt = 0

    return int(num)
print(addDigits(38))