from urllib.request import Request, urlopen
from urllib.parse import quote  # 글자를 유니코드(utf-8) 인코딩 함수
import json
import datetime
import ssl
import requests
import matplotlib.pyplot as plt
from apscheduler.schedulers.blocking import BlockingScheduler



plt.rcParams['font.family'] = 'NanumGothicCoding'
plt.rcParams['axes.unicode_minus'] = False


class BusanWater:
    def __init__(self) -> None:
        pass

    def getSearchResult(self):
        url = 'http://apis.data.go.kr/6260000/BusanRvrwtLevelInfoService/getRvrwtLevelInfo'
        params = {'serviceKey': 'l2SER5UdFnVMTCfW/75Op1w1xj0ZVJyWjxZCA4s2qcMkJIjXonsQeorj8k35mmylOV0ywqc75RoXXtagwXuUnQ==',
                  'pageNo': '1', 'numOfRows': '18', 'resultType': 'json'}

        response = requests.get(url, params=params)
        if response.status_code == 200:
            decodecontent = response.content.decode('utf-8')
            return json.loads(decodecontent)
        else:
            return None


def update_chart():
    json_ob = busan.getSearchResult()
    body = json_ob['getRvrwtLevelInfo']['body']['items']['item']

    timestamps = []
    values = []

    for item in body:
        timestamp_str = item['tmEf']
        value = float(item['wf'])
        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
        timestamps.append(timestamp)
        values.append(value)

    ax.clear()
    ax.plot(timestamps, values, label='Water Level')
    ax.legend()
    ax.set_title('Busan Water Level')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Water Level (m)')

    plt.pause(0.1)


busan = BusanWater()

# 차트 초기화
fig, ax = plt.subplots()

# APScheduler를 사용하여 5분마다 업데이트
scheduler = BlockingScheduler()
scheduler.add_job(update_chart, 'interval', minutes=1)

try:
    scheduler.start()
except KeyboardInterrupt:
    pass
