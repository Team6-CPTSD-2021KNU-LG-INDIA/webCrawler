from bs4 import BeautifulSoup
from bs4.element import NavigableString, ResultSet
from selenium import webdriver
import pandas as pd
import requests
import json
import time
from collections import OrderedDict
import importlib
from keywords import getKeyword

# function that returns keywords similar to the search term
knuSchedule = 'http://www.knu.ac.kr/wbbs/wbbs/user/yearSchedule/indexPopup.action?menu_idx=43'
olympicSchedule = 'https://focus.daum.net/ch/og2020/result'

# keyword 모듈에서 검색어와 가장 유사한 크롤링 리스트의 키워드를 반환 // 모듈
# 현재 test 목적으로 knu 학사일정 등록
def getNatualLanguage():
    return "경북대학교 일정을 찾아 주세요"

def matching(input):
    data = pd.read_csv('urlSet.csv', low_memory=False)
    index = list(data.loc[data['key']==input]['value'])

    return index[0]

# JSON 파일 생성. 추후 JSON 데이터를 서버에서 바로 전송할 예정
def toJson(resultSet):
    with open('savedJson.json', 'w', encoding='utf-8') as file:
        json.dump(resultSet, file, ensure_ascii=False, indent='\t')

# 동적 모듈 import. 다수의 커스텀 크롤링 모듈을 동적으로 import하기 위한 함수
def loadModule(module_name):
    module = importlib.import_module(module_name)
    return module


def Crawling(URL, keywords):
    # request를 이용한 html 문서 get. 동적으로 생성되는 data는 받아올수 없어 비활성화
    # source = requests.get(URL)

    #pandas의 따옴표 제거
    URL = URL[1:-1]

    # selenium 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('ignore-certificate-errors')
    chrome_options.add_argument("--headless")

    # Chrome driver setting
    PATH = '/mnt/c/Users/Home/Crawler/chromedriver'
    driver = webdriver.Chrome(PATH, options=chrome_options)
    driver.get(URL)
    time.sleep(1)


    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    
    print("toCrawl")
    crawledData = loadModule(keywords).scraping(soup)

    toJson(crawledData)


keywords = getKeyword(getNatualLanguage())
url = matching(keywords)
Crawling(url, keywords)