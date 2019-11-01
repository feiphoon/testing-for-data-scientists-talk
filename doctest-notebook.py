#!/usr/bin/env python
# coding: utf-8

# # A quick `doctest` test

# In[11]:


def addition(x, y):
    """Returns the value of x plus y.

    >>> addition(1, 2)
    3
    >>> addition(0, 0)
    0
    >>> addition(-2, 2)
    0
    """
    return x+y


# In[12]:


import doctest
doctest.testmod()


# In[ ]:




