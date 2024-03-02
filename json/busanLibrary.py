from urllib.request import Request, urlopen
from urllib.parse import quote # 글자를 유니코드(utf-8 ) 인코딩 함수
from urllib import parse
import json # 학습 필요
import datetime
import ssl
import requests

class BusanLibrary:
    def __init__(self) -> None:
        pass

    def getSearchResult(self,area):
        url = 'http://apis.data.go.kr/6260000/BusanLibraryInfoService/getLibraryInfo'
        params ={'serviceKey' : 'l2SER5UdFnVMTCfW/75Op1w1xj0ZVJyWjxZCA4s2qcMkJIjXonsQeorj8k35mmylOV0ywqc75RoXXtagwXuUnQ==', 'numOfRows' : '10', 'pageNo' : '1', 'resultType' : 'json','library_area' : {area}}

        response = requests.get(url, params=params)
        if response.status_code == 200: #나중에 처리할 것
            decodecontent = response.content.decode('utf-8')
            return json.loads(decodecontent)
        else:
            return None
        


