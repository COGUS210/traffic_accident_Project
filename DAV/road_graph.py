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
    file = open('accident_road.csv', encoding='utf-8')
    rdr = csv.reader(file)

    # header를 제외한 데이터 lists에 저장
    for line in rdr:
        if headFlag is False:
            headFlag = True
            continue
        lists.append(line)
    lists.sort()

def roadAccident():
    dict = {'일반국도': 0, '지방도': 0, '특별광역시도': 0, '시도': 0, '군도': 0,
            '고속국도': 0, '기타': 0}
    for line in lists:
        if line[1] == '발생건수':
            dict['일반국도'] += int(line[3])
            dict['지방도'] += int(line[4])
            dict['특별광역시도'] += int(line[5])
            dict['시도'] += int(line[6])
            dict['군도'] += int(line[7])
            dict['고속국도'] += int(line[8])
            dict['기타'] += int(line[9])
    return dict

def roadAccident2():
    dict = {'일반국도': 0, '지방도': 0, '특별광역시도': 0, '시도': 0, '군도': 0,
            '고속국도': 0, '기타': 0}
    for line in lists:
        if line[1] == '사망자수':
            dict['일반국도'] += int(line[3])
            dict['지방도'] += int(line[4])
            dict['특별광역시도'] += int(line[5])
            dict['시도'] += int(line[6])
            dict['군도'] += int(line[7])
            dict['고속국도'] += int(line[8])
            dict['기타'] += int(line[9])
    return dict

#발생건수
def viz_pie_chart():
    data = roadAccident()
    labels = '일반국도', '지방도', '특별광역시도', '시도', '군도', '고속국도'
    sizes = [data['일반국도'], data['지방도'], data['특별광역시도'], data['시도'],
             data['군도'], data['고속국도']]
    explode = (0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    #plt.title("Accident Ratios By Road type")
    plt.show()

#사망사고
def viz_pie_chart2():
    data = roadAccident2()
    labels = '일반국도', '지방도', '특별광역시도', '시도', '군도', '고속국도'
    sizes = [data['일반국도'], data['지방도'], data['특별광역시도'], data['시도'],
             data['군도'], data['고속국도']]
    explode = (0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    #plt.title("Accident Ratios By Road type")
    plt.show()


lists = []
init()
viz_pie_chart2()