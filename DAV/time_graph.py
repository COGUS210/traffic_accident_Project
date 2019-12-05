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

# 시간대별 사고
def timeAccident():
    timeDict = {}
    for line in lists:
        time = str(str(line[0]).partition(' ')[-1]).partition(':')[0]
        if timeDict.get(int(time)):
            timeDict[int(time)] += 1
        else:
            timeDict[int(time)] = 1
    timeDict = sorted(timeDict.items())

    return np.array(timeDict)

def viz_bar_chart():
    timeDict = timeAccident()

    x = []
    y = []
    for i in range(24):
        y.append(timeDict[i][1])
        x.append(timeDict[i][0])

    plt.bar(x, y, width=0.7, color='#456789')
    plt.title("Death Ratios By Time")
    plt.xlabel("Time")
    plt.ylabel("Death Ratios")
    plt.xticks(x)
    plt.show()

lists = []
init()
viz_bar_chart()