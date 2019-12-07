import csv
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

def init():
    headFlag = False
    file = open('traffic_death.csv', encoding='utf-8')
    file2 = open('car_num.csv', encoding='utf-8')
    rdr = csv.reader(file)
    rdr2 = csv.reader(file2)

    # header를 제외한 데이터 lists에 저장
    for line in rdr:
        if headFlag is False:
            headFlag = True
            continue
        lists.append(line)
    lists.sort()

    for line in rdr2:
        if headFlag is False:
            headFlag = True
            continue
        lists2.append(line)
    lists2.sort()

#차량종류별
def cartypeAccident():


lists = []
lists2 = []
init()