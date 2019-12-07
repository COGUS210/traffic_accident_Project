import csv
import operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family=font_name)


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


lists = []  # 차종별사고데이터
lists2 = []  # 차종별등록대수데이터

occur = []
die = []
init()
accident()
print(np.array(occur))
print("\n")
print(np.array(die))
