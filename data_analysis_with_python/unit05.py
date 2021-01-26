#!/usr/bin/env python
# coding: utf-8

# # 05 내 생일의 기온 변화를 그래프로 그리기

# ### (1) 데이터에 질문하기

# - 데이터 읽어오기

# In[2]:


import csv
f = open('seoul.csv')
data = csv.reader(f)
for row in data :
    print(row)


# In[3]:


import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)

for row in data :
    print(row[-1])


# - 데이터 리스트에 저장하기

# In[8]:


import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = [] # 최고 기온 데이터를 저장할 리스트 생성

for row in data :
    if row[-1] != "" :# 최고 기온 데이터 값이 존재한다면
        result.append(float(row[-1])) # result 리스트에 최고 기온 값 추가
                      
print(result)


# In[9]:


print(len(result)) # 데이터 개수 확인


# ### (2) 데이터 시각화하기

# In[13]:


import csv
import matplotlib.pyplot as plt

plt.figure(figsize = (10, 2)) # 가로로 10인치, 세로로 2인치로 설정
plt.plot(result, 'r') # result 리스트에 저장된 값을 빨간색 그래프로 그리기
plt.show() # 그래프 나타내기


# In[14]:


s = 'hello python'
print(s.split())

# split() 는 사용자가 설정하는 특정 문자를 기준으로 문자열을 분리한다.
# 특정 문자가 없다면, 공백으로 분리한다.


# In[15]:


date = '1907-10-01'
print(date.split('-')) # '-' 를 기준으로 문자열을 분리


# In[16]:


print(date.split('-')[0])
print(date.split('-')[1])
print(date.split('-')[2])


# In[25]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' : # 최고 기온 값이 존재한다면
        if row[0].split('-')[1] == '08' : # 8월에 해당하는 값이라면
            result.append(float(row[-1])) # result 리스트에 최고 기온 값 추가
            
plt.plot(result, 'hotpink') # result 리스트에 저장된 값을 hotpink 색으로 그리기
plt.show() # 그래프 나타내기


# In[26]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' : 
            result.append(float(row[-1]))
            
plt.plot(result, 'hotpink') 
plt.show()

# 최근 들어 기온이 높아짐
# 지구 온난화 또는 다양한 원인으로 인해
# 예전보다 기온이 상승했을 것으로 추측할 수 있음


# In[27]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = [] # 최고 기온 값을 저장할 리스트 high 생성
low = [] # 최저 기온 값을 저장할 리스트 low 생성

for row in data :
    if row[-1] != '' and row[-2] != '' : # 최고 기온 값과 최저 기온 값이 존재한다면
        if 1983 <= int(row[0].split('-')[0]) : # 1983년 이후 데이터라면
            if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
                                                # 2월 14일이라면
                    high.append(float(row[-1])) # 최고 기온 값을 hight 리스트에 저장
                    low.append(float(row[-2])) # 최저 기온 값을 low 리스트에 저장
            
plt.plot(high, 'hotpink') # high 리스트에 저장된 값을 hotpink 색으로 그리기
plt.plot(low, 'skyblue') # low 리스트에 저장된 값을 skyblue 색으로 그리기
plt.show() # 그래프 나타내기


# In[45]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = [] 
low = []

for row in data :
    if row[-1] != '' and row[-2] != '' : 
        if 1983 <= int(row[0].split('-')[0]) :
            if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
                    high.append(float(row[-1])) 
                    low.append(float(row[-2])) 
            
plt.rc('font', family = 'Malgun Gothic')
plt.title('내 생일의 기온 변화그래프')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')
plt.show()


# ! 평균 기온 그래프 그려보기

# In[10]:


import csv
import matplotlib.pyplot as plt
import numpy as np

f = open('seoul.csv')
data = csv.reader(f)
next(data)
avg = []


for row in data :
    if row[2] != '' :
        if 1908 <= int(row[0].split('-')[0]) : 
                avg.append(float(row[2]))

x = np.arange(1908, 2012, 20)
                
plt.plot(x, avg, color = 'red')
plt.show()

# 다시 해보기


# - 내 생일의 기온 변화를 그래프로 그리기

# In[55]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = [] # 최고 기온 값을 저장할 리스트 high 생성
low = [] # 최저 기온 값을 저장할 리스트 low 생성

for row in data :
    if row[-1] != '' and row[-2] != '' : # 최고 기온 값과 최저 기온 값이 존재한다면
        if 1983 <= int(row[0].split('-')[0]) : # 1983년 이후 데이터라면
            if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
                                                # 2월 14일이라면
                    high.append(float(row[-1])) # 최고 기온 값을 hight 리스트에 저장
                    low.append(float(row[-2])) # 최저 기온 값을 low 리스트에 저장
            
plt.rc('font', family = 'Malgun Gothic') # 맑은 고딕을 기본 글꼴로 설정
plt.title('내 생일의 기온 변화그래프') # 제목 설정
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
plt.plot(high, 'hotpink', label = 'high') # high 리스트에 저장된 값을 hotpink 색으로 그리기
plt.plot(low, 'skyblue', label = 'low') # low 리스트에 저장된 값을 skyblue 색으로 그리기
plt.legend() # 범례 표시
plt.show() # 그래프 나타내기

