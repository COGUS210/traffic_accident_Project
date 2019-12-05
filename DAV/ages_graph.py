import csv
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def init():
    headFlag = False
    file = open('accident_ages.csv', encoding='utf-8')
    rdr = csv.reader(file)

    # header를 제외한 데이터 lists에 저장
    for line in rdr:
        if headFlag is False:
            headFlag = True
            continue
        lists.append(line)
    lists.sort()

def agesAccident():
    dict = {10: 0, 20: 0, 30: 0, 40: 0, 50: 0, 60: 0}
    for line in lists:
        if line[1] == '발생건수':
            dict[10] += int(line[3])
            dict[20] += int(line[4])
            dict[30] += int(line[5])
            dict[40] += int(line[6])
            dict[50] += int(line[7])
            dict[60] += int(line[8])
            dict[60] += int(line[9])
    return dict

def viz_bar_graph():
    data = agesAccident()
    x = [10, 20, 30, 40, 50, 60]
    y = []
    for i in range(6):
        a = i + 1
        y.append(data[10*a])

    plt.bar(x, y, width=4, color='#456789')
    plt.title("Accident Numbers By Ages")
    plt.xlabel("Ages")
    plt.ylabel("Accident Numbers")
    plt.xticks(x, ['20-', 20, 30, 40, 50, '60+'])
    plt.show()

lists = []
init()
viz_bar_graph()