from urllib.request import Request, urlopen
from urllib.parse import quote # 글자를 유니코드(utf-8 ) 인코딩 함수
from urllib import parse
import json # 학습 필요
import datetime
import ssl

import requests

class BusanLibrary:
    def __init__(self) -> None:
        print('부산 도서관 검색 클래스 생성')

    def getSearchResult(self,area):
        url = 'http://apis.data.go.kr/6260000/BusanLibraryInfoService/getLibraryInfo'
        params ={'serviceKey' : 'l2SER5UdFnVMTCfW/75Op1w1xj0ZVJyWjxZCA4s2qcMkJIjXonsQeorj8k35mmylOV0ywqc75RoXXtagwXuUnQ==', 'numOfRows' : '10', 'pageNo' : '1', 'resultType' : 'json','library_area' : {area}}

        response = requests.get(url, params=params)
        decodecontent = response.content.decode('utf-8')

        return json.loads(decodecontent)
        


