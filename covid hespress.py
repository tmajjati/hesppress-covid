#!/usr/bin/env python
# coding: utf-8

# In[372]:


import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


# In[373]:


page = requests.get("https://covid.hespress.com/")


# In[374]:


page.status_code


# In[375]:


page.content


# In[376]:



soup = BeautifulSoup(page.content, 'lxml')


# In[377]:


print(soup.prettify())


# In[378]:


table = soup.find('table', attrs={'class': 'table table-sm table-striped'})


# In[379]:


table


# In[380]:


rows = table.find_all("tr", attrs={"style": ""})
rows


# In[381]:


data = []
for i,item in enumerate(rows):
    data.append(item.text.strip().split("\n")[:3])
        


# In[382]:


data


# In[383]:



import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd


dt = pd.DataFrame(data)



# In[384]:


dt.head()


# In[385]:


dt.to_csv('../data hespress/datahess.csv')


# In[386]:


k=pd.read_csv('C:/Users/data hespress/datahess.csv')


# In[387]:


k


# In[ ]:





# In[ ]:




