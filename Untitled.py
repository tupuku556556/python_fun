#!/usr/bin/env python
# coding: utf-8

# In[4]:


name=input()
age=int(input())
year=2020
add=age+year
print("your age will be 100 in the year", add)


# In[23]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in a:
    if i<5:
        b.append(i)
    
    
print(b)
        


# In[26]:


from random import randint

value = randint(0, 100)
print(value)


# In[30]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for e in a:
    for i in b:
         if i==e:
            c.append(i)


#print(c)
c=list(dict.fromkeys(c))
print(c)


# In[31]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l=list(dict.fromkeys([e for e in a for i in b if i==e]))
print(l)


# In[36]:


import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_big_arr = []
        for i in range(len(nums1)):
            new_big_arr.append(nums1[i])
        for i in range(len(nums2)):
            new_big_arr.append(nums2[i])
        
        print(new_big_arr)
        return statistics.median(new_big_arr)


# In[ ]:




