import csv
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# 주간 야간 사고 횟수
def noonAndNight():
    # 주간 야간 dictionary에 저장
    dict = {'주간': 0, '야간': 0}
    for line in lists:
        if line[1] == '주':
            dict['주간'] += 1
        elif line[1] == '야':
            dict['야간'] += 1
        else:
            dict[line[1]] += 1

    return dict

def viz_pie_chart():
    data = noonAndNight()
    labels = 'Day Time', 'Night Time'
    sizes = [data['주간'], data['야간']]
    explode = (0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow = True, startangle = 90)
    ax1.axis('equal')
    plt.title("Day/Night Accident Ratios")
    plt.show()

lists = []
init()
viz_pie_chart()

