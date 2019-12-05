import csv
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def init():
    headFlag = False
    file = open('accident_gender.csv', encoding='utf-8')
    rdr = csv.reader(file)

    # header를 제외한 데이터 lists에 저장
    for line in rdr:
        if headFlag is False:
            headFlag = True
            continue
        lists.append(line)
    lists.sort()

# 가해운전자 성별 사고 비율
def genderAccident():
    dict = {'남': 0, '여': 0}
    for line in lists:
        if line[1] == '발생건수':
            dict['남'] += int(int(line[3])/77000)
            dict['여'] += int(int(line[4])/33000)
    return dict

def viz_pie_chart():
    data = genderAccident()
    labels = 'Men', 'Women'
    sizes = [data['남'], data['여']]
    explode = (0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title("Accident Ratios By Gender")
    plt.show()

lists = []
init()
viz_pie_chart()