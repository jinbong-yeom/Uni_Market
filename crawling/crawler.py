from bs4 import BeautifulSoup
import requests
import time

from crawler_class import Bunjang, Danngn, Joongna


region_keyword = "청주"
count = 0



while True:
    #당근마켓 검색
    danngn = Danngn()
    danngn.crawler_search(region_keyword)
    danngn.serve_data()
    print("당근")

    #번개장터 검색
    bunjang = Bunjang()
    bunjang.crawler_search()
    bunjang.serve_data()
    print("번개")

    #중고나라 검색
    joongna = Joongna()
    joongna.crawler_search()
    joongna.serve_data()
    print("중고나라")

    time.sleep(5)
    print(count)
    count += 1