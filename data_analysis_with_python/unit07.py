#!/usr/bin/env python
# coding: utf-8

# ## 07 우리 동네 인구 구조 시각화하기

# ### (1) 인구 공공데이터 내려받기

# www.mois.go.kr  
# 정책자료 -> 통계 -> 주민등록 인구통계

# ### (3) 우리 동네 인구 구조 시각화하기

# In[4]:


import csv
f = open('age.csv')
data = csv.reader(f)

for row in data :
    print(row)


# In[5]:


# 우리 동네 데이터만 선택해서 출력하기

import csv
f = open('age.csv')
data = csv.reader(f)

for row in data :
    if '서울특별시 구로구 신도림동(1153051000)' == row[0] :
        print(row)


# In[6]:


# in 연산자

print('신도림' in '서울특별시 구로구 신도림동(1153051000)')
print('1153' in '서울특별시 구로구 신도림동(1153051000)')
print('()' in '서울특별시 구로구 신도림동(1153051000)')


# In[11]:


# in 연산자 활용하여 코드 간단하게 수정

import csv
f = open('age.csv')
data = csv.reader(f)

for row in data :
    if '신도림' in row[0] :
        print(row)


# In[13]:


# 0~100세 이상까지의 인구수를 순서대로 읽기
# row[0] : 지역명
# row[1], row[2] : 해당 지역의 총 인구수
# row[3] ~ : n세 인구수

import csv
f = open('age.csv')
data = csv.reader(f)

for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            print(i)


# In[14]:


# 0~100세 이상까지의 인구수를 순서대로 저장

import csv
f = open('age.csv')
data = csv.reader(f)
result = [] # 빈 리스트 만들기

for row in data :
    if '신도림' in row[0] : # '신도림'이 포함된 행정구역 찾기
        for i in row[3:] : # 0세부터 끝(100세 이상)까지 모든 연령에 대해 반복하기
            result.append(i) # 해당 연령의 인구수 리스트에 순서대로 저장하기
            
print(result)


# In[19]:


import csv
f = open('age.csv')
data = csv.reader(f)
result = []

for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i)) # 문자열로 저장된 각 값을 정수로 바꾸기

print(result)


# In[20]:


# 데이터 시각화
import matplotlib.pyplot as plt
plt.style.use('ggplot') # 격자 무늬 스타일 지정
plt.plot(result)
plt.show()

