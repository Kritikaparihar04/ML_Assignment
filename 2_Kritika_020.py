#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 2

# # 1. Load the csv file of the dataset into a dataframe in Python program.	

# In[1]:


import pandas as pd    #loading csv file using link
data=pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/us-weather-history/KCLT.csv")
data      


# In[ ]:





# # 2. Find the mean, median, mode, min and max for all numeric attributes.
# 

# In[2]:


# MEAN OF ALL THE ATTRIBUTES OF THE DATASET

data.mean(axis=0)    #axis=0 is used to print the mean of each column 


# In[3]:


#TO CALCULATE MODE 
data.mode()
    


# In[4]:


#MEDIAN OF EACH COLUMN

data.median()


# In[5]:


# MINIMUM
data.min()


# In[6]:


# MAXIMUM
data.max()


# In[ ]:





# # 3. Print the top 20% of rows showing only the first four columns.
# 

# In[7]:


x=data.head(int(len(data)*(20/100))) 
x                                     #it will print top 20% of rows


# In[8]:


#it will print top 20% rows showing only 4 columns
x.iloc[:,:4]          


# # 4 Create a new column (call it ‘newColumn’), it should have the same values as the column ‘actual_mean_temp’. 
# #Print head of dataframe.

# In[9]:


data['newColumn']=data['actual_mean_temp']  #assigning all the values of ‘actual_mean_temp’ to new column
data.head() 


# 
# 

# # 5. Remove the new column that you have created above. Print head of dataframe.

# In[10]:


data.pop('newColumn')  #pop is used to remove a column
data.head()


# In[ ]:





# # 6. Print the first 10 rows, then remove the row containing data of ‘2014-7-3’, save this row in a variable of type series (data structure). Print the first 10 rows after removal of row.

# In[11]:


f=data.head(10)  #it will print first 10 rows
f


# In[12]:


lf=f[f['date']=='2014-7-3']  #storing the row containing given date
lf


# In[13]:


#get the names of index for which col 
indexNames= data[data['date']=='2014-7-3'].index
#delete these row index from dataframe
data.drop(indexNames,inplace=True)


# In[14]:


data.head(10)        #Rows after removing the given row         


# # 7. Add the row that you deleted before. Print the first 10 rows again.
# 

# In[15]:


data=data.append(lf,ignore_index=True)     #it will add the removed row


# In[16]:


data.head(10)


# # 8. Update the actual_min_temp in the data row for date ‘2014-7-3’ to any value. Print the updated row.

# In[17]:


data.loc[data['date']=='2014-7-3','actual_min_temp']=55  #it will update the row 


# In[18]:


data[data['date']=='2014-7-3']


# In[ ]:





# # 9. Add 5 to the ‘actual_mean_temp’ wherever the ‘actual_min_temp’ is odd. Do this only on the top 10 rows. Print these 10 rows before and after the operation.

# In[19]:


print("10 Rows before the operation")  #before operation 
data.head(10)


# In[20]:


print("10 rows after the operation")         
 
for i in range(1,10):
    if(data.loc[i,'actual_min_temp']%2!=0):
        data.loc[i,'actual_mean_temp']+=5
data.head(10)
        


# In[ ]:





# # 10. Print only those rows where the absolute difference between the ‘record_min_temp_year’ and ‘record_max_temp_year’ is less than 30.
# 

# In[21]:


subset=data[abs(data['record_min_temp_year']-data['record_max_temp_year'])<30]  #storing the record in subset variable
subset 


# In[ ]:




