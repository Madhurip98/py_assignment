#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1
num1=int(input("Enter your number:"))
if(num1%3==0):
    print("Consultadd")     
elif(num1%5==0):
    print("Python Training")
elif((num1%3==0) & (num1%5==0)):
    print("Consultadd - Python Training")


# In[24]:


#Q2

num1 = input("Enter First Number: ")
num2 = input("Enter Second Number: ")

print("Enter which operation would you like to perform?")
ch = input("Enter any of operations: ")

result=0

if ch == '+':
    result = num1 + num2;

elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
elif ch == 'avg':
    first=int(input('Enter first number:'))
    second=int(input('Enter second number:'))
    result= (first+second)/2
elif result < 0:
    print("NEGATIVE")

print(num1, ch , num2, ":", result)


# In[19]:


#Q3

a=10
b=20
c=30
avg=(a+b+c)/3
print("Avg:",avg)
if avg > a and avg >b and avg >c:
    print('Avg is higher than a,b,c')
elif avg > a and avg > b:
    print('Avg is higher than a,b,c')
elif avg > a and avg > c:
    print('Avg is higher than a,c')
elif avg > b and avg > c:
    print('Avg is higher than b,c')
elif avg > a:
    print('Avg is just higher than a')
elif avg > b:
    print('Avg is just higher than b')
elif avg > c:
    print('Avg is just higher than c')
                
            


# In[30]:


#Q4

 

for i in range(-2,5):
    
    if i < 0:
        print("it's over!")
        
    if i >0:
        print('good going')
        break


# In[31]:


#Q5

for i in range(1999,3201):
    if i%7==0 and i%5:
        print(i)


# In[35]:


#Q6

x=123

i = 0

count = 0
for i in x:
    print(i)


# In[36]:


#Q6 
#PART 2

i = 0



while i < 5:
    print(i)
i += 1
if i == 3:
    break
else:
    print('error')


# In[37]:


#Q6 
#PART 3
count=0

while True:
    print(count)
count += 1
if count >= 5:
    break


# In[38]:


#Q7

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")


# In[39]:


#Q8

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)


# In[41]:


#Q9

#Part 1
number = input("Guess the lucky number ")
while number != 5:
   print ("That is not the lucky number")
   number = input("Guess the lucky number ")
    
    


# In[43]:


#Q9
#Part 2
   
number = -1
again = "yes"
while number != 5 and again != "no":
    number = input("Guess the lucky number: ")
    if number != 5:
        print( "That is not the lucky number")
        again = input("Would you like to guess again? ")


# In[45]:


#Q10

counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 5:
       print( "Try again.")
   else:
       print ("Good guess!")
   counter = counter +1
else:
   print ("Game over")


# In[47]:


#Q11

counter = 1
while counter <= 5:
   number = input("Guess the " + str(counter) + ". number ")
   if number != 5:
       print ("Try again.")
   else:
       print ("Good guess!")
       break
   counter = counter +1
else:
   print ("Sorry but that was not very successful")


# In[ ]:




