#!/usr/bin/env python
# coding: utf-8

# ## 10 우리 동네 인구 구조를 산점도로 나타내기

# ### (1) 꺾은선 그래프로 표현하기

# In[ ]:


import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

name = input('궁금한 동네를 입력해주세요 : ')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i])) # 남성 데이터 저장하기
            f.append(int(row[i+103])) # 여성 데이터 저장하기
        break
    
import matplotlib.pyplot as plt
plt.plot(m, label='Male')
plt.plot(f. label='Female')
plt.legend()
plt.show()


# ### (2) 막대그래프로 표현하기

# In[ ]:


import csv
f = open('gender.csv')
data = csv.reader(f)
result = []

name = input('궁금한 동네를 입력해주세요 : ')
for row in data :
    if name in row[0]
        for i in range(3,104) :
            result.append(int(row[i]) - int(row[i+103]))
        break

import matplotlib.pyplot as plt
plt.bar(range(101), result)
plt.show()


# ### (3) 산점도로 표현하기

# ### (4) scatter() 함수로 표현하기

# In[ ]:


import matplotlib.pyplot as plt
plt.scatter([1,2,3,4], [10,30,20,40])
plt.show()

# 격자 무늬 스타일 지정하고 싶을 경우
# plt.style.use('ggplot') 추가


# ### (5) 버블 차트로 표현하기

# In[ ]:


import matplotlib.pyplot as plt
plt.scatter([1,2,3,4], [10,30,20,40], s=[100,200,250,300])
                        # s : size 의미
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
plt.scatter([1,2,3,4], [10,30,20,40], s=[30,60,90,120], c=['red','blue','green','gold'])
            # c : 각 점의 색상 지정
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
plt.scatter([1,2,3,4], [10,30,20,40], s=[30,60,90,120], c=range(4))
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
plt.scatter([1,2,3,4], [10,30,20,40], s=[30,60,90,120], c=range(4), cmap='jet')
                    # cmap : 컬러맵 속성, jet은 무지개색
plt.show()


# In[ ]:


import matplotlib.pyplot as plt
import random
x = []
y = []
size = []
for i in range(100) :
    x.append(random.randint(50, 100))
    y.append(random.randint(50, 100))
    size.append(random.randint(10,100))
plt.scatter(x, y, s=size)
plt.show()


# In[ ]:


plt.scatter(x, y, s=size, c=size, cmap='jet')
plt.colorbar()
plt.show()


# In[ ]:


plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()


# ### (6) 제주도의 연령대별 성별 비율을 산점도로 표현하기

# In[ ]:


import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []

name = input('궁금한 동네를 입력해주세요 : ')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break
        
import matplotlib.pyplot as plt
plt.scatter(m, f)
plt.show()   


# In[ ]:


import matplotlib.pyplot as plt
plt.scatter(x, y, c=range(101), alpha=0.5, cmap='jet') # 컬러맵 적용
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g') # 추세선 추가
plt.show()


# #### 제주도의 연령대별 성별 비율을 산점도로 표현하기

# In[ ]:


import csv
import math
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
size = []

name = input('궁금한 동네를 입력해주세요 : ')
for row in data :
    if name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i]))
            f.append(int(row[i+103]))
            size.append(mat.sqrt(int(row[i])+int(row[i+103])))
        break

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', famliy='Malgun Gothic')
plt.figure(figsize=(10,5), dpi=300)
plt.title(name+' 지역의 성별 인구 그래프')
plt.scatter(x, y, s=size, c=range(101), alpha=0.5, cmap='jet') 
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')
plt.xlabel('남성 인구수')
plt.ylabel('여성 인구수')
plt.show()

