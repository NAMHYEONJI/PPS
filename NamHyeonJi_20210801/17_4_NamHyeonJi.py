def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if sorted(s) == sorted(t):
        return True
    else:
        return False

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))