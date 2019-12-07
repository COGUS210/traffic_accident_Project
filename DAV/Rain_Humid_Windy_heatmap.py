import csv
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 파싱
def init():
    headFlag = False
    file1 = open('weatherdata.csv', mode='r', encoding='utf-8-sig')
    file2 = open('carAccident.csv', mode='r', encoding='utf-8-sig')
    lists1 = []
    lists2 = []
    rdr1 = csv.reader(file1)
    rdr2 = csv.reader(file2)

    # header를 제외한 데이터 lists에 저장
    for line in rdr1:
        if headFlag is False:
            headFlag = True
            continue
        if line[0] == '105':
            line[0] = '강원'
        elif line[0] == '108':
            line[0] = '서울'
        elif line[0] == '112':
            line[0] = '인천'
        elif line[0] == '119':
            line[0] = '경기'
        elif line[0] == '131':
            line[0] = '충북'
        elif line[0] == '133':
            line[0] = '대전'
        elif line[0] == '143':
            line[0] = '대구'
        elif line[0] == '146':
            line[0] = '전남'
        elif line[0] == '152':
            line[0] = '울산'
        elif line[0] == '156':
            line[0] = '광주'
        elif line[0] == '159':
            line[0] = '부산'
        elif line[0] == '162':
            line[0] = '경남'
        elif line[0] == '168':
            line[0] = '전남'
        elif line[0] == '184':
            line[0] = '제주'
        elif line[0] == '232':
            line[0] = '충남'
        elif line[0] == '273':
            line[0] = '경북'
        lists1.append(line)
    rst1 = sorted(lists1, key=lambda x: (x[0]))

    for line in rdr2:
        lists2.append(line)
    rst2 = sorted(lists2, key=lambda x: (x[0], x[1]))


    for line1, line2 in zip(rst1, rst2):
        try:
            floatTmp1 = line1[3].split(',')
            floatTmp2 = line1[4].split(',')
            if len(floatTmp1) == 1:
                floatVal1 = float(floatTmp1[0])
            else:
                floatVal1 = float(floatTmp1[0]) + float(float(floatTmp1[1]) / 10)

            if len(floatTmp2) == 1:
                floatVal2 = float(floatTmp2[0])
            else:
                floatVal2 = float(floatTmp2[0]) + float(float(floatTmp2[1]) / 10)

            datas.append([int(line2[2]), int(line2[3]), int(line2[4]), floatVal2, floatVal1])
        except:
            print(line2[3])

    # for line in datas:
    #   print(line)

def heatMap():
    plt.figure(figsize=(5,5))
    data = pd.DataFrame(datas)
    print(data)
    sns.heatmap(data=data.corr(), annot=True, linewidths=.5, cmap='Blues')
    plt.show()
datas = []
init()
heatMap()