#!/usr/bin/env python
# coding: utf-8

# # Assignment 4

# # 1. Load the dataset and perform following pre-processing tasks: [4 pts]

# In[1]:


import pandas as pd #used to import dataset
import numpy as np #used for mathematical operations
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("C:/Users/Asus/Downloads/popularity.csv")
#it will read the data of datset 


# In[3]:


df


# # 1.1 Remove the first column of ‘Unnamed: 0

# In[4]:


del(df['Unnamed: 0'])


# In[5]:


df.head(30)


# # 1.2 Detect missing values, and replace them with the mean.
# 

# In[6]:


#  show the boolean dataframe     
df.isnull()


# In[7]:


# Count total missing value at each column in a DataFrame 
df.isnull().sum()


# In[8]:



df=df.fillna({'avg_shares':df['avg_shares'].mean(),'avg_comments':df['avg_comments'].mean()})
df.head(30)


# In[9]:


df.isnull().sum() #for checking is there any null value


# # 1.3 Draw box-plots for each attribute to detect if there are any outliers. If there are outliers, ignore them for now.
# 

# In[10]:


df.boxplot(column=["avg_shares","avg_comments","avg_expert","popularity_score"]) 
 


# # 1.4 Normalize all attributes within the range of 0 to 1.

# In[11]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
 
ndf=pd.DataFrame(scaler.fit_transform(df),
            columns=df.columns, index=df.index) 
ndf


# # Visualize through scatter plots the relationship of each attribute with the target attribute. [1pt]

# In[12]:


x=df['avg_shares']
#the target attribute is popularity score
y=df['popularity_score']
plt.scatter(x,y,c='yellow',s=60)


# In[13]:


x=df['avg_comments']
y=df['popularity_score']
plt.scatter(x,y)


# In[14]:


x=df['avg_expert']
y=df['popularity_score']
plt.scatter(x,y,c='red')


# # 3. Split the dataset into train and test, into 70% and 30% respectively. [1 pt]
# 

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


from sklearn.model_selection import train_test_split 


# In[17]:


train_data,test_data = train_test_split(df,test_size = 0.3,random_state=42)


# In[18]:


train_data


# In[19]:


test_data


# # 4. Train the linear regression model and print the coefficients (parameters) learned by the final model. [1 pt]

# In[20]:


x_train=train_data.iloc[:,:-1]
x_test=test_data.iloc[:,:-1]
y_train=train_data.iloc[:,:1]
y_test=test_data.iloc[:,:1]


# In[21]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)


# In[22]:


print(regressor.coef_)


# # 5. Print the confidence interval and p-value of each of the coefficients, and explain your interpretations. [1 pt]¶

# In[23]:


import statsmodels.api as sm 
model = sm.OLS(y_train, x_train).fit()
S_model = model.summary()
print(S_model)


# Interpretation for Confiedence Interval 
# Confiedence Interval of coefficient 1 i.e x1 is in the range [2.89e-17    5.43e-17]
# Confiedence Interval of coefficient 2 i.e x2 is in the range [1.000       1.000]
# Confiedence Interval of coefficient 3 i.e x3 is in the range [-9.57e-17    2.63e-17]


# Interpretation for p-value
# The p-value for each term tests the null hypothesis that the coefficient is equal to zero (no effect).
#A low p-value (< 0.05) indicates that you can reject the null hypothesis. 
#In other words, a predictor that has a low p-value is likely to be a meaningful addition to your model 
#because changes in the predictor's value are related to changes in the response variable.

#Conversely, a larger (insignificant) p-value suggests that changes in the predictor are not associated with changes
#in the response.

#In the output below, we can see that the predictor variables of x1 and x2 are significant
#because both of their p-values are 0.000. However, the p-value for x3 (0.263) is greater than the common alpha level of 0.05,
#which indicates that it is not statistically significant


# # 6. Evaluate the linear regression model and print the values of RMSE, MAE, and MSE.

# In[24]:


y_pred=regressor.predict(x_test)


# In[25]:


#Printing values of RMSE,MAE and MSE
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import math
print(mean_squared_error(y_test, y_pred))
print(math.sqrt(mean_squared_error(y_test, y_pred)))
print(mean_absolute_error(y_test, y_pred))


# # 7. Plot residual curve and Q-Q plot. [1 pt]

# In[26]:


# Residual is the difference between actual and predicted values of the target variable
residual = y_test - y_pred
residual


# In[27]:


# Creating residual plot with predicted value on x-axis and residual values on y-axis
import seaborn as sns
sns.residplot(x=y_pred,y=residual,data=df,color='green')
plt.show()


# In[28]:


# Q-Q plot of the target variable 
from scipy import stats
stats.probplot(df['popularity_score'], dist="norm", plot=plt)
plt.show()

