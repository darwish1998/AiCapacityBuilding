#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[8]:


my_list = [1,'hi']
my_list
type(my_list)


# In[13]:


array_t = np.array([1,2,'f',5])
print(array_t)

type(array_t)


# In[21]:


my_list2 = [1,2,3,4,0]
type(my_list2)
np.array(my_list2)


# In[24]:


ar_2d = [[1,2],[3,4],[5,6]]
ar_2d


# In[28]:


ar_3d = np.array(ar_2d)
ar_3d


# In[32]:


ar_2d = np.arange(12,25,2)
ar_2d


# In[38]:


ary = np.linspace(2,20,6)
ary


# In[39]:


ar_2d = np.array(ar_2d)
ar_2d


# In[44]:


t_z = np.ones((3,6))
t_z


# In[47]:


t_z = np.ones((3,6))
t_z


# In[60]:


f= np.full((3,3),4.5)
f
f2 = np.full((3,5,3),10) # Start no. of matrix follow no. rows then columns number....
f2


# In[66]:


x= np.random.rand(4,2)
x


# In[70]:


x.transpose()


# In[72]:


#Arrays shape


# In[75]:


ar= np.ones(4)
ar


# In[77]:


print(ar)
print(ar.ndim)
print(ar.shape)
print(ar.size)


# In[79]:


print(f"Dimension: {ar.ndim}")
print(f"    shape: {ar.shape}")
print(f"     size :{ar.size}")


# In[87]:


def print_array(ar):
    print(f"Dimensions: {ar.ndim}")
    print(f"     Shape: {ar.shape}")
    print(f"      Size: {ar.size}")
    print("")
    print(ar)


# In[92]:


ar= np.ones((3,6))
print_array(ar)


# In[105]:


ar_d = np.ones((2,3,2,2))
print_array(ar_d)


# # Broadcasting 
# 

# In[113]:


cost = np.array([20, 15, 25])
print("Pie cost:" , cost)
#print(cost)


# In[114]:





# In[117]:


sales = np.array([[2, 3, 1], [6, 3, 3], [5, 3, 5]])
print("\nPie sales (#):")
print(sales)


# In[118]:


total = np.zeros((3, 3))  # initialize an array of 0's
for col in range(sales.shape[1]):
    total[:, col] = sales[:, col] * cost
total

