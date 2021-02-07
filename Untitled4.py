#!/usr/bin/env python
# coding: utf-8

# In[5]:


text="paypalishiring"
for ele in text:
    print(" ".join(text))


# In[16]:


s="paypalishiring"
n=3
#sl=[s[i:i+n]for i in range(0,len(s),n)]
#print(sl)
result=' ',join((s[i:i+2] for i in range(0, len(s), 2))
print(result)
#".join(s[i:i+2] for i in range(0, len(s), 2))


# In[14]:


string = "23edfd56ab90"
print ':'.join([string[i:i+2] for i in range(0, len(string), 2)])


# In[19]:


a="paypalishiring"
r=' '.join([a[i:i+3] for i in range(0, len(a), 3)])
print(r)


# In[20]:


s="paypalishiring"
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        w, h = 100, 100
        bucket = [[None] * w for i in range(h)]
        result = [""] * numRows
        i = 0
        for c in s:
            if i == numRows - 1:
                down = False 
            elif i % numRows == 0:
                down = True 
            result[i] += c
            i = i + 1 if down else max(i - 1, 0) # max() for edge case
        return ''.join(result)


# In[ ]:




