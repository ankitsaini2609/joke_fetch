from bs4 import BeautifulSoup
import requests
from time import sleep
import json
from random import randint
pnum = randint(1,11)
url = ("http://123hindijokes.com/very-funny-jokes/"+str(pnum))

source = requests.get(url)
jokes = {}
soup = BeautifulSoup(source.content,'lxml')
joke = soup.find_all('ul', attrs={'class':'statusList'})
for i in joke:
    j = i.find_all('li')
    for k in j:
        jokes[1] = k.get_text()

with open("jokes_output.json","w") as file:
    json.dump(jokes,file,ensure_ascii=False,indent=4)
    sleep(3)
