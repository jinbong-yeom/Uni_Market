from bs4 import BeautifulSoup
import requests

from crawler_class import Bunjang, Danngn, Joongna


region_keyword = "청주"

#당근마켓 검색
danngn = Danngn()
danngn.crawler_search(region_keyword)
danngn.find_all()
danngn.serve_data()
print("당근")

#번개장터 검색
bunjang = Bunjang()
bunjang.crawler_search(search_word, sub_filter)
bunjang.find_all()
bunjang.serve_data()
print("번개")

#중고나라 검색
joongna = Joongna()
joongna.crawler_search(search_word, sub_filter)
joongna.find_all()
joongna.serve_data()
print("중고나라")