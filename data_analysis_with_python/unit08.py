#!/usr/bin/env python
# coding: utf-8

# ## 08 인구 구조를 다양한 형태로 시각화하기

# #### 혼자 해보기

# In[4]:


import csv
f = open('age.csv')
data = csv.reader(f)
result = []

region = input("인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요 : ")

for row in data :
    if region in row[0] :
        for i in row[3:] :
            result.append(int(i)) # 문자열로 저장된 각 값을 정수로 바꾸기

# 데이터 시각화
import matplotlib.pyplot as plt
plt.style.use('ggplot') # 격자 무늬 스타일 지정
plt.plot(result)
plt.show()


# #### 정답

# In[5]:


import csv

f = open('age.csv')
data = csv.reader(f)
result = []
name = input("인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요 : ")
# 인구 구조가 궁금한 지역의 이름을 input() 함수로 입력 받기

for row in data :
    if name in row[0] : # 입력받은 내용이 포함된 값 찾기
        for i in row[3:] :
            result.append(int(i))
            
import matplotlib.pyplot as plt
plt.style.use('ggplot') # 격자 무늬 스타일 지정
plt.rc('font', family = 'Malgun Gothic') # 한글 제목을 넣기 위해 폰트 설정
plt.title(name + ' 지역의 인구 구조') # title() 함수 사용하여 제목 넣기
plt.plot(result)
plt.show()


# ### (1) 막대그래프 그리기

# * bar() 함수

# In[6]:


import matplotlib.pyplot as plt
plt.bar([0, 1, 2, 4, 6, 10], [1, 2, 3, 5, 6, 7])
plt.show()

# bar(막대를 표시할 위치, 막대이 높이) <- 두 값의 개수 일치해야함


# In[7]:


import matplotlib.pyplot as plt
plt.bar(range(6), [1, 2, 3, 5, 6, 7]) # range() : 오름차순
plt.show()


# In[9]:


import csv
f = open('age.csv')
data = csv.reader(f)

result = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i))

import matplotlib.pyplot as plt
plt.bar(range(101), result) # 0~100세 이상까지 101개의 구간 존재
plt.show()


# * barh() 함수

# In[11]:


plt.barh(range(101), result)
# range(101) : y축의 막대 위치
# result : 막대의 너비


# ### (2) 항아리 모양 그래프 그리기

# * 데이터 수집하기

# In[12]:


# 방법 1

import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
for row in data :
    if '신도림' in row[0] :
        for i in range(0, 101) :
            m.append(int(row[i+3]))
            f.append(int(row[-(i+1)]))
f.reverse() # 리스트의 값을 역순으로 재베열하는 함수


# In[ ]:


# 방법 2

import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:104] :
            m.append(int(i)) # 남성 데이터를 리스트 m에 저장
        for i in row[106:] :
            f.append(int(i)) # 여성 데이터를 리스트 f에 저장


# * 데이터 시각화하기

# In[13]:


import matplotlib.pyplot as plt
plt.barh(range(101), m)
plt.barh(range(101), f)
plt.show()


# In[15]:


# 남성 데이터를 왼쪽, 여성 데이터를 오른쪽에 두도록 수정

import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:104] :
            m.append(-int(i)) # 마이너스 부호를 넣어서 음수로 변경
        for i in row[106:] :
            f.append(int(i))

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.title('신도림 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()


# In[16]:


# 남성 인구 그래프 마이너스 기호 깨짐 해결

import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:104] :
            m.append(-int(i)) # 마이너스 부호를 넣어서 음수로 변경
        for i in row[106:] :
            f.append(int(i))

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('신도림 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()


# * 우리 동네 인구 구조를 항아리 모양 그래프로 그리기

# #### 혼자 해보기

# In[4]:


import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

region = input('찾고 싶은 지역의 이름을 알려주세요 : ')

for row in data :
    if region in row[0] :
        for i in row[3:104] :
            m.append(-int(i))
        for i in row[106:] :
            f.append(int(i))

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(region + ' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()


# #### 정답

# In[20]:


import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')

for row in data :
    if name in row[0] :
        for i in row[3:104] :
            m.append(-int(i))
        for i in row[106:] :
            f.append(int(i))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize=(10, 5), dpi=300)
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name + ' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label='남성')
plt.barh(range(101), f, label='여성')
plt.legend()
plt.show()

