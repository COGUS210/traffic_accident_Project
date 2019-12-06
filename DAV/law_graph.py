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
    file = open('accident_Low.csv', encoding='utf-8')
    rdr = csv.reader(file)

    # header를 제외한 데이터 lists에 저장
    for line in rdr:
        if headFlag is False:
            headFlag = True
            continue
        lists.append(line)
    lists.sort()

#발생건수
def lawAccident():
    dict = {'중앙선침범': 0, '신호위반': 0, '안전거리미확보': 0, '불법유턴': 0, '과속': 0, '안전운전불이행': 0, '교차로운행방법위반': 0, '보행자보호의무위반': 0, '차로위반': 0, '직진우회전진행방해': 0}
    for line in lists:
        if line[1] == '발생건수':
            dict['중앙선침범'] += int(line[3])
            dict['신호위반'] += int(line[4])
            dict['안전거리미확보'] += int(line[5])
            dict['불법유턴'] += int(line[6])
            dict['과속'] += int(line[7])
            dict['안전운전불이행'] += int(line[8])
            dict['교차로운행방법위반'] += int(line[9])
            dict['보행자보호의무위반'] += int(line[10])
            dict['차로위반'] += int(line[11])
            dict['직진우회전진행방해'] += int(line[12])
    return dict

#사망사고
def lawAccident2():
    dict = {'중앙선침범': 0, '신호위반': 0, '안전거리미확보': 0, '불법유턴': 0, '과속': 0, '안전운전불이행': 0, '교차로운행방법위반': 0, '보행자보호의무위반': 0, '차로위반': 0, '직진우회전진행방해': 0}
    for line in lists:
        if line[1] == '사망자수':
            dict['중앙선침범'] += int(line[3])
            dict['신호위반'] += int(line[4])
            dict['안전거리미확보'] += int(line[5])
            dict['불법유턴'] += int(line[6])
            dict['과속'] += int(line[7])
            dict['안전운전불이행'] += int(line[8])
            dict['교차로운행방법위반'] += int(line[9])
            dict['보행자보호의무위반'] += int(line[10])
            dict['차로위반'] += int(line[11])
            dict['직진우회전진행방해'] += int(line[12])
    return dict

def viz_line_graph():
    lawDict = lawAccident()

    x = ['과속', '불법유턴', '차로위반', '직진우회전진행방해', '보행자보호의무위반', '교차로운행방법위반', '중앙선침범', '신호위반', '안전거리미확보', '안전운전불이행']
    y = []

    for key, value in lawDict.items():
        y.append(value)

    xt = []
    for i in range(10):
        xt.append(i)

    print(x)
    print(y)
    y.sort()
    print(y)

    plt.plot(xt, y, 'go-')
    plt.title("도로 종류에 따른 교통사고 발생건수")
    plt.xlabel("도로 종류")
    plt.ylabel("발생건수")
    plt.xticks(xt, x)
    plt.show()

def viz_line_graph2():
    lawDict = lawAccident2()

    x = ['차로위반', '불법유턴', '직진우회전진행방해', '안전거리미확보', '교차로운행방법위반', '과속', '보행자보호의무위반', '신호위반', '중앙선침범', '안전운전불이행']
    y = []

    for key, value in lawDict.items():
        y.append(value)

    xt = []
    for i in range(10):
        xt.append(i)

    print(x)
    print(y)
    y.sort()
    print(y)
    plt.plot(xt, y, 'ro-')
    plt.title("도로 종류에 따른 교통사고 사망사고")
    plt.xlabel("도로 종류")
    plt.ylabel("사망사고")
    plt.xticks(xt, x)
    plt.show()

lists = []
init()
viz_line_graph2()