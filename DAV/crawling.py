import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

regionList = [['강원', '01150'], ['경기', '02135'], ['경남', '03123'], ['경북', '04280'], ['광주', '05200'], ['대구', '06110'],
              ['대전', '07230'], ['부산', '08230'], ['서울', '09440'], ['세종', '17110'], ['울산', '10110'], ['인천', '11237'],
              ['전남', '12780'], ['전북', '13113'], ['제주', '14110'], ['충남', '15131'], ['충북', '16111']]

for region in regionList:
    for date in range(200201, 201713):
        if date % 100 > 0 and date % 100 < 13:
            response = requests.get("https://weather.naver.com/period/pastWetrMain.nhn?ym=" + str(date) + "&naverRgnCd=" + region[1])
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            listm = soup.find_all('td')
            for td in listm:
                cnt = 0
                img = td.find('img')
                temp = td.find_all('strong')

                for strong in temp:
                    cnt = cnt + 1
                if img is not None:
                    cnt = cnt + 1
                if cnt == 1:
                    break

                list = []

                if cnt == 4:
                    list.append(region[0])  #지역

                day = 0;
                for strong in temp:
                    if day == 0:
                        if int(strong.text.strip()) < 10:
                            list.append(str(date) + "0" + strong.text.strip())
                        else:
                            list.append(str(date) + strong.text.strip())
                        day = day + 1;
                    else:
                        list.append(strong.text.strip())    #일, 최저, 최고 기온
                    cnt = cnt + 1

                if img is not None:
                    list.append(img['alt'])   #날씨 상
                    cnt = cnt + 1

                if list:
                    print (list)
                    # csv파일에 저장
                    data = np.reshape(list, (-1, 5))
                    dataFrame = pd.DataFrame(data)
                    dataFrame.to_csv("data.csv", mode='a', index=False, header=False)
