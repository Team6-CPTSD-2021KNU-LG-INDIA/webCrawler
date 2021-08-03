import datetime
from bs4 import BeautifulSoup
from bs4.element import NavigableString, ResultSet
import requests
import json
from collections import OrderedDict

def scraping(soup):
    # 학사 일정의 각 일자
    eachContentsWithChild = soup.select('#calendar > dl > dd > ul > li')

    count = 1
    scheduleDict = {}

    for item in eachContentsWithChild:
        # 자식 태그 평문
        # print(item.next_element.text)
        now = datetime.datetime.now()

        date = str(now.year) + "-" + item.next_element.text[:-3].replace('.', '-')

        # 자식 태그의 제거
        item.next_element.extract()

        # 자식 태그를 제거한 결과의 평문만 가져와서 표시
        # print(item.text)

        title = item.text
        scheduleDict[count] = {"date": date, "title": title}
        count = count + 1

    return scheduleDict
