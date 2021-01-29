#!/usr/bin/env python
# coding: utf-8

# ## 09 우리 동네 인구 구조를 파이 차트로 나타내기

# ### (1) 제주도에는 여성의 비율이 더 높을까

# In[25]:


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
        break
            
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

# 제주특별자치도 확인해보기 -> 오류 발생


# In[24]:


print(len(m), len(f))


# ### (2) 혈액형 비율 표현하기

# * pie() 함수

# In[27]:


import matplotlib.pyplot as plt
plt.pie([10, 20])
plt.show()


# * 동그란 원 그리기

# In[28]:


import matplotlib.pyplot as plt
size = [2441, 2312, 1031, 1233]
plt.axis('equal')
plt.pie(size)
plt.show()


# * 레이블 추가하기

# In[30]:


import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic') # 그래프에 한글 표시
size = [2441, 2312, 1031, 1233] # 데이터
label = ['A형', 'B형', 'AB형', 'O형'] # 레이블
plt.axis('equal')
plt.pie(size, labels=label)
plt.show()


# * 비율 및 범례 표시하기

# In[32]:


import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label = ['A형', 'B형', 'AB형', 'O형']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%') # 소수점 아래 첫 번째 소수점까지 표시
plt.legend() # 범례 추가
plt.show() 


# * 색 및 돌출 효과 정하기

# In[35]:


import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label = ['A형', 'B형', 'AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%', colors=color, explode=(0,0,0.1,0))
                                 # expode : 특정 혈액형의 비율 돌출 효과(0은 비돌출)
plt.legend()
plt.show() 


# * 제주도의 성별 인구 비율 표현하기

# In[42]:


import csv

f = open('gender.csv')
data = csv.reader(f)
size = []
name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data :
    if name in row[0] :
        m = 0
        f = 0
        for i in range(101) :
            m += int(row[i+3])
            f += int(row[i+106])
        break
size.append(m)
size.append(f)
print(size)


# In[43]:


import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
color = ['crimson', 'darkcyan']
plt.axis('equal')
plt.pie(size, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
                                                    # startangle : 파이 차트의 시작 각도 지정
plt.title(name + ' 지역의 남녀 성별 비율')
plt.show()


# #### 원하는 지역의 성별 인구를 파이 차트로 구하기

# In[ ]:


import csv

f = open('gender.csv')
data = csv.reader(f) # 데이터 불러오기

size = [] # 남녀 인구수를 저장할 빈 리스트 만들기

name = input('찾고 싶은 지역의 이름을 알려주세요 : ') # 지역 이름 입력받기
for row in data :
    if name in row[0] : # name과 일치하는 지역 찾기
        m = 0 # 남성 인구수를 누적해서 더할 변수 초기화하기
        f = 0 # 여성 인구수를 누적해서 더할 변수 초기화하기
        for i in range(101) :
            m += int(row[i+3]) # 남성 인구수를 누적해서 더하기
            f += int(row[i+106]) # 여성 인구수를 누적해서 더하기
        break # 반복 종료
size.append(m) # 남성 인구수를 size 리스트에 더하기
size.append(f) # 여성 인구수를 size 리스트에 더하기

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
color = ['crimson', 'darkcyan'] # 색상 설정하기
plt.axis('equal')

plt.pie(size, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
plt.title(name + ' 지역의 남녀 성별 비율') # 제목 설정하기
plt.show()

