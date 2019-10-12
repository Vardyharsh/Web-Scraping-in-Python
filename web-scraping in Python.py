#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import the library to query a website
import requests
#Specify the url which to scrape

w_link = "https://en.wikipedia.org/wiki/List_of_European_countries_by_area"
link = requests.get(w_link).text


# In[8]:


from bs4 import BeautifulSoup
#Parse the variable in HTML format into Beautifulsoup format.
soup = BeautifulSoup(link, 'lxml')

print(soup.prettify()) #helps in viewing nested structure of html page.


# In[10]:


soup.title.string  #gives the title of html page.


# In[11]:


soup.find_all('a') #finds all hyperlink in the given html page.


# In[12]:


#just extracting href value i.e link present in html page.
v_link = soup.find_all('a')
for link in v_link:
    print(link.get('href'))


# In[13]:


#prints all tables in html web page.
all_tables = soup.find('table')
print(all_tables)


# In[15]:


#finding right table using class variable in Inspector window.
r_table = soup.find('table', class_='wikitable sortable')
r_table


# In[18]:


t_links = r_table.find_all('a')
t_links


# In[19]:


#getting name of all countries in a list.
country = []
for link in t_links:
    country.append(link.get('title'))  #appending name of country 
    
print(country)


# In[25]:


#Creating a pandas DataFrame from scraped list of values.
import pandas as pd 
df = pd.DataFrame(country)
df

