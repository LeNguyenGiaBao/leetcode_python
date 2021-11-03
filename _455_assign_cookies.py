def findContentChildren(g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        
        gi = len(g) - 1
        si = len(s) - 1
        count = 0
        
        while (gi >=0 and si >=0):
            if (s[si] >= g[gi]):
                count += 1
                gi -= 1
                si -= 1
            else:
                gi -= 1
        
        return count