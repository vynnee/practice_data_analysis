#!/usr/bin/env python
# coding: utf-8

# ## 02 데이터 분석을 위한 라이브러리

# #### 판다스의 설치 및 활용

# * 판다스 라이브러리 불러오기
# 
# 데이터 분석 라이브러리로, 데이터 프레임이라는 자료구조를 사용
# 
# 데이터 프레임은 엑셀의 스프레드시트와 유사한 형태이며 데이터를 쉽게 처이할 수 있도록 함

# In[8]:


import pandas as pd


# * 데이터 프레임을 생성하고 일부분 살펴보기

# In[4]:


# 판다스의 프레임을 생성합니다.
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
custom = [1, 5, 25, 13, 23232]

BabyDataSet = list(zip(names, births))
df = pd.DataFrame(data = BabyDataSet, columns = ['Names', 'Births'])

# 데이터 프레임의 상단 부분을 출력합니다.
df.head()


# * 데이터 프레임의 기본 정보 출력하기

# In[5]:


# 데이터 프레임의 열 타입 정보를 출력합니다.
df.dtypes


# In[7]:


# 데이터 프레임의 인덱스 정보입니다.
df.index


# In[9]:


# 데이터 프레임의 열의 형태 정보입니다.
df.columns


# * 데이터 프레임의 열 선택하기

# In[10]:


# 데이터 프레임에서 하나의 열을 선택합니다.
df['Names']


# * 데이터 프레임의 인덱스 선택하기

# In[11]:


# 0~3번째 인덱스를 선택합니다.
df[0:3]


# * 조건을 추가하여 선택하기

# In[13]:


# Births 열이 100보다 큰 데이터를 선택합니다.
df[df['Births'] > 100]


# * 평균값 계산하기

# In[14]:


# 데이터 프레임에서의 평균값을 계산합니다.
df.mean()


# #### 넘파이의 설치와 활용

# * 넘파이 라이브러리 불러오기
# 
# 넘파이는 Numerical python의 줄임말로, 수치 계산을 위해 만들어진 파이썬 라이브러리
# 
# 배열 개념으로 변수를 사용하며 벡터, 행렬 등의 연산을 쉽고 빠르게 수행하도록 지원

# In[15]:


import numpy as np


# * 넘파이 배열 생성하기

# In[17]:


arr1 = np.arange(15).reshape(3,5)
arr1
# 15개의 숫자를 (3,5) 차원으로 생성


# * 넘파이 배열 정보 확인하기

# In[18]:


arr1.shape


# In[19]:


arr1.dtype


# * 다른 형태의 배열 생성하기

# In[21]:


arr3 = np.zeros((3,4))
arr3


# * 넘파이 배열을 이용한 사칙연산 수행하기

# In[22]:


arr4 = np.array([
    [1,2,3],
    [4,5,6]
], dtype = np.float64)

arr5 = np.array([
    [7,8,9],
    [10,11,12]
], dtype = np.float64)

# 사칙연산을 출력합니다.
print("arr4 + arr5 = ")
print(arr4 + arr5, "\n")
print("arr4 - arr5 = ")
print(arr4 - arr5, "\n")
print("arr4 * arr5 = ")
print(arr4 * arr5, "\n")
print("arr4 / arr5 = ")
print(arr4 / arr5, "\n")


# #### matplotlib

# * Matplotlib 라이브러리 불러오기
# 
# Matplotlib 라이브러리는 데이터를 시각화해주는 가장 기본적인 라이브러리

# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline # 현재 실행중인 주피터 노트북에서 그래프를 출력 가능하도록 선언하는 명령어')
import matplotlib.pyplot as plt


# * 막대 그래프 출력하기

# In[24]:


y = df['Births']
x = df['Names']

# 막대 그래프를 출력합니다.
plt.bar(x, y) # 막대 그래프 객체 생성
plt.xlabel('Names') # x축 제목
plt.ylabel('Births') # y축 제목
plt.title('Bar plot') # 그래프 제목
plt.show() # 그래프 출력


# * 산점도 그래프 출력하기

# In[25]:


# 랜덤 추출 시드를 고정합니다.
np.random.seed(19920613)

# 산점도 데이터를 생성합니다.
x = np.arange(0.0, 100, 5.0)
y = (x * 1.5) + np.random.rand(20) * 50

# 산점도 데이터를 출력합니다.
plt.scatter(x, y, c="b", alpha=0.5, label="scatter point")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper left')
plt.title('Scatter plot')
plt.show()

