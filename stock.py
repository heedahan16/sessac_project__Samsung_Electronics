# 8월 한 달 간 삼성전자 주가 크롤링하여 stock.csv 파일로 저장

import requests
from bs4 import BeautifulSoup
import csv

f = open("stock.csv", mode="w", encoding="utf-8", newline="")
w = csv.writer(f)
w.writerow(["날짜", "종가", "전일비", "시가", "고가", "저가", "거래량"])

res = requests.get("https://finance.naver.com/item/sise.nhn?code=005930")
soup = BeautifulSoup(res.text, "html.parser")

code = soup.select("iframe")[-1]["src"].split("=")[1]

print("날짜, 종가, 전일비, 시가, 고가, 저가, 거래량")

for page in range(3, 6):

    h = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    params = {
        "code":code
        , "page":page
    }
    res = requests.get("https://finance.naver.com/item/sise_day.naver", params=params, headers=h)
    soup = BeautifulSoup(res.text, "html.parser")

    for tr in soup.select("table.type2 tr"):
        if tr.select("span") != [] and tr.select("span")[0].text[:-3] == "2023.08":
            date = tr.select("span")[0].text
            close = tr.select("span")[1].text
            diff = tr.select("span")[2].text.replace("\n", "").strip()
            open = tr.select("span")[3].text
            high= tr.select("span")[4].text
            low = tr.select("span")[5].text
            volume = tr.select("span")[6].text

            print(date, close, diff, open, high, low, volume)

            w.writerow([date, close, diff, open, high, low, volume])

f.close()
