from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pandas as pd
headers=[]
ward = ['Durham', 'Peterlee', 'Newton Aycliffe']

url = "https://dcsweb.durham.gov.uk/roadworks/roadworks-iframe.html"

page = urlopen(url)
html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

#print(html)

table_raw = soup.find("table")

#print(soup.get_text())
#print(soup.find_all("th"))

#Get the table headers:
th_table = soup.find_all("th")
for i in th_table:
  title = i.text
  headers.append(title)

#Create a dataframe:
#data = pd.DataFrame(columns = headers)
#
# Create a for loop to fill data
#for j in table_raw.find_all("tr")[1:]:
# row_data = j.find_all("td")
# row = [i.text for i in row_data]
# length = len(data)
# data.loc[length] = row
#
#print(data)
  
#Create a filtered dataframe:
data = pd.DataFrame(columns = headers)
# Create a for loop to fill data:
for j in table_raw.find_all("tr")[1:]:
 row_data = j.find_all("td")
 row = [i.text for i in row_data]
 length = len(data)
 data.loc[length] = row

#print(data)

data_location = data.Location.isin(ward)
data_location.shape
#data_location.Location.unique()
print(data_location)

data_combine1 = data[data_location]
print(data_combine1.head)