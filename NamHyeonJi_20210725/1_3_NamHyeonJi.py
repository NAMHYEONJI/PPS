def findContentChildren(g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        cnt = 0
        idx = 0
        for i in range(0, len(s)):
            for j in range(idx, len(g)):
                if s[i] >= g[j]:
                    cnt += 1
                    idx = j + 1
                    break

        return cnt
        
g = [1,2,3]
s = [1,1]
print(findContentChildren(g,s))      