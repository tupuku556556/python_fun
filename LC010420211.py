#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def longestPalindrome(self,s: str) -> str:
        # return the letter if one char long
        if len(s) == 1:
            return s[0]
        s_len = len(s)
        # create a 2 by 2 array
        palendrome = [[False] * s_len for i in s]
        longest = s[0]
        # iterate through i which is the length of the palindrom
        for i in range(0, s_len):
            # iterate through j which the starting position
            for j in range(0, s_len - i):
                # check if opposite ends are equal
                eq = s[j] == s[i + j]
                # one letter long (index 0) is always a palindrome
                if i == 0:
                    palendrome[i][j] = True
                    continue
                # check if two letters long is equal because this is an edge case
                elif i == 1 and eq:
                    palendrome[i][j] = True
                    longest = s[j:i + j + 1]
                # check if the first and last letter are equal also if the sandwhiched part is a palindrome
                elif  eq and palendrome[i-2][j+1]:
                    palendrome[i][j] = True
                    # update the longest one
                    longest = s[j:i + j + 1]
                else:
                    palendrome[i][j] = False
        return longest

