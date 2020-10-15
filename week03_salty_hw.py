import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

lists = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for list in lists:
    rank = list.select_one('td.number').text[0:2].strip()
    title = list.select_one('td.info > a.title.ellipsis').text.strip()
    artist = list.select_one('td.info > a.artist.ellipsis').text.strip()
    print(rank, title, artist)
    doc = {
        'rank': rank,
        'title': title,
        'artist': artist  # DB에는 숫자처럼 생긴 문자열 형태로 저장됩니다.
    }
    db.musics.insert_one(doc)