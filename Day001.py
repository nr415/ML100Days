#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
np.__version__


# In[12]:


#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
a = np.arange(0, 21, 1)
a


# In[13]:


#2.呈上題，將以上數列取出偶數。
a=a[a>0]
a[a%2==0]


# In[14]:


a[a%3==0]


# In[ ]:




