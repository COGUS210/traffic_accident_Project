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

# 요일별 사고 비율
def weekAccident():
    weekTimeDict = {}
    for line in lists:
        if weekTimeDict.get(line[2]):
            weekTimeDict[line[2]] += 1
        else:
            weekTimeDict[line[2]] = 1

    weekTimeDict = sorted(weekTimeDict.items())

    return np.array(weekTimeDict)

def viz_bar_chart():
    weekTimeDict = weekAccident()
    x = []
    y = []
    week = []

    for i in range(7):
        y.append(int(weekTimeDict[i][1]))
        x.append(i + 1)
        week.append(weekTimeDict[i][0])

    y.sort()
    plt.bar(x, y, width=0.7, color='#456789')
    plt.title("Death Accidents By Day Of The Week")
    plt.xlabel("Day of the Week")
    plt.ylabel("Death Accidents")
    plt.xticks(x, ['Sun', 'Wed', 'Thu', 'Tue', 'Mon', 'Sat', 'Fri'])
    plt.ylim(3200, 4000)
    plt.show()

lists = []
init()
viz_bar_chart()