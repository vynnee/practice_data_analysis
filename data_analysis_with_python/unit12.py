#!/usr/bin/env python
# coding: utf-8

# ## 12 지하철 시간대별 데이터 시각화하기

# ### (1) 지하철 시간대별 이용 현황 데이터 정제하기

# In[1]:


import csv
f = open('subwaytime.csv')
data = csv.reader(f)
for row in data :
    print(row)


# In[1]:


import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
for row in data :
    row[4:] = map(int, row[4:]) # map() 함수는 일괄적으로 데이터에 특정 함수를 적용
    print(row)


# ### (2) 출근 시간대 사람들이 가장 많이 타고 내리는 역은 어디일까

# In[2]:


# 아침 7시 승차 데이터 -> 인덱스 10번

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
result = []
for row in data :
    row[4:] = map(int, row[4:])
    result.append(row[10])
print(len(result)) # 598개 역에 대한 데이터가 저장된 것을 확인할 수 있음
print(result)


# In[3]:


# 막대그래프로 표현
import matplotlib.pyplot as plt
plt.bar(range(len(result)), result)
plt.show()


# In[4]:


import matplotlib.pyplot as plt
result.sort() # 오름차순으로 정렬
plt.bar(range(len(result)), result)
plt.show()

# 아래 그래프를 통해, 한 역이 다른 역들과 엄청나게 큰 차이를 두고 1위를 하고 있다는 사실을 알 수 있음


# In[7]:


# 출근 시간대인 7~9시까지의 승차 인원을 합치면?

for row in data :
    row[4:] = map(int, row[4:])
    result.append(sum(row[10:15:2]))
    
import matplotlib.pyplot as plt
result.sort()
plt.bar(range(len(result)), result)
plt.show()


# In[9]:


import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = 0 # 최댓값을 저장할 변수 초기화
mx_station = '' # 최댓값을 갖는 역 이름 저장 변수 초기화
for row in data : # 최댓값 찾기(전부 탐색하여 최댓값을 갱신하는 방식)
    row[4:] = map(int, row[4:])
    if sum(row[10:15:2]) > mx :
        mx = sum(row[10:15:2])
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx)


# #### 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기

# In[10]:


import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = 0
mx_station = ''
for row in data :
    row[4:] = map(int, row[4:])
    a = row[11:16:2] # 하차 인원 값 추출하기
    if sum(a) > mx :
        mx = sum(a)
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx)


# ### (3) 밤 11시에 사람들이 가장 많이 타는 역은 어디일까

# In[12]:


import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''
t = int(input('몇 시의 승차 인원이 가장 많은 역이 궁금하세요? : '))

for row in data :
    row[4:] = map(int, row[4:])
    a = row[4+(t-4)*2] # 입력 받은 시각의 승차 인원 값 추출하기
    if a > mx : # 모든 데이터 탐색
        mx = a
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx) # 승차 인원이 가장 큰 역과 인원 값 출력


# ### (4) 시간대별로 사람들이 가장 많이 타고 내리는 역은 어디일까

# In[13]:


import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = [0] * 24 # 시간대별 최대 승차 인원 저장 리스트 초기화
mx_station = [''] * 24 # 시간대별 최대 승차 인원 역 이름 저장 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        a = row[j*2+4] # j와 인덱스 번호 사이의 관계식 사용
        if a > mx[j] :
            mx[j] = a
            mx_station[j] = row[3]

print(mx_station)
print(mx)


# In[15]:


import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation = 90)
plt.show()


# In[19]:


import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = [0] * 24
mx_station = [''] * 24

for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        a = row[j*2+4]
        if a > mx[j] :
            mx[j] = a
            mx_station[j] = row[3] + '(' + str(j+4) + '시)'

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation = 90)
plt.show()


# #### 시간대별로 하차 인원이 가장 많은 역을 찾는 코드

# In[2]:


import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = [0] * 24 # 시간대별 최대 승차 인원을 저장할 리스트 초기화
mx_station = [''] * 24 # 시간대별 최대 승차 인원 역 이름을 저장할 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        b = row[5 + j * 2] # j값과 인덱스 번호 값의 관계식 사용
        if b > mx[j] :
            mx[j] = b
            mx_station[j] = row[3] + '(' + str(j+4) + '시)'

plt.rc('font', family = 'Malgun Gothic')
plt.bar(range(24), mx, color='b') # 막대그래프 속성 변경
plt.xticks(range(24), mx_station, rotation = 90)
plt.show()


# ### (5) 모든 지하철역에서 시간대별 승하차 인원을 모두 더하면

# 1. 데이터를 읽어온다.
# 
# 2. 모든 역에 대해 시간대별 승차 인원과 하차 인원을 누적해서 더한다.
# 
# 3. 시간대별 승차 인원과 하차 인원을 그래프로 표현한다.

# In[6]:


# 데이터 읽어오기

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
s_in = [0] * 24 # 승차 인원을 저장할 리스트 초기화
s_out = [0] * 24 # 하차 인원을 저장할 리스트 초기화


# In[5]:


# 모든 역에 대해 시간대별 승차 인원과 하차 인원을 누적해서 더하기

for row in data :
    row[4:] = map(int, row[4:])
    for i in range(24) :
        s_in[i] += row[4+i*2]
        s_out[i] += row[5+i*2]


# #### 지하철 시간대별 승하차 인원 추이를 나타내는 코드

# In[7]:


import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

s_in = [0] * 24 # 승차 인원을 저장할 리스트 초기화
s_out = [0] * 24 # 하차 인원을 저장할 리스트 초기화

for row in data :
    row[4:] = map(int, row[4:])
    for i in range(24) :
        s_in[i] += row[4+i*2]
        s_out[i] += row[5+i*2]
        
plt.rc('font', family = 'Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이') # 제목 추가
plt.plot(s_in, label='승차') # 승차 인원을 꺾은선 그래프로 표현
plt.plot(s_out, label='하차') # 하차 인원을 꺾은선 그래프로 표현
plt.legend()
plt.xticks(range(24), range(4, 28))
plt.show()

# 출퇴근 시간대에 승하차 인원이 많은 것을 확인할 수 있다

