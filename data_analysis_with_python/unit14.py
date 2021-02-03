#!/usr/bin/env python
# coding: utf-8

# ## 14 numpy를 활용한 나만의 프로젝트 만들기

# ### (5) 알고리즘을 코드로 표현하기

# 1. 데이터를 읽어온다.

# In[1]:


import csv
f = open('age.csv')
data = csv.reader(f)
for row in data :
    print(row)


# In[2]:


import csv
f = open('age.csv')
data = csv.reader(f)
next(data)
for row in data :
    print(row)


# 2. 궁금한 지역의 이름을 입력받는다.

# In[3]:


name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')


# 3. 궁금한 지역의 인구 구조를 저장한다.

# In[2]:


import csv
f = open('age.csv')
data = csv.reader(f)
next(data)

home = [] # 입력받은 지역의 데이터를 저장할 리스트 생성
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

for row in data :
    if name in row[0] : # 입력받은 지역의 이름이 포한된 행 찾기
        for i in row[3:] : # 3번 인덱스 값부터 슬라이싱
            home.append(int(i)) # 입력받은 지역의 데이터를 home에 저장
print(home) # home에 저장된 데이터 출력


# In[3]:


import numpy as np
import csv
f = open('age.csv')
data = csv.reader(f)
next(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)
print(home)


# In[4]:


import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.title(name + ' 지역의 인구 구조')
plt.plot(home)
plt.show()


# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 찾기

# In[5]:


# 햔 번 불러온 데이터를 여러 번 사용하려면 어떻게 해야 할까?
import numpy as np
import csv
f = open('age.csv')
data = csv.reader(f) # 여기서 데이터 읽음
next(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data : # 처음부터 마지막 줄까지 한 줄씩 아래로 읽힘
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2]) # for 반복문이 끝난 후에는 더 이상 읽을 수 있는 데이터가 없음
for row in data :
    print(row) # 따라서 다시 읽으려고 해도 읽을 데이터가 없음


# In[6]:


# 해결 방안
data = list(data) # 해당 코드 추가


# In[8]:


import numpy as np
import csv
f = open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
for row in data :
    print(row)


# In[9]:


# 전국의 모든 지역 중 한 곳(B)를 선택한다. 그리고 궁금한 지역 A의 0에 인구 비율에서 B의 0세 인구 비율을 뺀다.

import numpy as np
import csv
f = open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
for row in data :
    away = np.array(row[3:], dtype=int)/int(row[2])
    print(home - away)
    
# 신도림동과 다른 모든 지역과의 비율 차를 구함


# In[11]:


# 비율 차를 100세 이상 인구수에 해당하는 값까지 반복한 후 각각의 차이를 모두 더한다.

import numpy as np
import csv
f = open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
for row in data :
    away = np.array(row[3:], dtype=int)/int(row[2])
    print(np.sum(home - away))


# In[12]:


# 전국의 모든 지역에 대해 반복하며 그 차이가 가장 작은 지역을 찾는다.

import numpy as np
import csv

f = open('age.csv')
data = csv.reader(f)
next(data)

data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화

for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
for row in data :
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum(home - away)
    if s < mn :
        mn = s
        result_name = row[0]
        result = away


# In[13]:


import matplotlib.pyplot as plt
plt.plot(home)
plt.plot(result)
plt.show()


# In[15]:


import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.title(name + ' 지역과 가장 비슷한 인구 구조를 가진 지역') # 그래프 제목 설정
plt.plot(home, label = name) # home 값을 그리는 그래프 레이블 설정
plt.plot(result, label=result_name) # result 값을 그리는 그래프 레이블 설정
plt.legend() # 범례 표기
plt.show()

# 수긍하기 어려운 그래프가 그려짐
# 인구 구조가 가장 비슷한 지역을 찾는 알고리즘이 잘못 설계된 것으로 예상됨
# s < mn 조건으로, 0에 가까운 값을 찾음
# 그러나 마이너스 값이 존재했고, 그 값이 선택되어 이상한 결과가 도출됨


# In[21]:


import numpy as np
import csv

f = open('age.csv')
data = csv.reader(f)
next(data)

data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화

for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
for row in data :
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home - away)**2)
    if s < mn :
        mn = s
        result_name = row[0]
        result = away
        
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.title(name + ' 지역과 가장 비슷한 인구 구조를 가진 지역') # 그래프 제목 설정
plt.plot(home, label = name) # home 값을 그리는 그래프 레이블 설정
plt.plot(result, label=result_name) # result 값을 그리는 그래프 레이블 설정
plt.legend() # 범례 표기
plt.show()

# 신도림동과 가장 비슷한 지역은 신도림동
# 입력받은 이름과 같은 이름은 제외해보자


# In[29]:


import numpy as np
import csv

f = open('age.csv')
data = csv.reader(f)
next(data)

data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화

for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
for row in data :
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home - away)**2)
    if s < mn and name not in row[0]:
        mn = s
        result_name = row[0]
        result = away
        
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.title(name + ' 지역과 가장 비슷한 인구 구조를 가진 지역') # 그래프 제목 설정
plt.plot(home, label = name) # home 값을 그리는 그래프 레이블 설정
plt.plot(result, label=result_name) # result 값을 그리는 그래프 레이블 설정
plt.legend() # 범례 표기
plt.show()


# #### 우리 동네와 인구 구조가 가장 비슷한 동네를 찾는 코드

# In[30]:


import numpy as np
import csv

# 1. 데이터를 읽어온다.
f = open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)

# 2. 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1
result_name = ''
result = 0

# 3. 궁금한 지역의 인구 구조를 저장한다.
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
        
# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다.
for row in data :
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home - away)**2)
    if s < mn and name not in row[0]:
        mn = s
        result_name = row[0]
        result = away
        
# 5. 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.title(name + ' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label = name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()

