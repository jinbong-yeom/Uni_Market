from crawler_class import *
from threading import Thread

import argparse
import time


DAANGN = 1
BUNJANG = 2
JOONGNA = 3
REGION = "청주"

def start(crawler_instance):

    while True:
        start = time.time()
        crawler_instance.crawler_search()
        crawler_instance.serve_data()
        print(time.time() - start)
        
        time.sleep(5)

    return

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", dest="type", action="store")
args = parser.parse_args()

type: int = args.type

crawler = None

if int(args.type) == DAANGN:
    crawler = Danngn()
elif int(args.type) == BUNJANG:
    crawler = Bunjang()
elif int(args.type) == JOONGNA:
    crawler = Joongna()
else:
    print("")

if crawler is not None:
    thread = Thread(target=start, args=(crawler, ), daemon=True)
    thread.start()

    while True:
        try:
            command = input()

            if command == 'q':
                break
        except KeyboardInterrupt as ki:
            pass
