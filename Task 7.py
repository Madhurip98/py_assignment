#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Q1
import math
[C,D]=[50,30]
num=input('Enter D:')
result=[]
for D in num:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result.append(Q)

print(result)


# In[11]:


#Q2

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

A = Square(5)
print(A.area())    

print(Square().area()) 


# In[19]:


#Q3

class MYCLASS:
    def threeELEM(self, n):
       
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (self[i] + self[j] + self[k] == 0):
                        print(self[i], self[j], self[k])
                        
self= [-25,-10,-7,-3,2,4,8,10]
n = len(self)
print(MYCLASS.threeELEM(self,n))


# In[41]:


#Q4

class Time:
    
    
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def addTime(t1, t2):
        t3 = Time(0, 0) 
        t3.hours = t1.hours + t2.hours 
        t3.minutes = t1.minutes + t2.minutes 
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3

    def displayTime(self):
        print(self.hours, self.minutes)

    def displayMinutes(self):
        print((self.hours * 60) + self.minutes, "minutes")

a = Time(2, 50)
b = Time(1, 20)
c = Time.addTime(a,b)

c.displayTime()
c.displayMinutes()



# In[89]:


class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if (initialAge < 0):
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge    
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if ( self.age < 13 ):
            print("You are young.")
        elif ( self.age >= 13 and self.age < 18 ):
            print("You are a teenager.")
        else:
            print("You are old.")        
    def yearPasses(self):
        self.age += 1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()

for j in range(0, t):
    yearPasses = int(input()) 
    p = Person(age) 
    p.yearPasses()       
    
    


# In[ ]:




