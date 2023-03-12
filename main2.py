# load pandas
import pandas as pd
from urllib.request import urlopen

url = "https://dcsweb.durham.gov.uk/roadworks/roadworks-iframe.html"

page = urlopen(url)

data_url = 'https://dcsweb.durham.gov.uk/roadworks/roadworks-iframe.html'
# read data from url as pandas dataframe
gapminder = page.read().decode("utf-8")

print(gapminder)

#is_ward1 =  gapminder['Location']==Peterlee
#print(is_ward1.head())
