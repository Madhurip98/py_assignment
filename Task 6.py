#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q2




students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']


for i in range(0,1):
    new=dict(zip(students,subjects))
    print(new)


# In[4]:


#Q1

str1 = "United States"
 
x = [char for char in str1 if char.isupper()]
 
# printing result
print("The uppercase characters in string are : " + str(x))


# In[9]:


#Q4

def rev_gen(str):
    l = len(str)
    for i in range(l-1, -1, -1):
        yield str[i]
        
for char in rev_gen("Consultadd Training"):
    print(char)


# In[11]:


#Q5
#example for decorator

def uppercase_dec(function):
    def func2():
        func1 = function()
        make_up = func1.upper()
        return make_up

    return func2

def exp():
    return 'I am Maddy'

decorate = uppercase_dec(exp)
decorate()


# In[ ]:




