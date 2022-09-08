#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q1
try:
    x==str
    
except Exception as e:
    print("Syntax Error occured and Handled",e)


# In[17]:


#Q2
import sys

assert len(sys.argv) >= 2
try:
    f=open(sys.argv[1],'r')
    data = f.read()
except Exception:
    print("enter name again")


# In[22]:


#Q3

try:
    num=input('enter a num:')
    if num(len)<=4:
        print("correct")
        
        
except Exception:
    print('The length is too short/long !!! Please provide only four digits')
        


# In[29]:


#Q4

print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    retype_password = input(' re-type password')
    if password=='password23' and username=='iam_admin' and retype_password == password:
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1


# In[39]:


#Q6
my_file = open("doc.txt", "r")
for str in my_file:
   
   if len(str)%2==0:
        print(str)
print(my_file.read())



# In[ ]:




