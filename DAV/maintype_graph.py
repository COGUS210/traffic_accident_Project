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
    file2 = open('accident_maintype.csv', encoding='utf-8')
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

#사고종류_발생건수
def maintypeAccident():
    dict = {}
    for line in lists:
        if dict.get(line[6]):
            dict[line[6]] += 1
        else:
            dict[line[6]] = 1
    del dict['건널목']
    del dict['철길건널목']
    return dict

#사고종류_사망사고
def maintypeAccident2():
    dict = {'차대차': 0, '차량단독': 0, '차대사람': 0}
    for line in lists2:
        if line[1] == '사망자수':
            dict['차대차'] += int(line[4])
            dict['차대사람'] += int(line[3])
            dict['차량단독'] += int(line[5])
    return dict

def viz_pie_chart():
    data = maintypeAccident()

    x = []
    y = []
    for key in data:
        x.append(key)
        y.append(data[key])

    labels = x
    sizes = y

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title("사고유형에 따른 교통사고 발생 비율")
    plt.show()

def viz_pie_chart2():
    data = maintypeAccident2()

    x = []
    y = []
    for key in data:
        x.append(key)
        y.append(data[key])

    labels = x
    sizes = y

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title("사고유형에 따른 사망 사고 발생 비율")
    plt.show()

lists = []
lists2 = []
init()
viz_pie_chart2()