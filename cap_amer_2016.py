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

    header = countryDataList[0]
    header2 = ['Country','Dist','ReleaseDate','OpeningWknd','PercentTotal','TotalGross','TotalGrossDate']
    data = countryDataList[3:]

    # this section will take the header of country information and then split
    # last element and update it and add it back to header
    total_gross = header[-1].split('/')[0].strip().replace(' ', '_')
    total_gross_as_of = total_gross + '_date'
    total_gross_as_of

    header.pop(-1)
    header.extend([total_gross, total_gross_as_of])

    df = pd.DataFrame(data)
    df.columns = header2
    fileToSaveAs = subUrl.split('=')[1].split('.')[0]+'.csv'
    df.to_csv(fileToSaveAs)
    #return df, fileToSaveAs

pullData('id=marvel2016.htm')



    

