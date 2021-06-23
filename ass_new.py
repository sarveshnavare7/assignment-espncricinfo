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

i=0 #used for getting matchids
d=0 #csv index
l=[]#list of match ids
url=input("Enter url:-")
browser = webdriver.Chrome(executable_path=r'C:\Program Files\webdriver\chromedriver.exe')
browser.get(url)
browser.maximize_window()
source = browser.page_source
data=bs(source, 'html.parser')
body = data.find('body')
script = body.find('script', {"id":"__NEXT_DATA__"})
y=""
for z in script:
    y=y+z
#print(y)
data_json=json.loads(y)
#print(data_json)
while(i>=0):
    try:
        #print(data_json["props"]["pageProps"]["data"]["pageData"]["content"]["matches"][i]['objectId'])
        l.append(data_json["props"]["pageProps"]["data"]["pageData"]["content"]["matches"][i]['objectId'])
        i=i+1
    except:
        break
print(l)

result=pd.DataFrame(columns=['match_id','Date','ground_id','home_team_id','home_team_name','away_team_id','away_team_name','player_name','player_id','team_id','bowling_style','batting_style'])
for id in l:
    driver = webdriver.Chrome(executable_path=r'C:\Program Files\webdriver\chromedriver.exe')
    driver.get('https://www.espncricinfo.com/matches/engine/match/'+str(id)+'.json')
    driver.maximize_window()
    msource = driver.page_source
    mdata=bs(msource, 'html.parser')
    mbody = mdata.find('body')
    mpre = mbody.find('pre')
    data_json=json.loads(mpre.text)
    driver.close()
    k=0
    while(k<2):
        j=0
        while(j<11):
            match_id=id
            Date=data_json['match']['start_date_raw']
            #print(data_json['team'])
            ground_id=data_json['match']['ground_id']
            home_team_id=data_json['match']['home_team_id']
            home_team_name=(data_json['match']['team1_name']) if k is 0 else (data_json['match']['team2_name'])
            away_team_id=data_json['match']['away_team_id']
            away_team_name=(data_json['match']['team2_name']) if k is 0 else (data_json['match']['team1_name'])
            player_name=data_json['team'][k]['player'][j]['known_as']
            player_id=data_json['team'][k]['player'][j]['object_id']
            team_id=data_json['team'][k]['team_id']
            bowling_style=data_json['team'][k]['player'][j]['bowling_style']
            batting_style=data_json['team'][k]['player'][j]['batting_style']
            result.loc[d] = [match_id,Date,ground_id,home_team_id,home_team_name,away_team_id,away_team_name,player_name,player_id,team_id,bowling_style,batting_style]
            j+=1
            d=d+1
        k=k+1
print(result)
result.to_csv(r'D:\assignment\ass2.csv')
#print(data_json['team'][k]['player'][k]['known_as'])
