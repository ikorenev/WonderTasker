

import json
from bs4 import BeautifulSoup
import requests



Tasker='https://4334-213-138-93-197.ngrok-free.app'
filteredNews = []
allNews = []
async def getTask():
    page=requests.get(Tasker)
    print(page.status_code)


    page = requests.get(Tasker)
    soup = BeautifulSoup(page.text, "html.parser")
    print(soup)

json