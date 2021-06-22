from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import requests
from datetime import datetime

i=input("Enter match id:-")
browser = webdriver.Chrome(executable_path=r'C:\Program Files\webdriver\chromedriver.exe')
browser.get('https://www.espncricinfo.com/matches/engine/match/'+i+'.json')
browser.maximize_window()
source = browser.page_source
data=bs(source, 'html.parser')
body = data.find('body')
pre = body.find('pre')
# url='https://www.espncricinfo.com/matches/engine/match/'+i+'.json'
# content=requests.get(url)
# soup=bs(content.text,"html.parser")
#print(soup)
# u=urlopen(url)
# page=u.read()
#page_soup=bs(page,"html.parser")
#print(page_soup)

#dataframe
result=pd.DataFrame(columns=['match_id','Date','ground_id','home_team_id','home_team_name','away_team_id','away_team_name','player_name','player_id','team_id','bowling_style','batting_style'])
data_json=json.loads(pre.text)
print(data_json)
match_id=i
#Date=

#site_json=json.loads(soup.text)
# all_divs = str(soup.find('pre'))
# data = all_divs[59:-6]
# data_json = json.loads(data)
#print(data_json)
#print(site_json)