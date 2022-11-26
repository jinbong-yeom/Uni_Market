from bs4 import BeautifulSoup
import requests
import time

from crawler_class import Bunjang, Danngn, Joongna



bunjang = Bunjang()
joongna = Joongna()
count = 0
while True:


    #번개장터 검색
    bunjang.crawler_search()
    bunjang.serve_data()
    print("번개")

    #중고나라 검색
    joongna.crawler_search()
    joongna.serve_data()
    print("중고나라")

    time.sleep(5)
    print(count)
    count += 1