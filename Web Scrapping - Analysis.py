

# ### WebScrapping Phase

# Scrapping data from IMBD Movie rating

# In[21]:


# importing the required PKGS
from bs4 import BeautifulSoup
import requests, openpyxl


# ### Workbook Creation

# In[22]:


# creating excel workbook 
excel  = openpyxl.Workbook()
# assigning new variable woith the active sheet
sheet = excel.active
sheet.title = "Top Rated Movies"
# creating the excel header names
sheet.append(['Movie Rank', 'Movie Title', 'Year of Release', 'IMDB Rating'])


# In[23]:


# creating try excempt for the data scrap
try:
    source = requests.get('https://www.imdb.com/chart/top')
    # will use the raise _for_status_code
    source.raise_for_status()
    # creating the bs4 and passing the source as the responce object
    soup = BeautifulSoup(source.text,'html.parser')
    movies = soup.find('tbody',class_='lister-list').find_all('tr')
# oppenning a loop over
    for movie in movies:
        # fetch one movie at a time
        name = movie.find('td',class_='titleColumn').a.text
        rank = movie.find('td',class_='titleColumn').get_text(strip = True).split('.')[0]
        year = movie.find('td',class_='titleColumn').span.text.strip('()')
        rating = movie.find('td',class_='ratingColumn imdbRating').strong.text
#         print(name,rank,year,rating)
        sheet.append([rank,name,year,rating])
except Exception as e:
    print(e)
# saving the excel file
excel.save('IMDB_Movies.xlsx')


# In[24]:


get_ipython().system('dir')


# Now we have the data from scraped data

# ### Data Analysis Phase

# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('warnings.filterwarnings', '("ignore")')


# In[27]:


# Data loading from excel file
data = pd.read_excel("IMDB_Movies.xlsx")
data.head()


# ### Data Understanding

# In[28]:


# data size 
data.shape
# we have 4 columns by 250 records of data


# ### Data Summary Statistics

# In[29]:


data.describe()


# ### Data Info

# In[30]:


data.info()


# ### Tail

# In[31]:


data.tail()


# ### Data Cleaning

# In[32]:

# checking for missing values in the data
data.isna().sum()
# there are no missing values


# ### Data Assessment

# In[33]:


# pairplot from the data
data.sample(5)


# ### Data Analysis 

# **Analysis Questions**
# >What is the movie sale by title

# In[34]:


data.groupby(["Movie Title","IMDB Rating"])[['Movie Title',]].count()


# >What are the available movies 

# In[35]:


data['Movie Title'].nunique()
# there are 250 unique rcords of movie title


# In[36]:


data['IMDB Rating'].value_counts().plot(kind='bar')


# In[37]:


data['Movie Rank'].nunique()


# In[38]:


# data = data.set_index('Movie Rank')
data.groupby(['Year of Release'])[['Movie Title']].sum().head()


# In[39]:


data['Year of Release'].value_counts().head(20).plot(kind='bar')


# In[40]:


data.head()


# In[41]:


rating_title=data.sort_values('IMDB Rating',ascending=False)[['Movie Title','IMDB Rating']]
rating_title = rating_title.set_index('Movie Title')
rating_title.head(10).plot(kind='bar')


# ### List Rated Movies

# In[42]:


rating_title=data.sort_values('IMDB Rating',ascending=True)[['Movie Title','IMDB Rating']]
rating_title = rating_title.set_index('Movie Title')
rating_title


# In[43]:


data.head()


# In[44]:


data.groupby('Year of Release')[['Year of Release']].sum().head(20).plot(kind = 'bar')


# In[45]:


data.groupby('Year of Release')[['Year of Release']].sum().tail(20).plot(kind = 'bar')


# ### Release Year

# In[46]:


release = data['Year of Release'].describe()
release = pd.DataFrame(release)
release.T


# In[47]:


data['Year of Release'].plot(kind='hist')


# In[48]:


data.head()


# ### IMDB Rating

# In[49]:


# summary statistics
rating = data['IMDB Rating'].describe()
rating = pd.DataFrame(rating)
rating.describe().T


# In[50]:


data['IMDB Rating'].plot(kind = 'hist')


# In[51]:


data.head()
# 

