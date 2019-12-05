import csv
import operator
import pandas as pd
import numpy as np


# 데이터 파
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

    print(dict)


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
    print(np.array(timeDict))


# 요일별 사고 비율
def weekAccident():
    weekTimeDict = {}
    for line in lists:
        if weekTimeDict.get(line[2]):
            weekTimeDict[line[2]] += 1
        else:
            weekTimeDict[line[2]] = 1

    print(weekTimeDict)


lists = []
init()
weekAccident()
# timeAccident()
# noonAndNight()
