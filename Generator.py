import pandas as pd 
import csv
import os

#read saved tables
rawdataTables = pd.read_csv("rawdata.csv")

#print the saved table
print(rawdataTables)

#read all selected attributes
cols = str(pd.read_csv("rawdata.csv", nrows=0))

#ask user to select which attributes they want to keep and which they want to combine
combinecols = [str(x) for x in input("Enter attributes you want to combine").split(',')]

#combine cols
newcol = ['/'.join(i) for i in rawdataTables[combinecols].astype(str).values]

#generate output
outTable = rawdataTables.assign(CardDetail=newcol).drop(combinecols, 1)
outTable.to_csv("output.csv", index=False)