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
        date = item.find('em').text
        content = item.find('strong').text

        playerlist = ""
        players = item.select('span.tit_teaminfo')
        for player in players:
            temp = player.text
            playerlist = playerlist+" "+temp
        # print(playerlist)

        scheduleDict[count] = {"date": date, "content":content, "players":playerlist}
        # print(scheduleDict[count])
        count = count + 1

    # print(scheduleDict)

    return scheduleDict


testB = BeautifulSoup();
# testB.find_previous