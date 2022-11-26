import time
from crawler_class import Danngn

def start_daangn():
    region_keyword = "청주"
    count = 0
    danngn = Danngn()

    while True:
        #당근마켓 검색
        danngn.crawler_search(region_keyword)
        danngn.serve_data()
        print("당근")
        
        count += 1
        time.sleep(5)