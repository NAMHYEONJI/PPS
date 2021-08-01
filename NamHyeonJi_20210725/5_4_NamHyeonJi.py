def dayOfYear(date):
    """
    :type date: str
    :rtype: int
    """
    date = date.split("-")
    date = list(map(int, date))
    res = date[2]
    check = 0

    if date[0] % 4 == 0 :
        check = 1
    if date[0] % 4 == 0 and date[0] % 100 == 0:
        check = 0
    if date[0] % 4 == 0 and date[0] % 100 == 0 and date[0] % 400 == 0:
        check = 1 
    
    if check == 1 and date[1] >= 3:
        res+=1

    days = [31,28,31,30,31,30,31,31,30,31,30]
   
    if date[1] >= 2 :
        for i in range(date[1]-1):
            res += days[i]
    return res

date = "2004-03-01"
print(dayOfYear(date))