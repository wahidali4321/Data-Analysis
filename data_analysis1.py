#!/usr/bin/env python
# coding: utf-8

# # <center>Preprocessing 
# - anamellay
# - outliers
# - structure
# - data
#     

# ## import libraray

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ### data cleaning and exploring

# In[2]:


df = pd.read_csv('amazon.csv') # import csv file of amazon
print(df) # printing csv file


# In[3]:


#now we want to show just 10 first row
df.head(10)


# In[4]:


#set option to be maximum for rows and columns 
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


# In[5]:


df


# In[12]:


#hide all warning
import warnings
warnings.filterwarnings('ignore')


# ### now  we want to know how much columns

# In[13]:


df.columns


# In[15]:


# now we want to show that how much columsn and row
print("the number of rows is ",df.shape[0], 'the no of columns are ',df.shape[1])


# In[17]:


df.info()


# In[18]:


# now we want to show how much statistical data
df.describe()


# ## how to make size a numeric
# 

# In[24]:


# find out unique value
df['price'].head(20)


# In[27]:


# now to show the unique value 
df['price'].unique()


# ### observation
# - $ sign
# - 5 missing value

# In[32]:


# now to find out null value
df['price'].isnull().sum()


# In[35]:


# Assuming 'price' is not a numeric column
num_observations = df['price'].notna('$').sum()
print(f'Number of non-null observations in the "price" column: {num_observations}')


# In[36]:


# Assuming 'price' is not a numeric column
num_observations = (df['price'] != '$').sum()
print(f'Number of non-null observations in the "price" column (excluding "$"): {num_observations}')


# In[39]:


# Assuming 'price' is a column with strings containing dollar signs
df['price'] = df['price'].str.replace('$', '1')

# Convert the column to numeric if needed
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Display the DataFrame with the updated 'price' column
print(df)


# In[40]:


df['price'].info()


# In[41]:


df


# In[43]:


df.describe()


# In[ ]:




