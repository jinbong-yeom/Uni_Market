from bs4 import BeautifulSoup
import requests
import datetime

from crawler_class import Bunjang, Danngn
from crawling.crawler_class import Joongna


#당근마켓 검색
danngn = Danngn()
danngn.crawler_search("노트북")
danngn.find_all()

#번개장터 검색
bunjang = Bunjang()
bunjang.crawler_search("노트북")
bunjang.find_all()

#중고나라 검색
joongna = Joongna()
joongna.crawler_data("노트북")
joongna.find_all()