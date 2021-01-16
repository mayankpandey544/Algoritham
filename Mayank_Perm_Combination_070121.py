#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
from itertools import product
box_1=['g','b']
box_2=['g','b','y']
perm=[]
for p in itertools.product(box_1, repeat=2):
    perm.append(p)
perm


# In[20]:


perm=[]
for p in itertools.product(box_2, repeat=3):
    perm.append(p)
print(perm)


# In[21]:


perm=itertools.permutations(box_1)
for i in list(perm):
    print(i)


# In[22]:


perm=itertools.permutations(box_1)
for i in list(perm):
    print(i)


# In[23]:


perm=[]
for p in itertools.product(box_2, repeat=2):
    perm.append(p)
print(perm)


# In[24]:


perm= itertools.permutations(box_2,2)
for p in list(perm):
    print(p)


# In[25]:


from itertools import combinations_with_replacement
comb=combinations_with_replacement(box_1,2)

for c in list(comb):
    print(c)


# In[26]:


comb=combinations_with_replacement(box_2,2)

for c in list(comb):
    print(c)


# In[18]:


from itertools import combinations
comb= combinations(box_1,2)

for c in list(comb):
    print(c)


# In[19]:


from itertools import combinations
comb= combinations(box_2,2)

for c in list(comb):
    print(c)


# In[ ]:




