#!/usr/bin/env python
# coding: utf-8

# ## 06 기온 데이터를 다양하게 시각화하기

# ### (2) 히스토그램

# - hist() 함수

# In[1]:


import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()


# - 주사위 시뮬레이션

# In[2]:


import random
print(random.randint(1, 6))


# In[6]:


import random
dice = []
for i in range(5) :
    dice.append(random.randint(1, 6))
print(dice)


# In[7]:


import matplotlib.pyplot as plt
plt.hist(dice, bins=6)
plt.show()


# In[1]:


import random
dice = []
for i in range(100) : # 100으로 수정
    dice.append(random.randint(1, 6))
print(dice)

import matplotlib.pyplot as plt
plt.hist(dice, bins=6)
plt.show()


# In[2]:


import random
dice = []
for i in range(10000) : # 10000으로 수정
    dice.append(random.randint(1, 6))
print(dice)

import matplotlib.pyplot as plt
plt.hist(dice, bins=6)
plt.show()


# ### (3) 기온 데이터를 히스토그램으로 표현하기

# In[4]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))
    
plt.hist(result, bins=100, color='r') # 히스토그램으로 나타내기
plt.show()


# In[6]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = [] # 8월의 최고 기온 값을 저장할 aug 리스트 생성

for row in data :
    month = row[0].split('-')[1] # -로 구분된 값 중 2번째 값을 month에 저장
    if row[-1] != '' :
        if month == '08' : # 8월달이라면
            aug.append(float(row[-1])) # aug 리스트에 최고 기온 값 추가
    
plt.hist(aug, bins=100, color='r')
plt.show()


# - 1월과 8월의 데이터를 히스토그램으로 시각화하기

# In[7]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)

aug = []
jan = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '' :
        if month == '08' :
            aug.append(float(row[-1]))
        if month == '01' :
            jan.append(float(row[-1]))

plt.hist(aug, bins=100, color='r', label='Aug')
plt.hist(jan, bins=100, color='b', label='Jan')
plt.legend()
plt.show()


# ### (4) 기온 데이터를 상자 그림으로 표현하기

# In[8]:


import matplotlib.pyplot as plt
import random

result = []
for i in range(13) :
    result.append(random.randint(1, 1000))
print(sorted(result))

plt.boxplot(result)
plt.show()


# In[10]:


import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))
        
import matplotlib.pyplot as plt
plt.boxplot(result)
plt.show()


# In[12]:


import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)

aug = []
jan = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '' :
        if month == '08' :
            aug.append(float(row[-1]))
        if month == '01' :
            jan.append(float(row[-1]))

plt.boxplot(aug)
plt.boxplot(jan)
plt.show()


# In[13]:


plt.boxplot([aug, jan])


# In[14]:


import matplotlib.pyplot as plt
import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)

# 월별 데이터를 저장할 리스트 month 생성(12개)
month = [[],[],[],[],[],[],[],[],[],[],[],[]]

for row in data :
    if row[-1] != '' :
        # 월과 같은 번호의 인덱스에 월별 데이터 저장(예:1월->month[0])
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))
        
plt.boxplot(month)
plt.show()


# In[15]:


import matplotlib.pyplot as plt
import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = [] # 일별 데이터를 저장할 리스트 day 생성
for i in range(31) :
    day.append([]) # day 리스트 내 31개 리스트 생성
    
for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '08' : # 8월이라면
            # 최고 기온 값 저장
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))
            
plt.style.use('ggplot') # 그래프 스타일 지정
plt.figure(figsize=(10,5), dpi=300) # 그래프 크기 수정
plt.boxplot(day, showfliers=False) # 아웃라이어 값 생략

plt.show()

