#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers=eval(input("enter Tuple :"))
even=0
odd=0
for days in numbers:
    if days%2==0:
        even=even+1
    else:
        odd=odd+1
print("number of even numbers are :",even)
print("number of odd numbers  are :",odd)


# In[ ]:




