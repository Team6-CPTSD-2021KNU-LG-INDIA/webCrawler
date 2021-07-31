from bs4 import BeautifulSoup
from bs4.element import NavigableString, ResultSet
import requests
import json
from collections import OrderedDict

def scraping(soup):
    print("scraping....")
    wholeData = soup.select('#content > div > div > div > table:nth-child(8) > tbody > td')
    # print(wholeData)
    # to count each schedules
    count = 1
    # to save each schedules and zip to dictionary
    scheduleDict = {}

    for item in wholeData:
        who = item.find('td').text
        how = item.findNext('td').text
        vaccine = item.find('td').text
        scale = item.find('td').text
        date = item.find('td').text
        print(who)
        scheduleDict[count] = {"who": who, "how":how, "vaccine":vaccine, "scale":scale, "date":date}
        # print(scheduleDict[count])
        count = count + 1

    # print(scheduleDict)

    return scheduleDict


testB = BeautifulSoup();
# testB.find_previous