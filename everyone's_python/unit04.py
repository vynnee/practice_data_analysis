#!/usr/bin/env python
# coding: utf-8

# # 04 기본 그래프 그리기

# ### (1) 'matplotlib 라이브러리'란?

# In[3]:


import matplotlib.pyplot as plt

# matplotlib 라이브러리 중 pyplot 이라는 모듈을 주로 사용할 예정.


# ### (2) 기본 그래프 그리기

# In[4]:


import matplotlib.pyplot as plt
plt.plot([10, 20, 30, 40]) # y축 값으로 입력됨
plt.show() # x축 값은 자동으로 0부터 1씩 증가하는 정수로 입력됨


# In[5]:


import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [12, 43, 25, 15]) # x, y 순으로 입력됨
plt.show()


# ### (3) 그래프에 옵션 추가하기

# - 그래프에 제목 넣기

# In[6]:


import matplotlib.pyplot as plt
plt.title('plotting') # 그래프 제목
plt.plot([10, 20, 30, 40])
plt.show()


# - 그래프에 범례 넣기

# In[7]:


import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([10, 20, 30, 40], label='asc') # 증가를 의미하는 asc 범례
plt.plot([40, 30, 20, 10], label='desc') # 감소를 의미하는 desc 범례
plt.legend() # plt.legend(loc = 5) 처럼 loc를 통해 범례 위치 지정할 수 있음
plt.show()


# - 그래프 색상 바꾸기

# In[12]:


import matplotlib.pyplot as plt
plt.title('color') # 제목 설정
# 그래프 그리기
plt.plot([10, 20, 30, 40], color = 'skyblue', label = 'skyblue')
plt.plot([40, 30, 20, 10], 'pink', label = 'pink')
plt.legend() # 범례 표시
plt.show()


# - 그래프 선 모양 바꾸기

# In[14]:


import matplotlib.pyplot as plt
plt.title('linestyle') # 제목 설정
# 빨간색 dashed 그래프
plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
# 초록색 dotted 그래프
plt.plot([40, 30, 20, 10], color='g', ls=':', label='dotted')
plt.legend() # 범례 표시
plt.show()


# - 마커 모양 바꾸기

# In[16]:


import matplotlib.pyplot as plt
plt.title('marker') # 제목 설정
plt.plot([10, 20, 30, 40], 'r.', label='circle') # 빨간색 원형 마커 그래프
# 초록색 삼각형 마커 그래프
plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
plt.legend() # 범례 표시
plt.show()

