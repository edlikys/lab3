#!/usr/bin/env python
# coding: utf-8

# In[5]:


all = open('file.txt', 'r')
s = all.read().lower().strip().split()
y = 0
m =''
for i in s:
    z = s.count(i)
    if z >= y:
        y = z
        m = i
print(m, y)


# In[ ]:




