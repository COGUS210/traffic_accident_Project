import numpy as np
import pandas as pd
import csv



list = []
region = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북',
          '경남', '제주']
#for i in range(2, 18):
#    for j in range(1, 48, 3):
regionNum = 0

for j in range(1, 48, 3):  #지역
    f = open('caraccidentdata.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    #for i in range(2, 18): #2002~2017년
    for line in rdr:
        list.clear()
        list.append(region[regionNum])
        list.append(line[0])
        list.append(line[j])
        list.append(line[j+1])
        list.append(line[j+2])
        data = np.reshape(list, (-1, 5))
        dataFrame = pd.DataFrame(data)
        dataFrame.to_csv("carAccident.csv", mode='a', index=False, header=False)
        print(list)
    regionNum = regionNum + 1
f.close()