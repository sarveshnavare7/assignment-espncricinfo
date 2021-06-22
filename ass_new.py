import requests
import urllib.request

i=input("enter match id-")
url='https://www.espncricinfo.com/matches/engine/match/'+i+'.json'
# f=urllib.request.urlopen(url).read()
# print(f)
data=requests.get(url)
print(data.text)
print(url)

