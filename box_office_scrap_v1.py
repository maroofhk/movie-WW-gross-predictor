import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

urlWwGross2016 = 'http://www.boxofficemojo.com/yearly/chart/?view2=worldwide&yr=2016&p=.htm'
responsewwGross2016 = requests.get(urlWwGross2016)

#first use of Beatiful soup
pageWwGross2016 = responsewwGross2016.text
soupWwGross2016 = BeautifulSoup(pageWwGross2016)

tableWwGross2016 = soupWwGross2016.find_all('table')

dataJumble = tableWwGross2016[3].find_all('tr')
    
print(dataJumble[0].text)


#header = ['Rank', 'Title', 'Worldwide_percentage','Overseas_percentage']

