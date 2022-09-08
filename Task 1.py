#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Question 1

a, b, c = 4, "geeks", 3.14
print("a=",a)
print("b=",b)
print("c=",c)


# In[4]:


#Q2

a=1+2j
b=10
a,b=b,a
print(a,b)


# In[5]:


#Q3
#a)
a=1+2j
b=10
temp=a
a=b
b=temp
print(a,b)

#b)
a=1+2j
b=10
a,b=b,a
print(a,b)


# In[3]:


#Q4

import future        # pip install future
import builtins      # pip install future
import past          # pip install future
import six 

# Python 2 and 3:
from __future__ import print_function    # (at top of module)

print('Hello', 'Maddy')


# In[20]:


#Q5

#User= input('Enter any 2 numbers between 1-10:')
#z=(User)

z = 0

for i in range (0,2):
    z = float(input("Enter any 2 numbers between 1-10: "))
    sum = sum + z
    result=30+z
    

z=print(result)


# In[34]:


#Q6
z= "string"

print('The data type of the input value is :',type(z))


# In[58]:


#Q7

str="my name is"
def uppercamelcase(str):
    return "".join(str.title().split())

    return ans2
def lowercamelcase(str):
    content = "".join(str.title().split())
    return content[0].lower() + content[1:]

def snakecase(str):
    return "_".join(str.lower().split())

a=uppercamelcase(str)
print(a)
b=lowercamelcase(str)
print(b)
c=snakecase(str)
print(c)
d=str.upper()
print(d)


# In[ ]:


#Q8

#Yes, when a different data type is assigned to 'a' again than it's older data type, the value will change becuase the values are dynamically typed in python since it is a dynamcial programming language.

