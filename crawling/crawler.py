from crawler_bunjang import start_bunjang
from crawler_daangn import start_daangn
from crawler_joongna import start_joongna
import argparse

BUNJANG = 1
DAANGN = 2
JOONGNA = 3

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", dest="type", action="store")
args = parser.parse_args()

type: int = args.type

if int(args.type) == BUNJANG:
    start_bunjang()
elif int(args.type) == DAANGN:
    start_daangn()
elif int(args.type) == JOONGNA:
    start_joongna()