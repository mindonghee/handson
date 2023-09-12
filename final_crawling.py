import requests
from bs4 import BeautifulSoup

from urllib.request import Request, urlopen
import csv, datetime


# 긍정 단어 리스트 정의
positive_words = ["최고", "획기적", "돌파", "급등", "상승", "흥행", "성공", "기록", "대박", "승리"]


current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"/home/ubuntu/1_dhmin/news/{current_time}_page3_positive.csv"

with open(filename, 'w', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'URL'])

    for i in range(1, 30, 10):
        req = Request(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B4%88%EC%A0%84%EB%8F%84%EC%B2%B4&start={i}', headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req).read()

        # 가져온 내용을 문자열로 디코딩
        html = response.decode('utf-8')
        #파싱
        soup = BeautifulSoup(html, 'html.parser')
        # 여러개의 태그 가져오기 -> list return
        links = soup.select(".news_tit")
        for link in links:
            # tag의 text 요소 가져오기
            title = link.text
            # href 속성 가져오기
            url = link.attrs['href']
            print(title, url)

            if any(word in title for word in positive_words):
                writer.writerow([title, url])
        