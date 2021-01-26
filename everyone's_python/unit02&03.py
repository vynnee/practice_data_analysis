#!/usr/bin/env python
# coding: utf-8

# # 02 서울의 기온 데이터 분석하기

# ### (1) CSV 파일에서 데이터 읽어오기

# In[8]:


import csv
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f, delimiter = ',')
print(data)
f.close()


# ### (2) 데이터 출력하기

# In[4]:


import csv
f = open('seoul.csv', encoding = 'cp949')
data = csv.reader(f)
for row in data :
    print(row)
f.close()


# ### (3) 헤더 저장하기

# In[6]:


import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
print(header)
f.close()


# In[1]:


import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    print(row)
f.close()


# ### (4) 기온 공공데이터에 질문하기

# 데이터를 살펴보고, 가설을 세워보기

# # 03 서울이 가장 더웠던 날은 언제였을까

# ### (1) 질문 다듬기

# 서울이 가장 더웠던 날은 언제였을까? 얼마나 더웠을까?
# -> 기상 관측 이래, 서울의 최고 기온이 가장 높았던 날은 언제였고, 몇 도였을까?

# ### (2) 문제 해결 방법 구상하기

# 1. 데이터를 읽어온다.
# 2. 순차적으로 최고 기온을 확인한다.
# 3. 최고 기온이 가장 높았던 날짜와 데이터를 저장한다.
# 4. 최종 저장된 데이터를 출력한다.

# ### (3) 파이썬 코드를 구현하기

# In[14]:


import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    print(row)
f.close()

# 현재 최고 기온 데이터는 문자열임
# 따라서 float 형태로 변환해야함
# float() 함수 사용


# In[15]:


import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    row[-1] = float(row[-1]) # 최고 기온을 실수로 변환
    print(row)
f.close()

# 1950년 9월 이후부터 오류 발생
# 데이터가 없기 때문임
# 따라서 대체할 특정 값을 넣어줌


# In[17]:


import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    if row[-1] == '':
        row[-1] = -999  # -999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1])
    print(row)
f.close()

# 1950년 9월 이후부터 오류 발생
# 데이터가 없기 때문임
# 따라서 대체할 특정 값을 넣어줌


# In[20]:


import csv
max_temp = -999 # 최고 기온 값을 저장할 변수
max_date = '' # 최고 기온이 가장 높았던 날짜를 저장할 변수
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    if row[-1] == '':
        row[-1] = -999  # -999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1])
    if max_temp < row[-1] :
        max_date = row[0]
        max_temp = row[-1]   
f.close()
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은 ', max_date, '로, ', max_temp, '도 였습니다.')

