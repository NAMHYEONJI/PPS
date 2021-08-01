def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    res = []
    for i in s:
        if i.isalnum():
                res.append(i.lower())
    for i in range(int(len(res)/2)):
        if res[i] != res.pop():
            return False
    return True
    
s = "race a car"
print(isPalindrome(s))
    