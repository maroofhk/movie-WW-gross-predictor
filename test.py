import pandas as pd
import time
import random

ww2016 = pd.read_csv("worldwide_releases_2016_v2.csv")
'''
for index, element in ww2016.iterrows():
    title = element.Movie_link.split('?')[1].split('.')[0]
    print(title)

'''
timer = random.randint(5,10)
time.sleep(timer)
print(timer)

