#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import matplotlib as mpl
get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np

import folium 


get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


URL = "C:/Users/ahmed.antar/Downloads/Historical_Wildfires.csv"
path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
df = pd.read_csv(path)

print(df)


# In[18]:


#top five rows of data set
df.head()


# In[19]:


#column names
df.columns


# In[20]:


#data type
df.dtypes


# In[10]:


import datetime as dt

df['Year'] = pd.to_datetime(df['Date']).dt.year
df['Month'] = pd.to_datetime(df['Date']).dt.month


# In[11]:


#df.columns
df.dtypes


# In[26]:


df_line = df.groupby(df['Year'])['Automobile_Sales'].mean()
plt.figure(figsize=(10, 6))
df_line.plot(kind = 'line')
plt.xticks(list(range(1980,2024)), rotation = 75)
plt.xlabel('Year')
plt.ylabel('Sales Volume')
plt.title('Automobile Sales over Time')
plt.text(1982, 650, '1981-82 Recession')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




