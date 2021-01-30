#!/usr/bin/env python
# coding: utf-8

# ## 11 대중교통 데이터 시각화하기

# ### (2) 지하철 유무임별 이용현황 데이터 정제하기

# In[1]:


# 콤마 제거
## row[4] = int(row[4].replace(',', ''))


# In[2]:


import csv
f = open('subwayfee.csv')
data = csv.reader(f)

for row in data :
    print(row)


# In[10]:


import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data) # 두 번째 줄부터 데이터를 다루기 위한 코드

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    print(row)


# ### (3) 유임 승차 비율이 가장 높은 역은 어디일까

# In[11]:


# 유임 승차 비율 rate를 계산하는 방법은 다양함
# 'rate = 유임승차인원 / 무임승차인원'을 사용할 예정임

# 알고리즘
# 1. 데이터를 읽어온다.
# 2. 모든 역의 데이터를 바탕으로 각 역의 rate를 계산한다.
# 3. 비율이 가장 높은 역을 찾는다.
# 4. 비율이 가장 높은 역은 어디인지, 그 비율이 얼마인지 출력한다.

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    rate = row[4] / row[6]
    if rate > mx :
        mx = rate
print(mx)

# division by zero 오류 발생


# In[13]:


for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] == 0 :
        print(row)
        
# row[6] 값이 0인 역이 존재


# In[15]:


import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 : # 만약 row[6](무임 승차 인원) 값이 0이 아니라면
        rate = row[4] / row[6]
        if rate > mx : # 만약 rate 값이 mx 값보다 크다면
            mx = rate # mx 값을 rate 값으로 업데이트
            print(row, round(rate, 2)) # 업데이트된 값 출력하기
            
# 충무로역의 데이터가 이상함
# 3호선 충무로역의 유임하차, 무임하차 값이 모두 0임
# 충무로역은 3호선과 4호선이 운행되는 환승역으로, 4호선 충무로역의 값과 함께 처리해야할 것임


# In[20]:


# 따라서 전체 인원 중 유임 승차 인원을 구하는 방법으로 데이터를 다뤄봄
# rate = 유임 승차 인원 / 전체(유임+무임) 인원

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4]+row[6]) > 10000: # 유무임 승차 인원을 합해서 100,000명 이상인 경우만 찾음
        rate = row[4] / (row[4] + row[6])
        if rate > mx :
            mx = rate
            print(row, round(rate, 2))
            
# 홍대입구역의 rate 가 0.95로 가장 높음
# 유임 승차 비율이 높은 역은 홍대입구역 하나일까?


# In[21]:


import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4]+row[6]) > 10000:
        rate = row[4] / (row[4] + row[6])
        if rate > 0.94 : # if 조건문 변경
            mx = rate
            print(row, round(rate, 2))
            
# 위와 다른 결과 도출


# #### 유임 승차 비율이 가장 높은 역 찾기

# In[23]:


import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx = 0
rate = 0
mx_station = ''

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4]+row[6]) > 10000:
        rate = row[4] / (row[4] + row[6])
        if rate > mx :
            mx = rate
            mx_station = row[3] + ' ' + row[1] # rate가 가장 높은 역 이름과 호선 저장
            
print(mx_station, round(mx*100,2))


# ### (4) 유무임 승하차 인원이 가장 많은 역은 어디일까

# In[25]:


import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx = [0] * 4
mx_station = [''] * 4

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > mx[i-4] :
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] + ' ' + row[1]

for i in range(4) :
    print(mx_station[i], mx[i])


# #### 유무임 승하차 인원이 가장 많은 역 찾기

# In[26]:


import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

mx = [0] * 4
mx_station = [''] * 4
label = ['유임승차', '무임승차', '유임하차', '무임하차']

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > mx[i-4] :
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] + ' ' + row[1]

for i in range(4) :
    print(label[i] + ' : ' + mx_station[i], mx[i])


# ### (5) 모든 역의 유무임 승하차 비율은 어떻게 될까

# In[27]:


import csv
import matplotlib.pyplot as plt

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

label = ['유임승차', '무임승차', '유임하차', '무임하차']

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.pie(row[4:8])
    plt.axis('equal')
    plt.show()


# In[29]:


import csv
import matplotlib.pyplot as plt

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

label = ['유임승차', '무임승차', '유임하차', '무임하차']

c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']

plt.rc('font', family = 'Malgun Gothic')

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3] + ' ' + row[1]) 
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
    plt.axis('equal')
    plt.show()


# #### 모든 역의 유무임 승하차 비율을 파이 차트로 나타내기

# In[ ]:


import csv
import matplotlib.pyplot as plt

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

label = ['유임승차', '무임승차', '유임하차', '무임하차']

c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']

plt.rc('font', family = 'Malgun Gothic')

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3] + ' ' + row[1]) 
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3] + ' ' + row[1] + '.png') # 파이 차트를 이미지 파일로 저장
    plt.show()

