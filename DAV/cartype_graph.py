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
    file = open('accident_cartype.csv', encoding='utf-8')
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


def accident():
    for line1 in lists:  # lists : accident, lists2 : car_num
        if line1[1] == '발생건수' or line1[1] == '사망자수':
            for line2 in lists2:
                if line1[0] == line2[0] and line1[1] == '발생건수':
                    occur.append(
                        [round(float(line1[3]) / float(line2[1]), 4), round(float(line1[4]) / float(line2[2]), 4),
                         round(float(line1[5]) / float(line2[3]), 4), round(float(line1[6]) / float(line2[4]), 4),
                         round(float(line1[7]) / float(line2[5]), 4)])
                if line1[0] == line2[0] and line1[1] == '사망자수':
                    die.append(
                        [round(float(line1[3]) / float(line2[1]), 7), round(float(line1[4]) / float(line2[2]), 7),
                         round(float(line1[5]) / float(line2[3]), 7), round(float(line1[6]) / float(line2[4]), 7),
                         round(float(line1[7]) / float(line2[5]), 7)])

    data1 = 0
    data2 = 0
    for i in range(5):
        for j in range(10):
            data1 += occur[j][i]
            data2 += die[j][i]
        y1.append(round(data1, 3))
        y2.append(round(data2, 5) * 100)

#발생건수
def viz_pie_chart():
    x = ['승용차', '승합차', '화물차', '특수차', '이륜차']
    labels = x
    sizes = y1

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title("차종별 교통사고 발생 비율")
    plt.show()

#사망사고
def viz_pie_chart2():
    x = ['승용차', '승합차', '화물차', '특수차', '이륜차']
    labels = x
    sizes = y2

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.title("차종별 사망사고 발생 비율")
    plt.show()

lists = []  # 차종별사고데이터
lists2 = []  # 차종별등록대수데이터

occur = []
die = []
y1 = []
y2 = []
init()
accident()
viz_pie_chart2()
print(np.array(occur))
print(y1)
print("\n")
print(np.array(die))
print(y2)
