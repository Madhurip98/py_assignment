#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Q1


LIST = [12, 3.14,"Apple","2+bj",33,4.667,"Cat","c+dj","Dog",6.98]
print(LIST)


# In[12]:


#Q2
l1=[1,6,4.5,"Animal",9.0]
print(l1[::])
print(l1[2:])
print(l1[:2])
print(l1[2:4])
print(l1[::2])
print(l1[::-2])
print(l1[1:4:2])


# In[17]:


#Q3
from math import prod
l2=[2,3,4,8,9]
print(sum(l2))
print(prod(l2))


# In[18]:


#Q4

l3=(2,5,4,9,8,0,3)
print('Largest:',max(l3))
print('Smallest:',min(l3))


# In[20]:


#Q5

list = [5,8, 122, 60, 55, 20, 29]
list = [x for x in list if x%2!=0]
print(list)


# In[56]:


#Q6

sqr_list = [] 
for i in range(1,31): 
  sqr_list.append(i*i) 
 
print( sqr_list[:6]+sqr_list[-6:]) 


# In[57]:


#Q7

l1 = [1,3,5,7,9,10]
l2 = [2, 4, 6, 8]
l1[-1:] = l2
print(l1)


# In[60]:


#Q8

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3 = {}
for d in (dic1, dic2): dic3.update(d)
print(dic3)


# In[63]:


#Q9


n=int(input("Enter a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 


# In[64]:


#Q10

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


# In[ ]:




