#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
a=input('Enter a string:')
print(a[::-1])


# In[4]:


#Q2

def string_func(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_func("abcSdefPghijQkl")


# In[5]:


#Q3

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([5,9,8,7,7,4,5])) 


# In[7]:


#Q4

words=[n for n in input().split('-')]
words.sort()
print('-'.join(words))


# In[8]:


#Q5

a=input("Enter a few lines:")
print(a.upper())


# In[10]:


#Q6

def calculateSum (a,b):
    SUM = int(a) + int(b)
    return SUM
Num1="10"
Num2="80"

print(calculateSum(Num1,Num2))


# In[21]:


#Q7

def max_length(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
        
print(max_length("Apple","Dog"))
print(max_length("Apple","Doggy"))


# In[27]:


#Q8

def Tuple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

Tuple()


# In[34]:


#Q9

def showNumbers(limit):
    for i in range(limit+1):
        if (i%2==0):
            print (i,"EVEN", end=" ")
        else:
            print(i,"ODD", end=" ")

        print()

print(showNumbers(3))


# In[46]:


#Q10
def even(x):
    return x%2==0

even_list = filter(even,range(1,21))

print(list(even_list))


# In[47]:


#Q11

def even(x):
    return x%2==0

def sqr(x):
    return x*x

l = [1,2,3,4,5,6,7,8,9,10]
l = map(sqr,filter(even,l))   # first filters number by even number and the apply map() on the resultant elements
print(list(l))


# In[48]:


#Q12

def div():
    return 5/0

try:
    div()
except ZeroDivisionError as ze:
    print("It's not divisible")


# In[55]:


#Q13
from functools import reduce
reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7], 0)


# In[66]:


#Q14
def multiple(n):
    return n%7==0
my_list = [12, 7, 54, 49, 45, 72, 225]


result = list(filter(lambda x: (x % 3 ) and multiple(7), my_list))


print("Numbers not divisible by 3 but multiple by 7 are",result)


#numbers = (1, 2, 3, 4)
#result = map(calculateSquare, numbers)
#print(result)


# In[70]:


#Q15

#(i)
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

#(ii)

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()


# In[ ]:




