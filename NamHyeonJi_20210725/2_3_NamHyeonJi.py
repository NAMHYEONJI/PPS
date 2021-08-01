def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        min_len = 999
        for i in strs:
            le = len(i)
            if len < min_len:
                min_len = len

        i = 0

        while i < min_len:
            prefix = []
            for idx, str in enumerate(strs):
                if len(prefix) <= 0:
                    if idx == 0:
                        prefix.append(str[i])
                    else:
                        break
                else:
                    if prefix[0] != str[i]:
                        prefix.pop()
            
            if len(prefix) == 0:
                break;
            else:
                i += 1
                res += prefix[0]
                
        return res
