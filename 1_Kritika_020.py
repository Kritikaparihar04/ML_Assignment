#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Write a python program (menu driven) that asks for an operation to be performed on two input numbers. 
#Operations are add, subtract, divide, multiply. The program should keep asking for options on new numbers until the
#user specifies explicitly to exit. Also handle the scenario of divide by zero through exception handling in python.


# In[1]:


def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num2*num1
def div(num1,num2):
    try:
        print("The division of number is {}".format(num1/num2))
    except:
        print("oops cant divide by zero")


# In[2]:


print("Choose one of the mathematical operation(1/2/3/4)")
print("write 1 for addition")
print("write 2 for subtraction")
print("write 3 for multiplication")
print("write 4 for division")


# In[3]:


def main():
    op=input("enter the operation number")
    if op in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if op == '1':
            print("The sum is :",num1, "+", num2, "=", add(num1, num2))

        elif op == '2':
            print("The subtraction :",num1, "-", num2, "=", sub(num1, num2))

        elif op == '3':
            print("The multiplication is :",num1, "*", num2, "=", mul(num1, num2))

        elif op == '4':
             div(num1, num2)
    else:
        print("invalid operation number")
    choose=input("want to continue yes or no(y/n)")  
    if(choose=='y'):
        main()
    else:
        exit()

    
main()
   
    


# In[1]:


#2.Write a python program that takes a sentence as input from the user and reverses the words in the sentence. 
#Eg. If the sentence is 'Welcome to AI lab', then the output should be 'lab AI to Welcome'. 
#(Use list and string data structures)


# In[2]:


sent=input("Please enter the sentence")
word_list = sent.split()
reversed_list = word_list[:: -1]
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)


# In[ ]:





# In[3]:


#3.Write a python program that reads text from an input file (use your own input text file, it should contain at least 5-6
# small sentences) and counts the number of times each alphabet is appearing in it, and displays the frequency of #
#the occurrence of each alphabet. (Use dictionary data-structure to solve it)


# In[4]:


#Creating a new file
file=open("kritika.txt",'w')
file.write("heyaa I am Kritika Parihar n i am doing mca /m i lives in Chandigarh")
file.write(" i am doing mca ")
file.write(" i lives in Chandigarh")
file.write("I like to explore technical fields")
file.write("its my text file for testing the given program")
file.close()


# In[5]:


fname = input("Enter file name: ")
l=input("Enter letter to be searched:")
k = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
print("Occurrences of the letter:")
print(k)


# In[ ]:





# In[6]:


#4.Write a python program to find the square root of a given number (n) within a given precision (p). Do not use 
#any predefined library. (Take a guess, compute error at each successive step, until error is less than given precision)
# Example values of n are 10,15, 45, etc. Example values of p are 0.1, 0.05, 0.01, etc. [Hint: Find square root using binary
# search]


# In[7]:


def squareRoot(number, precision): 
  
    start = 0
    end,ans = number,1
  
    # For computing integral part 
    # of square root of number 
    while (start <= end) : 
        mid = int((start + end) / 2) 
          
        if (mid * mid == number) : 
            ans = mid 
            break
          
        # incrementing start if integral 
        # part lies on right side of the mid 
        if (mid * mid < number) : 
            start = mid + 1
              
          
        # decrementing end if integral part 
        # lies on the left side of the mid 
        else : 
            end = mid - 1
          
    # For computing the fractional part 
    # of square root upto given precision 
    increment = 0.1
    for i in range(0, precision):  
        while (ans * ans <= number): 
            ans += increment 
          
        # loop terminates when ans * ans > number 
        ans = ans - increment 
        increment = increment / 10
      
    return ans 
  
# Driver code 
print(round(squareRoot(40, 3), 4)) 
print(round(squareRoot(10, 4), 4)) 
     


# In[ ]:





# In[8]:


#5.Find the minimum value of a function y = (x+3)2. Write a python program to find the minimum value, use the 
# numerical method described in this link.


# In[9]:


def y(x):
    return((x+3)**2)

def dy(x):
    return(2*(x+3))

def minimum(n,x,alpha):
    while(n):
        ty = y(x)
        tdy = dy(x)
        x = x-(alpha*tdy)
        n-=1
    return(x)
for i in range(10,70,10):
    print(minimum(i,0,0.3))


# In[10]:


#6.Create a suitable class in python to represent the mathematical concept of 'vector' (use list data structure to represent 3
#vector). Create appropriate member variables and member functions of this class to perform operations: Length of vector, 
#Cosine similarity between two vectors, Euclidean distance between two vectors.


# In[11]:


import numpy as np
import math
class vectors():
    def __init__(self,x,y,z):
        self.vector = np.array([x,y,z])
    def length(self):
        temp = self.vector
        temp = np.square(temp)
        return(math.sqrt(sum(temp)))
    def distance(self,other):
        t = self.vector-other.vector
        t = np.square(t)
        return(math.sqrt(sum(t)))
    def cosine(self,other):
        t1 = self.vector
        t2 = other.vector
        product = sum(t1*t2)
        t1 = np.square(t1)
        ma = math.sqrt(sum(t1))
        t2 = other.vector
        t2 = np.square(t2)
        mb = math.sqrt(sum(t2))
        return(product/(ma*mb))
    
temp1 = vectors(2,3,4)
temp2 = vectors(4,5,6)
print(temp1.length())
print(temp1.distance(temp2))
print(temp1.cosine(temp2))


# In[ ]:





# In[ ]:




