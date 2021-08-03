import datetime
from bs4 import BeautifulSoup
from bs4.element import NavigableString, ResultSet
import requests
import json
from collections import OrderedDict

def scraping(soup):
    print("scraping....")
    wholeData = soup.select('#olympic-result-api > div.schedule_list > ol > li')

    # to count each schedules
    count = 1
    # to save each schedules and zip to dictionary
    scheduleDict = {}
    for item in wholeData:
        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")
        time = item.find('em').text
        title = item.find('strong').text

        contents = ""
        players = item.select('span.tit_teaminfo')
        for player in players:
            temp = player.text
            contents = contents+" "+temp
        # print(playerlist)

        scheduleDict[count] = {"date":date, "time": time, "title":title, "contents":contents}
        # print(scheduleDict[count])
        count = count + 1

    # print(scheduleDict)

    return scheduleDict


testB = BeautifulSoup();
# testB.find_previous