# 1. 2023년 8월 한 달 동안의 연합뉴스의 2. 날짜, 타이틀, 기사 본문, 기사 반응, 카테고리 항목을  크롤링 하고 3. 기사 내용 전처리 진행한 후 4. news.csv 파일로 저장하는 코드 작성

# 2023년 8월 한 달 동안의 연합뉴스 크롤링
import requests
from bs4 import BeautifulSoup

h = {
    "Cookie":"JSESSIONID=F283F2C5A7F8C7A5E5F1F9A2DAE9FD24; NNB=EBHCWBDFIDSGI; isShownNewLnb=Y; nx_ssl=2"
    , "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

res = requests.get("https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=001", headers=h)
soup = BeautifulSoup(res.text, "html.parser")

oid = {
    "뉴스1":"421"
    , "뉴시스":"003"
    , "연합뉴스":"001"
    , "연합뉴스TV":"449"
    , "한국경제TV":"215"
    , "JTBC":"437"
    , "KBS":"056"
    , "MBC":"214"
    , "MBN":"057"
    , "SBS":"055"
    , "SBS Biz":"374"
    , "TV조선":"448"
    , "YTN":"052"
}

oid = oid["연합뉴스"]

year = "2023"
month = "08"
# for month in range(1, 13):
#     if month < 10:
#         month = "0" + str(month)
for day in range(1, 32):
    if day < 10:
        day = "0" + str(day )
    date = year + str(month) + str(day)

    print("date: ", date)

    page = 1
    while True:

        params = {
            "mode":"LPOD"
            , "mid":"sec"
            , "oid":oid
            , "date":date
            , "page":page
        }

        res = requests.get("https://news.naver.com/main/list.nhn?", params=params, headers=h)
        soup = BeautifulSoup(res.text, "html.parser")

        now_page = int(soup.select_one("div.paging strong").text)

        if page != now_page:
            break
        print("page: ", page)

        link_list = []
        for a in soup.select("dt a"):
            if not (a["href"] in link_list):
                link_list.append(a["href"])

        page += 1

