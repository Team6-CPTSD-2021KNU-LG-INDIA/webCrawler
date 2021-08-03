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

def matching(input):
    data = pd.read_csv('urlSet.csv', low_memory=False)
    index = list(data.loc[data['key']==input]['value'])

    return index[0]

# JSON 파일 생성. 추후 JSON 데이터를 서버에서 바로 전송할 예정
def toJson(resultSet):
    with open('savedJson.json', 'w', encoding='utf-8') as file:
        json.dump(resultSet, file, ensure_ascii=False, indent=4)
    file.close()
    return json.dumps(resultSet, ensure_ascii=False, indent=4)

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

    # Chrome driver setting(in my wsl)
    PATH = '/mnt/c/Users/Home/Crawler/chromedriver'
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    driver.get(URL)
    time.sleep(1)


    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    
    print("toCrawl")
    crawledData = loadModule(keywords).scraping(soup)

    return toJson(crawledData)

def scripts(NL):
    keywords = getKeyword(NL)
    url = matching(keywords)
    return Crawling(url, keywords)

print(scripts("vaccine"))