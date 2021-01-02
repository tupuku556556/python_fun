#!/usr/bin/env python
# coding: utf-8

# In[22]:


import collections
the_string="abcabcabc"
results = collections.Counter(the_string)
print(results)


# In[25]:


#!python2

# import module
from collections import Counter

# get the indices
def getIndices(length):
    # holds the indices
    specific_range = []; all_sets = []

    # start building the indices
    for i in range(0, length - 2):

        # build a set of indices of a specific range
        for j in range(1, length + 2):
            specific_range.append([j - 1, j + i + 3])

            # append 'specific_range' to 'all_sets', reset 'specific_range'
            if specific_range[j - 1][1] == length:
                all_sets.append(specific_range)
                specific_range = []
                break

    # return all of the calculated indices ranges
    return all_sets

# store search strings
tmplst = []; combos = []; found = []

# string to be searched
mystring = "abcdthisisatextwithsampletextforasampleabcd"
# mystring = "abcdthisisatextwithtextsampletextforasampleabcdtext"

# get length of string
length = len(mystring)

# get all of the indices ranges, 4 and greater
all_sets = getIndices(length)

# get the search string combinations
for sublst in all_sets:
    for subsublst in sublst:
        tmplst.append(mystring[subsublst[0]: subsublst[1]])
    combos.append(tmplst)
    tmplst = []

# search for matching string patterns
for sublst in all_sets:
    for subsublst in sublst:
        for sublstitems in combos:
            if mystring[subsublst[0]: subsublst[1]] in sublstitems:
                found.append(mystring[subsublst[0]: subsublst[1]])

# make a dictionary containing the strings and their counts
d1 = Counter(found)

# filter out counts of 2 or more and print them
for k, v in d1.items():
    if v > 1:
        print (k, v)


# In[ ]:




