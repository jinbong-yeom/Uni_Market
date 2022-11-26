from crawler_class import Bunjang
import time

bunjang = Bunjang()

count = 0
while True:

    #번개장터 검색
    bunjang.crawler_search()
    bunjang.serve_data()
    print("번개")

    time.sleep(5)
    count += 1