from bs4 import BeautifulSoup 
import requests
import pandas as pd 
import csv
import os

#take user input url
url = input("Enter your url")

#connect the url with the script
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#extract the webtable from the web page
if url.find("en.wikipedia.org") == -1:
    congress_table = soup.find_all('table')   
else:
    congress_table = soup.find_all('table', {'class':'wikitable'or'wikitable sortable'}) 
df = pd.read_html(str(congress_table))

#print the extracted table
print(df)
dfout = pd.concat(df, ignore_index=True)

#let user select attributes
userSelectedAttributes = [str(x) for x in input("Enter selected attributes based on the table").split(',')]

#extract data based on input attributes
keep_col = userSelectedAttributes
new_f = dfout[keep_col]

#read saved tables
preTables = pd.read_csv("rawdata.csv")
preTables[userSelectedAttributes] = new_f

#save data into CSV
preTables.to_csv("rawdata.csv", index=False)