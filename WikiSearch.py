from bs4 import BeautifulSoup 
import requests
import pandas as pd 
import csv
import os
import wikipedia

#take user input kekword
userInput = input("Enter your keyword")

#print out related results
print(wikipedia.search(userInput))

#ask user to select what they aim to
keyword = input("Please select your main keyword")

#find the wiki page based on user input keyword
wiki_url = wikipedia.page(keyword).url

#connect the url with the script
response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

#extract the webtable from the web page
congress_table = soup.find_all('table', {'class':'wikitable'or'wikitable sortable'}) 
df = pd.read_html(str(congress_table))

#print the extracted table
print(df)
dfout = pd.concat(df, ignore_index=True)

#take user input attributes
userAttributes = [str(x) for x in input("Enter selected attributes based on the table").split(',')]

#extract data based on input attributes
keep_col = userAttributes
new_f = dfout[keep_col]

#save data into CSV
new_f.to_csv("rawdata.csv", index=False)