from bs4 import BeautifulSoup
from bs4.element import NavigableString, ResultSet
import requests
import json
from collections import OrderedDict
import importlib

knuSchedule = 'http://www.knu.ac.kr/wbbs/wbbs/user/yearSchedule/indexPopup.action?menu_idx=43'

# keyword 모듈에서 검색어와 가장 유사한 크롤링 리스트의 키워드를 반환 // 모듈
# 현재 test 목적으로 knu 학사일정 등록
def getKeyword():
    return "knu"

# JSON 파일 생성. 추후 JSON 데이터를 서버에서 바로 전송할 예정
def toJson(resultSet):
    with open('savedJson.json', 'w', encoding='utf-8') as file:
        json.dump(resultSet, file, ensure_ascii=False, indent='\t')

# 동적 모듈 import. 다수의 커스텀 크롤링 모듈을 동적으로 import하기 위한 함수
def loadModule(module_name):
    module = importlib.import_module(module_name)
    return module


def Crawling(URL):
    source = requests.get(URL)
    if source.status_code == 200:
        soup = BeautifulSoup(source.text, 'html.parser')

        # 학사 일정의 각 일자
        
        crawledData = loadModule(getKeyword()).scraping(soup)

        toJson(crawledData)

    else:
        print(source.status_code + " Bad request!")


Crawling(knuSchedule)