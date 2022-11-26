import time

from crawler_class import Joongna


joongna = Joongna()
count = 0
while True:
    #중고나라 검색
    joongna.crawler_search()
    joongna.serve_data()
    print("중고나라")

    time.sleep(5)
    print(count)
    count += 1