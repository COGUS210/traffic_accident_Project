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
    rdr = csv.reader(file)

    # header를 제외한 데이터 lists에 저장
    for line in rdr:
        if headFlag is False:
            headFlag = True
            continue
        lists.append(line)
    lists.sort()

#사고종류
def typeAccident():
    dict = {}
    for line in lists:
        if dict.get(line[7]):
            dict[line[7]] += 1
        else:
            dict[line[7]] = 1
    del dict['기타']
    del dict['경보기무시']
    del dict['주/정차차량 충돌']
    del dict['차단기돌파']
    del dict['직전진행']
    del dict['후진중충돌']
    del dict['철길건널목']
    del dict['전복']

    return dict

def viz_pie_chart():
    data = typeAccident()

    x = []
    y = []
    for key in data:
        x.append(key)
        y.append(data[key])

    print(x)
    print(y)

    labels = x
    sizes = y
    color = ['#32327c', '#5c2d7a', '#992576', '#c01c74', '#e01073', '#c04483', '#954784', '#504887', '#204988', '#007ca5', '#3a85a6', '#8d92a6']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=color, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    # plt.title("Accident Ratios By Road type")
    plt.show()

lists = []
init()
viz_pie_chart()