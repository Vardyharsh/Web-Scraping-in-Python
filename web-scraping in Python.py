#!/usr/bin/env python
# coding: utf-8

#import the library to query a website
import requests
#Specify the url which to scrape

w_link = "https://en.wikipedia.org/wiki/List_of_European_countries_by_area"
link = requests.get(w_link).text


from bs4 import BeautifulSoup
#Parse the variable in HTML format into Beautifulsoup format.
soup = BeautifulSoup(link, 'lxml')

print(soup.prettify()) #helps in viewing nested structure of html page.



soup.title.string  #gives the title of html page.


soup.find_all('a') #finds all hyperlink in the given html page.


#just extracting href value i.e link present in html page.
v_link = soup.find_all('a')
for link in v_link:
    print(link.get('href'))



#prints all tables in html web page.
all_tables = soup.find('table')
print(all_tables)




#finding right table using class variable in Inspector window.
r_table = soup.find('table', class_='wikitable sortable')
r_table


t_links = r_table.find_all('a')
t_links



#getting name of all countries in a list.
country = []
for link in t_links:
    country.append(link.get('title'))  #appending name of country 
    
print(country)


#Creating a pandas DataFrame from scraped list of values.
import pandas as pd 
df = pd.DataFrame(country)
df

