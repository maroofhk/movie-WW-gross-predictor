import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup

import pandas as pd

def findRelevantData(tableElement):
    listOfTableData = tableElement.find_all('td')
    distributorText = listOfTableData[2].text.split(':')[1].strip()
    
    # convert to actual number
    prodBudget = listOfTableData[-1].text.split(':')[1].strip()
    mpaa_rating = listOfTableData[-2].text.split(':')[1].strip()
    
    # convert this to datetime
    releaseDate = listOfTableData[3].text.split(':')[1].strip()
    
    runTime = listOfTableData[-3].text.split(':')[1].strip()
    genre = listOfTableData[4].text.split(':')[1].strip()
    
    return distributorText, prodBudget, mpaa_rating, releaseDate, runTime, genre

def pullData(subUrl):

    url = 'http://www.boxofficemojo.com/movies/?page=intl&'+subUrl

    resp = requests.get(url)
    page = resp.text
    soup = BeautifulSoup(page)

    box = soup.find_all('table')

    topBox = box[4]
    countryData = box[7]

    countryDataList = []
    for row in countryData.find_all('tr'):

        rowData = []
        rowData = [x.text for x in row.find_all('td')]
        countryDataList.append(rowData)

    header2 = ['Country','Dist','ReleaseDate','OpeningWknd','PercentTotal','TotalGross','TotalGrossDate']
    data = countryDataList[3:]

    df = pd.DataFrame(data)
    df.columns = header2

    # Adding information from topbox of movie
    topBoxHeader = ['UsDist','UsRelease','Genre','Runtime','MpaaRating','ProdBudget']
    for element in zip(topBoxHeader, findRelevantData(topBox)):
        df[element[0]] = element[1]
    fileToSaveAs = subUrl.split('=')[1].split('.')[0]+'.csv'
    df.to_csv(fileToSaveAs, encoding='utf-8')
'''
ww2016 = pd.read_csv("worldwide_releases_2016_v2.csv")

linkList = []
for index, element in ww2016.iterrows():
    title = element.Movie_link.split('?')[1].split('.')[0]
    linkList.append(title)
    
for i in linkList:
    print(i)
'''
pullData('id=disney2016')






    

