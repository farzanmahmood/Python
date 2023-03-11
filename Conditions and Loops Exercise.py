#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Q1 Given two integer numbers. If any of the numbers are greater than 50 return true

number1=20
number2=40

number1>50 or number2>50


# In[5]:


number1=20
number2=40

if (number1>50 or number2>50):
    print("One or both the numbers are greater than 50")
else:
    print("Neither number is greater than 50")


# In[6]:


#Q2 Given a list of numbers, return True if first and last number of a list is same?
#list=[1,2,5,4,1]

list1=[1,2,5,4,1]

list1[0] == list1[-1]


# In[29]:


#Q3 Given a range of the first 10 numbers[1:10], Iterate from the start number to
#and In each iteration print the sum of the current number and previous number

x=0

for i in range(1,11):
    sum = x + i
    print(sum)
    x = sum


    


# In[34]:


#Q4 Given a string name, display only those characters which are present at an even index?
name="NPowerCanada"
name[1::2]

#Leaving end index blank as that covers the whole string to the end


# In[48]:


#Q5 Given a string oldString and an integer number n,
#remove characters from a string starting from zero up to n and return a newStrin
# oldString="PythonCourse"
#n=6

oldString="PythonCourse"
n=6

for i in range(n+1):
    newString = oldString[i:]
    print(newString, "\n")
    
#Not sure if need 6 or 7 iterations here, I think 7


# In[56]:


#Q6 Print the follwoing pattern
#*
#**
#***
#****

for i in range(1,5):
    print("*"*i)


# In[68]:


for i in range(1,5):
    for j in range(i):
        print("*", end = "")
    print('\n')
    
#nested loop way of doing it


# In[93]:


#Q7 Reverse the following list using for loop
#list1=[90,70,50,60]

list1 = [90,70,50,60]
reverse_list1 = []

for i in range(len(list1)):
    reverse_list1.append(list1[-i - 1])
reverse_list1
    
#-i minus 1 because negative inedx gotta start at -1 not -0.


# In[94]:


digits = [1,4,7,8,3,6]
result = []

for i in digits:
    result = [i] + result 
    print(result)
# Here [i] is not index, rather it's the list element itself and it just keeps getting added to the front of the list every time so that it ends up being reverse.


# In[9]:


s=input("enter string: ")
print(s[::-1])


# In[101]:


#Q8 Display numbers from -10 to -1 using for loop [hint use range method]

for i in range(10):
    print(i - 10)

