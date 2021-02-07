#!/usr/bin/env python
# coding: utf-8

# In[21]:


text="paypalishiring"
#from string import ascii_lowercase
for i in range(0,len(text), 3):
    for i in range(0,len(text), 1):
        text += text[i:i+1] + ' '

from itertools import zip_longest
for x in zip_longest(*text.split()):
    print (' '.join(x))


# In[ ]:




