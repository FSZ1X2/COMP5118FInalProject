from bs4 import BeautifulSoup 
import requests
import pandas as pd 
import csv
import os

#take user input url
wiki_url = input("Enter your url")

#connect the url with the script
response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')

#extract the webtable from the web page
congress_table = soup.find('table', {'class':'wikitable'or'wikitable sortable'}) 
df = pd.read_html(str(congress_table))

#print the extracted table
print(df)
dfout = pd.concat(df, ignore_index=True)

#let user select attributes
L = [str(x) for x in input("Enter selected attributes based on the table").split(',')]
#print("\nThe values of input are", L) 

#extract data based on input attributes
keep_col = L
new_f = dfout[keep_col]

#save data into CSV
new_f.to_csv("test.csv", index=False)