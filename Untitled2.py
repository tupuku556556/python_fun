#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def longestPalindrome(self, s: str) -> str:
        b = ''
        k = 0
        flag = 0
        l = 0
        z = 0
        for i in s: 
            if flag == 0:
                pass
            else:
                k+=1
                s = s[1:]
            for j in s:
                b+=j
                
                if b == b[::-1]:
                    l = len(b)
                if l > z:
                    z = l
                    ans = b
                                    
            b = ''
            flag = 1
        return (ans)

