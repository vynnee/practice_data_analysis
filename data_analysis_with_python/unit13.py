#!/usr/bin/env python
# coding: utf-8

# ## 13 숫자 데이터를 쉽게 다루게 돕는 numpy 라이브러리

# ### (1) matplotlib 홈페이지
# 
# matplotlib.org

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# In[5]:


import matplotlib.pyplot as plt
import numpy as np

t = []
p2 = []
p3 = []

for i in range(0, 50, 2) :
    t.append(i/10)
    p2.append((i/10) ** 2)
    p3.append((i/10) ** 3)
    
plt.plot(t, t, 'r--', t, p2, 'bs', t, p3, 'g^')
plt.show()


# ### (2) numpy 라이브러리 시작하기

# In[7]:


import numpy 
print(numpy.sqrt(2))


# In[8]:


import numpy as np
print(np.sqrt(2))


# In[9]:


import numpy as np
print(np.pi)
print(np.sin(0))
print(np.cos(np.pi))


# In[10]:


import numpy as np
a = np.random.rand(5)
print(a)
print(type(a))

# numpy 라이브러리에는 서브 라이브러리가 존재 (ex. random 서브 라이브러리)
# rand() 함수 : 0~1 사이에 있는 n개의 실수 랜덤으로 생성

# ndarray의 nd : N-Dimensional, 즉 N 차원
# ndarray의 array : 배열


# In[13]:


import numpy as np
print(np.random.choice(6,10))
# 0~5 사이의 숫자를 랜덤하게 10번 생성


# In[14]:


import numpy as np
print(np.random.choice(6,10, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1]))


# ### (3) numpy 라이브러리를 활용해 그래프 그리기

# In[17]:


import matplotlib.pyplot as plt
import numpy as np
dice = np.random.choice(6,1000000, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
plt.hist(dice, bins=6)
plt.show()


# In[19]:


import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(10, 100, 200)
y = np.random.randint(10, 100, 200)
size = np.random.rand(100) * 100

plt.scatter(x, y, s = size, c = x, cmap = 'jet', alpha = 0.7)
plt.colorbar()
plt.show()


# ### (4) numpy array 생성하기

# In[20]:


import numpy as np
a = np.array([1,2,3,4])
print(a)


# In[21]:


import numpy as np
a = np.array([1,2,3,4])
print(a[1], a[-1]) # a의 1번 인덱스 값, -1번 인덱스 값 출력
print(a[1:]) # a의 1번 인덱스를 기준으로 슬라이싱 결과 출력


# In[22]:


import numpy as np
a = np.array([1,2,'3',4])
print(a)

# numpy array 는 한 가지 타입의 데이터만을 저장
# 숫자와 문자가 함께 저장되었다면 문자로 변환되어 저장


# In[23]:


import numpy as np
a = np.zeros(10) # 0 으로 이루어진 크기가 10인 배열 생성
print(a)


# In[24]:


import numpy as np
a = np.ones(10) # 1 로 이루어진 크기가 10인 배열 생성
print(a)


# In[26]:


import numpy as np
a = np.eye(3) # 3행 x 3열의 단위 배열 생성
print(a)


# In[27]:


import numpy as np
print(np.arange(3)) # arange() 함수에 1개 값 입력
print(np.arange(3,7)) # arange() 함수에 2개 값 입력
print(np.arange(3,7,2)) # arange() 함수에 3개 값 입력


# In[30]:


import numpy as np
a = np.arange(1, 2, 0.1) # 1이상 2미만 구간에서 0.1 간격으로 실수 생성
b = np.linspace(1, 2, 11) # 1부터 2까지 11개 구간으로 나눈 실수 생성
print(a)
print(b)


# In[31]:


import numpy as np
a = np.arange(-np.pi, np.pi, np.pi/10)
b = np.linspace(-np.pi, np.pi, 20)
print(a)
print(b)


# ### (5) numpy array의 다양한 활동

# In[32]:


# np.zeros(), np.ones() 함수는 있는데 np.twos(), np.threes() 함수는 없음
# 그렇다면 초기값이 5인 배열을 100개 만들고 싶다면?

import numpy as np
a = np.zeros(10) + 5
print(a)


# In[33]:


import numpy as np
a = np.linspace(1, 2, 11)
print(np.sqrt(a)) # a값의 제곱근을 출력함


# In[34]:


import matplotlib.pyplot as plt
import numpy as np

a = np.arange(-np.pi, np.pi, np.pi/100)

plt.plot(a, np.sin(a))
plt.show()


# In[35]:


import matplotlib.pyplot as plt
import numpy as np

a = np.arange(-np.pi, np.pi, np.pi/100)

plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.plot(a+np.pi/2, np.sin(a))
plt.show()


# In[36]:


import numpy as np
a = np.arange(-5, 5)
print(a)


# In[37]:


print(a<0)


# In[38]:


print(a[a<0])


# In[40]:


mask1 = abs(a) > 3 # abs() : 절대값
print(a[mask1])


# In[41]:


mask1 = abs(a) > 3
mask2 = abs(a) % 2 == 0
print(a[mask1+mask2]) # 둘 중 하나의 조건이라도 참일 경우
print(a[mask1*mask2]) # 두 가지 조건이 모두 참일 경우


# #### numpy 라이브러리를 사용하여 재미있는 버블 차트 그리기

# In[42]:


import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(-100, 100, 1000) # 1000개의 랜덤 값 추출
y = np.random.randint(-100, 100, 1000) # 1000개의 랜덤 값 추출
size = np.random.rand(100) * 100
mask1 = abs(x) > 50
mask2 = abs(y) > 50
x = x[mask1+mask2]
y = y[mask1+mask2]

plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
plt.colorbar()
plt.show()

