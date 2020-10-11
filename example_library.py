import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)


response_data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716')

soup = BeautifulSoup(response_data.text, 'html.parser')
movies = soup.select("#old_content > table > tbody > tr")
for movie in movies:
    rank = movie.select_one("td.ac > img[alt]")
    title = movie.select_one("td.title > div > a")
    point = movie.select_one("td.point")
    if rank and title and point:
        print(f"{rank['alt']}위 : {title.text} / 별점 {point.text} ")


