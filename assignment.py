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

k=0
d=0
i=input("Enter match id:-")
browser = webdriver.Chrome(executable_path=r'C:\Program Files\webdriver\chromedriver.exe')
browser.get('https://www.espncricinfo.com/matches/engine/match/'+i+'.json')
browser.maximize_window()
source = browser.page_source
data=bs(source, 'html.parser')
body = data.find('body')
pre = body.find('pre')


#dataframe
result=pd.DataFrame(columns=['match_id','Date','ground_id','home_team_id','home_team_name','away_team_id','away_team_name','player_name','player_id','team_id','bowling_style','batting_style'])
data_json=json.loads(pre.text)

while(k<2):
    j=0
    while(j<11):
        match_id=i
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
result.to_csv(r'D:\assignment\ass1.csv')
print(result)
#print(data_json['team'][k]['player'][k]['known_as'])
