from bs4 import BeautifulSoup
import requests
import datetime

from crawler_class import Bunjang, Danngn, Joongna


#당근마켓 검색
danngn = Danngn()
danngn.crawler_search("노트북")
danngn.serve_data()

#번개장터 검색
bunjang = Bunjang()
bunjang.crawler_search("노트북")
bunjang.serve_data()

#중고나라 검색
joongna = Joongna()
joongna.crawler_search("노트북")
joongna.serve_data()